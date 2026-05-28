"""文档查询层 — 搜索、详情、列表"""
import sys
from pathlib import Path

# 把项目根目录加到 Python 路径，这样才能 import config
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import get_connection


def search_documents(query: str, category: str = None, tag: str = None, limit: int = 10) -> list[dict]:
    """全文搜索文档，返回高亮摘要。
    短查询（<3字符）用 LIKE 兜底，长查询用 FTS5 trigram。
    """
    conn = get_connection()

    # 构建公共过滤条件
    filter_sql = ""
    filter_params: list = []

    if category:
        filter_sql += " AND d.category_id IN (SELECT id FROM categories WHERE name = ?)"
        filter_params.append(category)

    if tag:
        filter_sql += " AND d.id IN (SELECT document_id FROM document_tags dt JOIN tags t ON t.id = dt.tag_id WHERE t.name = ?)"
        filter_params.append(tag)

    if len(query) >= 3:
        # FTS5 trigram 搜索（需要至少 3 个字符）
        sql = f"""
            SELECT d.id, d.title, d.status,
                   snippet(documents_fts, 1, '【', '】', '...', 40) AS snippet,
                   rank
            FROM documents_fts
            JOIN documents d ON d.id = documents_fts.rowid
            WHERE documents_fts MATCH ? AND d.is_deleted = 0
            {filter_sql}
            ORDER BY rank LIMIT ?
        """
        params = [query] + filter_params + [limit]
    else:
        # LIKE 兜底（短查询或中文两字）
        pattern = f"%{query}%"
        sql = f"""
            SELECT d.id, d.title, d.status,
                   substr(d.content, 1, 200) AS snippet,
                   0 AS rank
            FROM documents d
            WHERE (d.title LIKE ? OR d.content LIKE ?) AND d.is_deleted = 0
            {filter_sql}
            LIMIT ?
        """
        params = [pattern, pattern] + filter_params + [limit]

    rows = conn.execute(sql, params).fetchall()
    return [dict(row) for row in rows]


def get_document(doc_id: int) -> dict | None:
    """获取文档详情：基本信息 + 标签 + 版本历史"""
    conn = get_connection()

    # 基本信息
    doc = conn.execute(
        """SELECT d.*, c.name AS category_name, u.display_name AS author_name
           FROM documents d
           JOIN categories c ON c.id = d.category_id
           JOIN users u ON u.id = d.created_by
           WHERE d.id = ? AND d.is_deleted = 0""",
        (doc_id,)
    ).fetchone()

    if not doc:
        return None

    result = dict(doc)

    # 关联标签（多对多：document_tags → tags）
    result["tags"] = [
        row["name"] for row in conn.execute(
            """SELECT t.name FROM document_tags dt
               JOIN tags t ON t.id = dt.tag_id
               WHERE dt.document_id = ?""",
            (doc_id,)
        ).fetchall()
    ]

    # 版本历史（倒序：最新在前）
    result["versions"] = [
        dict(row) for row in conn.execute(
            """SELECT v.version_number, v.title_snapshot, v.change_summary,
                      u.display_name AS changed_by_name, v.created_at
               FROM document_versions v
               JOIN users u ON u.id = v.changed_by
               WHERE v.document_id = ?
               ORDER BY v.version_number DESC""",
            (doc_id,)
        ).fetchall()
    ]

    # 附件列表
    result["attachments"] = [
        dict(row) for row in conn.execute(
            """SELECT filename, file_path, mime_type, file_size, created_at
               FROM attachments
               WHERE document_id = ?""",
            (doc_id,)
        ).fetchall()
    ]

    # 浏览次数 +1
    conn.execute("UPDATE documents SET view_count = view_count + 1 WHERE id = ?", (doc_id,))
    conn.commit()
    conn.close()

    return result


def list_recent(limit: int = 10) -> list[dict]:
    """最近更新的文档列表"""
    conn = get_connection()
    rows = conn.execute(
        """SELECT d.id, d.title, d.status, d.updated_at,
                  c.name AS category_name, u.display_name AS author_name
           FROM documents d
           JOIN categories c ON c.id = d.category_id
           JOIN users u ON u.id = d.created_by
           WHERE d.is_deleted = 0
           ORDER BY d.updated_at DESC
           LIMIT ?""",
        (limit,)
    ).fetchall()
    return [dict(row) for row in rows]


# ── 手动测试 ──
if __name__ == "__main__":
    print("=== 最近更新 ===")
    for doc in list_recent(5):
        print(f"  [{doc['category_name']}] {doc['title']} ({doc['author_name']})")

    print("\n=== 搜索 'Python' ===")
    for result in search_documents("Python"):
        print(f"  {result['title']}")

    print("\n=== 文档 #1 详情 ===")
    detail = get_document(1)
    if detail:
        print(f"  标题: {detail['title']}")
        print(f"  分类: {detail['category_name']}")
        print(f"  标签: {', '.join(detail['tags'])}")
        print(f"  版本: {len(detail['versions'])} 个")
        print(f"  附件: {len(detail['attachments'])} 个")
