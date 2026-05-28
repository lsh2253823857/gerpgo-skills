# GerpGo Skills — 积加ERP智能知识库

基于 SQLite + MCP 的企业知识库系统，集成积加ERP开放平台 167 个 API 接口文档，支持全文搜索和 AI Agent 检索。

## 架构

```
Claude Code Agent
       │ MCP 协议
       ▼
  MCP Server (Python)     ← 4 个工具：搜索/详情/分类/统计
       │ sqlite3
       ▼
  SQLite 知识库数据库      ← 188 篇文档 + FTS5 全文索引
```

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 初始化数据库
cd db && sqlite3 enterprise_kb.db < schema.sql && python seed_data.py

# 3. 导入积加API文档
python import_gerpgo.py

# 4. 启动 MCP Server
cd ../server && python main.py
```

## 目录结构

```
├── config.py                    # 数据库连接配置
├── requirements.txt             # 依赖（mcp）
├── db/
│   ├── schema.sql               # 8 表 + FTS5 + 触发器 + 索引
│   ├── seed_data.py             # 示例数据填充
│   ├── import_gerpgo.py         # 积加API文档导入脚本
│   └── enterprise_kb.db         # SQLite 数据库文件
├── server/
│   ├── main.py                  # MCP Server 入口
│   ├── documents.py             # 文档搜索（FTS5 + LIKE）
│   ├── categories.py            # 分类树查询（递归CTE）
│   └── dashboard.py             # 统计概览
└── skills/
    └── gerpgo-api/
        ├── SKILL.md             # Skill 定义（引用知识库）
        ├── scripts/
        │   └── gerpgo_client.py # 积加API调用客户端
        └── test-prompts.json    # 测试用例
```

## 数据库设计

| 表 | 用途 | 学的概念 |
|----|------|----------|
| users | 用户与角色 | 枚举约束、唯一索引 |
| categories | 分类树 | 自引用外键、递归CTE |
| documents | 知识文档 | 主外键、FTS关联 |
| tags | 标签 | 唯一约束 |
| document_tags | 多对多关联 | 复合主键、级联删除 |
| document_versions | 版本历史 | 审计追踪 |
| attachments | 文件附件 | BLOB vs 路径设计 |
| search_log | 搜索日志 | 聚合分析 |

## MCP 工具

| 工具 | 功能 |
|------|------|
| `search_knowledge(query, category, tag, limit)` | 全文搜索知识库 |
| `get_document_detail(document_id)` | 获取文档详情+版本+附件 |
| `browse_categories(parent_id)` | 浏览分类树 |
| `show_dashboard()` | 统计概览 |

## 积加API覆盖范围

| 分类 | 接口数 | 示例 |
|------|--------|------|
| 运营 — 评论与反馈 | Review, Feedback, 买家之声 |
| 运营 — 订单管理 | 订单查询、退款、退货、换货 |
| 运营 — 促销活动 | 促销、优惠券、秒杀 |
| 物流 — FBA | FBA货件、配送、移除 |
| 库存 — 库存管理 | 库存查询、调拨、出入库 |
| 采购 — 采购管理 | 采购单、供应商 |
| 财务 — 利润分析 | 利润、结算、成本 |
| 广告 — 广告数据 | 广告报表、关键词、ASIN |
| 产品 — 产品管理 | 产品资料、SKU、品类 |

## Skill 集成模式

```
Skill（流程逻辑）  →  MCP（查询接口）  →  数据库（知识存储）
                      按需检索             167 个 API
```

## License

MIT
