"""
Enterprise Knowledge Base — MCP Server
让 Claude Code 通过 MCP 协议检索知识库
"""
import sys
from pathlib import Path

# 加入项目根目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp.server.fastmcp import FastMCP

from server.documents import search_documents, get_document, list_recent
from server.categories import list_categories, get_category_tree, list_documents_by_category
from server.dashboard import get_dashboard

# ── 创建 MCP Server 实例 ──
mcp = FastMCP("enterprise-kb")


# ──────────────────────────────────────────────
# Tool 1: 全文搜索
# ──────────────────────────────────────────────
@mcp.tool()
def search_knowledge(query: str, category: str = None, tag: str = None, limit: int = 10) -> str:
    """全文搜索知识库文档，返回高亮摘要。

    Args:
        query: 搜索关键词
        category: 按分类名称过滤（可选）
        tag: 按标签名称过滤（可选）
        limit: 返回结果数量，默认 10
    """
    results = search_documents(query, category=category, tag=tag, limit=limit)
    if not results:
        return "未找到匹配的文档。"

    lines = []
    for r in results:
        lines.append(f"[{r['id']}] {r['title']}  (状态: {r['status']})")
        lines.append(f"    摘要: {r['snippet']}")
        lines.append("")
    return "\n".join(lines)


# ──────────────────────────────────────────────
# Tool 2: 获取文档详情
# ──────────────────────────────────────────────
@mcp.tool()
def get_document_detail(document_id: int) -> str:
    """获取文档的完整详情，包括标签、版本历史和附件。

    Args:
        document_id: 文档 ID
    """
    doc = get_document(document_id)
    if not doc:
        return f"文档 #{document_id} 不存在。"

    lines = []
    lines.append(f"标题: {doc['title']}")
    lines.append(f"状态: {doc['status']}")
    lines.append(f"分类: {doc['category_name']}")
    lines.append(f"作者: {doc['author_name']}")
    lines.append(f"标签: {', '.join(doc['tags']) or '无'}")
    lines.append(f"浏览: {doc['view_count']} 次")
    lines.append(f"创建: {doc['created_at']}")
    lines.append(f"更新: {doc['updated_at']}")
    lines.append("")

    # 版本历史
    if doc["versions"]:
        lines.append("── 版本历史 ──")
        for v in doc["versions"]:
            lines.append(f"  v{v['version_number']} — {v['change_summary']} ({v['changed_by_name']} @ {v['created_at']})")
        lines.append("")

    # 附件
    if doc["attachments"]:
        lines.append("── 附件 ──")
        for a in doc["attachments"]:
            size_kb = a["file_size"] // 1024 if a["file_size"] else "?"
            lines.append(f"  {a['filename']} ({size_kb} KB)")
        lines.append("")

    # 内容预览（前 500 字）
    if doc["content"]:
        lines.append("── 内容预览 ──")
        lines.append(doc["content"][:500])
        if len(doc["content"]) > 500:
            lines.append("... (内容已截断)")

    return "\n".join(lines)


# ──────────────────────────────────────────────
# Tool 3: 浏览分类树
# ──────────────────────────────────────────────
@mcp.tool()
def browse_categories(parent_id: int = None) -> str:
    """浏览知识库的分类树结构。

    Args:
        parent_id: 父分类 ID，不传则显示顶级分类
    """
    cats = list_categories(parent_id)
    if not cats:
        return "该分类下没有子分类。"

    lines = []
    for cat in cats:
        lines.append(f"[{cat['id']}] {cat['name']} — {cat.get('description', '')}")
    return "\n".join(lines)


# ──────────────────────────────────────────────
# Tool 4: 统计概览
# ──────────────────────────────────────────────
@mcp.tool()
def show_dashboard() -> str:
    """显示知识库的统计概览：文档数量、分类分布、热门搜索、最近更新。"""
    dash = get_dashboard()

    lines = []
    lines.append(f"文档: {dash['total_docs']} (已发布 {dash['published']} / 草稿 {dash['drafts']})")
    lines.append(f"分类: {dash['total_categories']}  用户: {dash['total_users']}  标签: {dash['total_tags']}")
    lines.append("")

    lines.append("── 分类分布 ──")
    for cat in dash["category_dist"]:
        lines.append(f"  {cat['name']}: {cat['count']} 篇")
    lines.append("")

    lines.append("── 热门搜索 ──")
    for s in dash["hot_search"]:
        lines.append(f"  \"{s['query']}\" — {s['count']} 次")
    lines.append("")

    lines.append("── 最近更新 ──")
    for doc in dash["recent_updates"]:
        lines.append(f"  {doc['title']} ({doc['author_name']})")

    return "\n".join(lines)


# ── 启动入口 ──
if __name__ == "__main__":
    mcp.run()
