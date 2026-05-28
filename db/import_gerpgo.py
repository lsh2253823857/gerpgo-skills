"""
将积加 API 文档导入知识库
Usage: python import_gerpgo.py
"""
import re
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "enterprise_kb.db"
API_DOC = Path(r"D:\xiazai\gerpgo-skills-master\gerpgo-api\references\积加API接口使用文档.md")

# ── 分类规则：根据 endpoint 或标题关键词判断 ──
CATEGORY_RULES = [
    # (关键词列表, 分类名, 分类描述, 标签列表)
    (["review", "feedback", "买家之声", "评论"],       "运营 — 评论与反馈",   "评论、Feedback、买家之声相关 API",     ["运营", "评论", "Feedback"]),
    (["order", "订单", "退款", "退货", "换货", "发货"],  "运营 — 订单管理",     "订单查询、退款、退货、换货、发货 API",   ["运营", "订单"]),
    (["promotion", "促销", "优惠券", "秒杀", "折扣"],   "运营 — 促销活动",     "促销、优惠券、秒杀、会员折扣 API",      ["运营", "促销"]),
    (["fba/shipment", "fba货件", "fba配送"],           "物流 — FBA",          "FBA 货件、配送、移除订单 API",         ["物流", "FBA"]),
    (["inventory", "stock", "库存", "调拨", "出入库", "进销存"], "库存 — 库存管理", "库存查询、调拨、出入库记录 API",  ["库存"]),
    (["purchase", "采购", "供应商"],                    "采购 — 采购管理",     "采购单、供应商管理 API",              ["采购"]),
    (["finance", "settlement", "利润", "财务", "结算", "成本"], "财务 — 利润分析", "财务利润、结算、成本分析 API",    ["财务"]),
    (["advertising", "广告", "asin分析", "关键词", "搜索词", "投放", "品牌广告", "展示广告"], "广告 — 广告数据", "广告报表、关键词、ASIN 分析 API", ["广告"]),
    (["product", "sku", "msku", "产品", "商品", "品类", "品牌", "变体"], "产品 — 产品管理", "产品资料、SKU、品类、品牌 API", ["产品"]),
    (["fulfillment", "自发货", "自配送", "配货"],        "物流 — 自发货",       "自发货、自配送订单 API",              ["物流", "自发货"]),
    (["purchase/order", "采购单"],                       "采购 — 采购单",       "采购单管理 API",                     ["采购", "采购单"]),
]

# ── 默认分类（未匹配到规则时）──
DEFAULT_CATEGORY = ("其他 API", "其他未分类的 API", ["其他"])


def classify(title: str, endpoint: str) -> tuple[str, str, list[str]]:
    """根据标题和 endpoint 判断分类"""
    text = (title + " " + endpoint).lower()
    for keywords, cat_name, cat_desc, tags in CATEGORY_RULES:
        for kw in keywords:
            if kw.lower() in text:
                return cat_name, cat_desc, tags
    return DEFAULT_CATEGORY[0], DEFAULT_CATEGORY[1], DEFAULT_CATEGORY[2]


def parse_api_doc(filepath: Path) -> list[dict]:
    """解析 API 文档，按 ## N. 分割成独立条目"""
    content = filepath.read_text(encoding="utf-8")

    # 按 ## 数字. 分割
    sections = re.split(r'\n(?=## \d+\.)', content)

    apis = []
    for section in sections:
        # 提取标题
        title_match = re.match(r'## (\d+)\.\s*(.+)', section)
        if not title_match:
            continue

        api_num = int(title_match.group(1))
        api_title = title_match.group(2).strip()

        # 提取 endpoint
        endpoint_match = re.search(r'请求地址\s*\|\s*`([^`]+)`', section)
        endpoint = endpoint_match.group(1).strip() if endpoint_match else ""

        # 提取请求方式
        method_match = re.search(r'请求方式\s*\|\s*(\w+)', section)
        method = method_match.group(1).strip() if method_match else "POST"

        # 提取限流
        rate_match = re.search(r'限流规则\s*\|\s*(.+?)(?:\s*\||\s*$)', section)
        rate_limit = rate_match.group(1).strip() if rate_match else ""

        # 提取请求体参数（表格部分）
        req_params = ""
        req_section = re.search(r'### 请求体参数\s*\n(.*?)(?=\n###|\n---|\Z)', section, re.DOTALL)
        if req_section:
            req_params = req_section.group(1).strip()

        # 提取请求示例
        req_example = ""
        example_match = re.search(r'### 请求示例\s*\n```(?:json)?\s*\n(.*?)```', section, re.DOTALL)
        if example_match:
            req_example = example_match.group(1).strip()

        apis.append({
            "num": api_num,
            "title": api_title,
            "endpoint": endpoint,
            "method": method,
            "rate_limit": rate_limit,
            "req_params": req_params,
            "req_example": req_example,
            "full_content": section.strip(),
        })

    return apis


def import_to_db(apis: list[dict]):
    """导入到知识库数据库"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # 确保有"积加API"父分类
    cur.execute("SELECT id FROM categories WHERE name = '积加ERP API'")
    row = cur.fetchone()
    if row:
        parent_cat_id = row[0]
    else:
        cur.execute(
            "INSERT INTO categories (name, description, parent_id, sort_order) VALUES (?, ?, NULL, 10)",
            ("积加ERP API", "积加ERP开放平台 API 接口文档")
        )
        parent_cat_id = cur.lastrowid

    # 确保有"系统集成"角色用户（用于创建文档）
    cur.execute("SELECT id FROM users WHERE username = 'system_import'")
    row = cur.fetchone()
    if row:
        system_user_id = row[0]
    else:
        cur.execute(
            "INSERT INTO users (username, display_name, role) VALUES (?, ?, ?)",
            ("system_import", "系统导入", "admin")
        )
        system_user_id = cur.lastrowid

    # 确保标签存在
    all_tags = set()
    for api in apis:
        _, _, tags = classify(api["title"], api["endpoint"])
        all_tags.update(tags)
    all_tags.add("积加API")

    tag_ids = {}
    for tag_name in all_tags:
        cur.execute("SELECT id FROM tags WHERE name = ?", (tag_name,))
        row = cur.fetchone()
        if row:
            tag_ids[tag_name] = row[0]
        else:
            cur.execute("INSERT INTO tags (name) VALUES (?)", (tag_name,))
            tag_ids[tag_name] = cur.lastrowid

    # 确保子分类存在
    cat_cache = {}
    for api in apis:
        cat_name, cat_desc, _ = classify(api["title"], api["endpoint"])
        if cat_name not in cat_cache:
            cur.execute("SELECT id FROM categories WHERE name = ? AND parent_id = ?", (cat_name, parent_cat_id))
            row = cur.fetchone()
            if row:
                cat_cache[cat_name] = row[0]
            else:
                cur.execute(
                    "INSERT INTO categories (name, description, parent_id, sort_order) VALUES (?, ?, ?, 0)",
                    (cat_name, cat_desc, parent_cat_id)
                )
                cat_cache[cat_name] = cur.lastrowid

    # 导入文档
    imported = 0
    for api in apis:
        cat_name, _, tag_list = classify(api["title"], api["endpoint"])
        cat_id = cat_cache[cat_name]

        # 文档内容：精简版（endpoint + 参数 + 示例），用于搜索
        content_parts = [
            f"接口: {api['title']}",
            f"地址: {api['endpoint']}",
            f"方式: {api['method']}",
            f"限流: {api['rate_limit']}",
        ]
        if api["req_params"]:
            content_parts.append(f"请求参数:\n{api['req_params']}")
        if api["req_example"]:
            content_parts.append(f"请求示例:\n{api['req_example']}")
        content = "\n".join(content_parts)

        # 插入文档
        cur.execute(
            """INSERT INTO documents (title, content, category_id, created_by, status)
               VALUES (?, ?, ?, ?, 'published')""",
            (f"积加API — {api['title']}", content, cat_id, system_user_id)
        )
        doc_id = cur.lastrowid

        # 关联标签
        for tag_name in tag_list:
            cur.execute(
                "INSERT OR IGNORE INTO document_tags (document_id, tag_id) VALUES (?, ?)",
                (doc_id, tag_ids[tag_name])
            )
        # 额外加"积加API"标签
        cur.execute(
            "INSERT OR IGNORE INTO document_tags (document_id, tag_id) VALUES (?, ?)",
            (doc_id, tag_ids["积加API"])
        )

        imported += 1

    conn.commit()
    conn.close()
    print(f"导入完成: {imported} 个 API 文档, {len(cat_cache)} 个子分类, {len(tag_ids)} 个标签")


if __name__ == "__main__":
    print("解析 API 文档...")
    apis = parse_api_doc(API_DOC)
    print(f"解析到 {len(apis)} 个 API 接口")

    print("导入知识库...")
    import_to_db(apis)
