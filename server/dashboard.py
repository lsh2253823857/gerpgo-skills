"""统计概览 — 聚合查询练习"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from config import get_connection


def get_dashboard() -> dict:
    """返回知识库的统计概览"""
    conn = get_connection()

    # ── 总量统计 ──
    stats = conn.execute("""
        SELECT
            COUNT(*)                                    AS total_docs,
            COUNT(CASE WHEN status = 'published' THEN 1 END) AS published,
            COUNT(CASE WHEN status = 'draft'     THEN 1 END) AS drafts,
            COUNT(DISTINCT category_id)                 AS total_categories,
            (SELECT COUNT(*) FROM users)                AS total_users,
            (SELECT COUNT(*) FROM tags)                 AS total_tags
        FROM documents
        WHERE is_deleted = 0
    """).fetchone()

    # ── 各分类文档数分布 ──
    category_dist = conn.execute("""
        SELECT c.name, COUNT(d.id) AS doc_count
        FROM categories c
        LEFT JOIN documents d ON d.category_id = c.id AND d.is_deleted = 0
        GROUP BY c.id
        HAVING doc_count > 0
        ORDER BY doc_count DESC
    """).fetchall()

    # ── 热门搜索词（按搜索次数降序）──
    hot_search = conn.execute("""
        SELECT query_text, COUNT(*) AS search_count
        FROM search_log
        GROUP BY query_text
        ORDER BY search_count DESC
        LIMIT 5
    """).fetchall()

    # ── 最近 5 篇更新 ──
    recent = conn.execute("""
        SELECT d.id, d.title, u.display_name AS author_name, d.updated_at
        FROM documents d
        JOIN users u ON u.id = d.created_by
        WHERE d.is_deleted = 0
        ORDER BY d.updated_at DESC
        LIMIT 5
    """).fetchall()

    conn.close()

    return {
        "total_docs":      stats["total_docs"],
        "published":       stats["published"],
        "drafts":          stats["drafts"],
        "total_categories": stats["total_categories"],
        "total_users":     stats["total_users"],
        "total_tags":      stats["total_tags"],
        "category_dist":   [{"name": r["name"], "count": r["doc_count"]} for r in category_dist],
        "hot_search":      [{"query": r["query_text"], "count": r["search_count"]} for r in hot_search],
        "recent_updates":  [dict(r) for r in recent],
    }


# ── 手动测试 ──
if __name__ == "__main__":
    dash = get_dashboard()

    print("=== 总量 ===")
    print(f"  文档: {dash['total_docs']} (已发布 {dash['published']} / 草稿 {dash['drafts']})")
    print(f"  分类: {dash['total_categories']}  用户: {dash['total_users']}  标签: {dash['total_tags']}")

    print("\n=== 分类分布 ===")
    for cat in dash["category_dist"]:
        print(f"  {cat['name']}: {cat['count']} 篇")

    print("\n=== 热门搜索 ===")
    for s in dash["hot_search"]:
        print(f"  \"{s['query']}\" — {s['count']} 次")

    print("\n=== 最近更新 ===")
    for doc in dash["recent_updates"]:
        print(f"  {doc['title']} ({doc['author_name']})")
