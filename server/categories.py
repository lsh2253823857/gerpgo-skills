"""分类树查询层 — 递归 CTE 遍历树形结构"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from config import get_connection


def list_categories(parent_id: int = None) -> list[dict]:
    """列出指定分类下的直接子分类（不递归展开）
    parent_id=None → 顶级分类
    parent_id=5   → 编码规范下的子分类
    """
    conn = get_connection()

    if parent_id is None:
        # 顶级分类：没有父级的那些
        sql = "SELECT * FROM categories WHERE parent_id IS NULL ORDER BY sort_order"
        params = ()
    else:
        sql = "SELECT * FROM categories WHERE parent_id = ? ORDER BY sort_order"
        params = (parent_id,)

    rows = conn.execute(sql, params).fetchall()
    return [dict(row) for row in rows]


def get_category_tree() -> list[dict]:
    """用递归 CTE 一次性拉出整棵分类树"""
    conn = get_connection()

    # 递归 CTE：从根节点开始，不断查找子节点
    sql = """
        WITH RECURSIVE cat_tree(id, name, parent_id, depth, path) AS (
            -- 起始条件：顶级分类（parent_id 为空）
            SELECT id, name, parent_id, 0, name
            FROM categories
            WHERE parent_id IS NULL

            UNION ALL

            -- 递归条件：查找当前层节点的子节点
            SELECT c.id, c.name, c.parent_id, t.depth + 1, t.path || ' > ' || c.name
            FROM categories c
            JOIN cat_tree t ON c.parent_id = t.id
        )
        SELECT * FROM cat_tree ORDER BY path
    """

    rows = conn.execute(sql).fetchall()
    return [dict(row) for row in rows]


def list_documents_by_category(cat_id: int, include_children: bool = False) -> list[dict]:
    """列出某个分类下的文档
    include_children=True → 包含子分类下的文档
    """
    conn = get_connection()

    if include_children:
        # 先用递归 CTE 找出所有子分类 id
        sql = """
            SELECT d.id, d.title, d.status, u.display_name AS author_name,
                   c.name AS category_name, d.updated_at
            FROM documents d
            JOIN users u ON u.id = d.created_by
            JOIN categories c ON c.id = d.category_id
            WHERE d.category_id IN (
                WITH RECURSIVE subcats(id) AS (
                    SELECT id FROM categories WHERE id = ?
                    UNION ALL
                    SELECT c.id FROM categories c JOIN subcats s ON c.parent_id = s.id
                )
                SELECT id FROM subcats
            ) AND d.is_deleted = 0
            ORDER BY d.updated_at DESC
        """
        params = (cat_id,)
    else:
        sql = """
            SELECT d.id, d.title, d.status, u.display_name AS author_name,
                   c.name AS category_name, d.updated_at
            FROM documents d
            JOIN users u ON u.id = d.created_by
            JOIN categories c ON c.id = d.category_id
            WHERE d.category_id = ? AND d.is_deleted = 0
            ORDER BY d.updated_at DESC
        """
        params = (cat_id,)

    rows = conn.execute(sql, params).fetchall()
    return [dict(row) for row in rows]


# ── 手动测试 ──
if __name__ == "__main__":
    print("=== 顶级分类 ===")
    for cat in list_categories():
        print(f"  [{cat['id']}] {cat['name']}")

    print("\n=== 完整分类树 ===")
    for cat in get_category_tree():
        indent = "  " * cat["depth"]
        print(f"  {indent}[{cat['id']}] {cat['name']}")

    print("\n=== 编码规范(5) 下的文档 ===")
    for doc in list_documents_by_category(5):
        print(f"  {doc['title']}")

    print("\n=== 编码规范(5) 含子分类的文档 ===")
    for doc in list_documents_by_category(5, include_children=True):
        print(f"  [{doc['category_name']}] {doc['title']}")
