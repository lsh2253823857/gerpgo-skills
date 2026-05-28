"""
Seed data for enterprise_kb.db — 示例数据填充
Usage: python seed_data.py
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "enterprise_kb.db"


def seed():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # ──────────────────────────────────────────────
    # 1. Users (10+ users)
    # ──────────────────────────────────────────────
    users = [
        ("admin_wang",   "王明",       "admin"),
        ("admin_liu",    "刘洋",       "admin"),
        ("admin_chen",   "陈芳",       "admin"),
        ("editor_zhang", "张伟",       "editor"),
        ("editor_zhao",  "赵丽",       "editor"),
        ("editor_sun",   "孙强",       "editor"),
        ("editor_li",    "李静",       "editor"),
        ("editor_zhou",  "周涛",       "editor"),
        ("viewer_wu",    "吴磊",       "viewer"),
        ("viewer_huang", "黄蓉",       "viewer"),
        ("viewer_xu",    "许晴",       "viewer"),
        ("viewer_mao",   "毛星",       "viewer"),
    ]
    cur.executemany(
        "INSERT INTO users (username, display_name, role) VALUES (?, ?, ?)", users
    )

    # ──────────────────────────────────────────────
    # 2. Categories (树形: 2-3 levels)
    # ──────────────────────────────────────────────
    # 顶级分类
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (1,  '技术文档', '技术规范与架构资料', NULL, 1)")
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (2,  '业务知识', '客户、产品与销售知识', NULL, 2)")
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (3,  '团队管理', 'SOP 流程与团队规范', NULL, 3)")
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (4,  '公共资料', '公司通用文档', NULL, 4)")

    # 二级分类 — 技术文档
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (5,  '编码规范',   '各语言编码标准', 1, 1)")
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (6,  '架构设计',   '系统架构决策记录', 1, 2)")
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (7,  'API 文档',    '接口文档与变更记录', 1, 3)")

    # 二级分类 — 业务知识
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (8,  '产品规格',   '产品功能与规格说明', 2, 1)")
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (9,  '客户案例',   '成功案例与经验总结', 2, 2)")

    # 二级分类 — 团队管理
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (10, '发布流程',   '上线与部署 SOP', 3, 1)")
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (11, '会议纪要',   '周会与决策记录', 3, 2)")

    # 三级分类 — 编码规范下
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (12, 'Python 规范', 'Python 编码标准', 5, 1)")
    cur.execute("INSERT INTO categories (id, name, description, parent_id, sort_order) VALUES (13, 'JavaScript 规范', 'JS/TS 编码标准', 5, 2)")

    # ──────────────────────────────────────────────
    # 3. Documents (20+ documents)
    # ──────────────────────────────────────────────
    documents = [
        # (title, content, category_id, created_by, status)
        ("Python 编码规范 v2.0", """Python 编码规范 v2.0

一、命名规范
1. 模块名：小写，如 db_utils
2. 类名：大驼峰，如 DatabaseManager
3. 函数名：小写下划线，如 get_document_by_id
4. 常量：全大写，如 MAX_RETRY = 3

二、代码风格
1. 每行不超过 120 字符
2. 函数注释使用 Google 风格 docstring
3. import 顺序：标准库 → 第三方 → 本地模块

三、异常处理
1. 不要裸 except，至少捕获 Exception
2. 自定义异常继承自 BaseException 或其子类
3. 日志优先使用 logging 模块，不要用 print""", 12, 4, "published"),

        ("JavaScript 编码规范 v1.5", """JavaScript 编码规范 v1.5

一、命名规范
1. 变量和函数：camelCase，如 getUserInfo
2. 常量：UPPER_SNAKE_CASE，如 API_BASE_URL
3. 类名：PascalCase，如 UserService
4. 布尔变量以 is/has/can 开头

二、模块化
1. 每个文件只导出一个默认组件
2. 组件目录结构遵循 feature-based 组织
3. 避免循环依赖

三、性能建议
1. 使用 useMemo/useCallback 避免不必要的重渲染
2. 列表渲染必须提供稳定的 key
3. 避免在 render 中创建新对象""", 13, 5, "published"),

        ("微服务架构决策记录 ADR-001", """ADR-001: 微服务拆分策略

背景：
公司核心系统从单体架构迁移到微服务，需要确定拆分粒度。

决策：
1. 按业务域拆分（DDD bounded context），而非按技术层
2. 每个微服务独立数据库，不共享
3. 服务间通信优先使用异步消息（RabbitMQ），同步调用仅用于简单查询

利弊：
+ 各团队独立开发部署
+ 故障隔离，单个服务挂掉不影响全局
- 分布式事务复杂度增加
- 运维成本上升

状态：已采纳""", 6, 4, "published"),

        ("REST API 设计规范", """REST API 设计规范

一、URL 设计
1. 资源名词复数：/api/v1/documents
2. 层级嵌套不超过两级：/api/v1/users/{id}/documents
3. 过滤参数用 query string：?status=published&category=tech

二、HTTP 方法
- GET: 查询（幂等）
- POST: 创建
- PUT: 全量更新
- PATCH: 部分更新
- DELETE: 删除

三、响应格式
成功：{"code": 200, "data": {...}, "message": "success"}
失败：{"code": 400, "data": null, "message": "参数错误: title 不能为空"}

四、版本控制
使用 URL 路径版本号：/api/v1/...""", 7, 4, "published"),

        ("数据库迁移规范", """数据库迁移规范

一、原则
1. 所有 DDL 变更必须通过迁移脚本，禁止手动改表
2. 迁移脚本必须可回滚
3. 大表变更必须在低峰期执行

二、迁移脚本命名
{timestamp}_{description}.sql
示例：20260527_add_version_to_documents.sql

三、审批流程
1. 开发者提交迁移脚本
2. DBA 审核（SQL 正确性 + 性能影响）
3. 在 staging 环境验证
4. 生产环境执行（需双人确认）

四、回滚预案
每次迁移必须附带回滚脚本（down.sql）""", 6, 6, "published"),

        ("用户权限管理 API 文档", """用户权限管理 API

POST /api/v1/auth/login
  参数: {username: str, password: str}
  返回: {token: str, user: User}

GET /api/v1/users/{id}/permissions
  Header: Authorization: Bearer <token>
  返回: {permissions: [{resource: str, actions: [str]}]}

PUT /api/v1/users/{id}/role
  Header: Authorization: Bearer <token> (admin only)
  参数: {role: "admin" | "editor" | "viewer"}
  返回: {user: User}

DELETE /api/v1/users/{id}
  Header: Authorization: Bearer <token> (admin only)
  返回: {success: bool}""", 7, 4, "published"),

        ("产品规格 — 知识库搜索模块", """产品规格：知识库搜索模块

功能概述：
为企业知识库提供全文搜索能力，支持关键词搜索、分类筛选、标签过滤。

搜索算法：
1. 优先全文匹配（FTS5）
2. 次选模糊匹配（LIKE）
3. 结果按相关度排序（rank 值）

UI 要求：
- 搜索框支持自动补全
- 搜索结果高亮关键词
- 支持搜索历史（最近 20 条）
- 筛选器：分类、标签、时间范围

性能指标：
- 搜索响应 < 200ms
- 支持 10 万篇文档""", 8, 6, "published"),

        ("产品规格 — 文档协作模块", """产品规格：文档协作模块

功能概述：
支持多人编辑同一文档，保留版本历史，可回滚到任意版本。

核心流程：
1. 用户点击"编辑"获取锁
2. 编辑完成后点击"发布"释放锁并创建新版本
3. 超过 30 分钟未操作自动释放锁
4. 其他用户可在"编辑中"状态下查看只读版本

版本管理：
- 每次发布创建版本快照（完整内容）
- 版本列表显示：版本号、修改者、修改说明、时间
- 点击任意版本可查看详情

冲突处理：
- 如果两人同时编辑，先发布者成功
- 后发布者看到冲突提示，需合并或放弃""", 8, 5, "published"),

        ("数据库性能优化指南", """数据库性能优化指南

一、索引优化
1. WHERE/JOIN 常用列必须有索引
2. 复合索引遵循最左前缀原则
3. 避免在函数调用中使用索引列
4. 小表不需要索引

二、查询优化
1. SELECT 只取需要的列，不用 SELECT *
2. 大数据量分页使用游标而非 OFFSET
3. 避免子查询，优先 JOIN
4. EXPLAIN 分析执行计划

三、连接池
1. 生产环境必须使用连接池
2. 最大连接数 = CPU 核数 × 2 + 磁盘数
3. 设置连接超时和空闲回收

四、监控
1. 开启慢查询日志（阈值 500ms）
2. 定期 ANALYZE 更新统计信息""", 1, 4, "published"),

        ("客户案例 — ABC 金融公司知识库迁移", """案例：ABC 金融公司知识库迁移

背景：
ABC 金融公司原有 Confluence 知识库，文档散落在 200+ 空间，搜索效率低。
目标迁移到新知识库系统并统一分类。

挑战：
1. 历史文档 5000+ 篇，格式不统一
2. 部分文档有权限要求
3. 需要保留原始创建者和修改记录

方案：
1. 编写 Python 脚本批量导出 Confluence
2. Markdown 统一格式化
3. 自动分类（基于标题关键词 + NLP 分类）
4. 保留元数据（作者、时间、标签）

结果：
- 迁移完成率 98.5%
- 搜索效率提升 3 倍
- 用户满意度 4.5/5""", 9, 5, "published"),

        ("客户案例 — XYZ 制造业文档管理", """案例：XYZ 制造业文档管理

背景：
XYZ 公司需要管理 5000+ 工艺文件，传统文件服务器版本混乱。
引入知识库系统实现版本控制和权限管理。

方案：
1. 文件按工艺类别分类（8 大类、42 小类）
2. 每个文件有版本号（主版本.次版本）
3. 编辑审批流程：提交 → 审核 → 发布
4. 过期文件自动归档

关键指标：
- 文件检索时间从 10 分钟降到 30 秒
- 版本冲突事故降为 0
- 审批流程平均 2 个工作日完成""", 9, 6, "published"),

        ("发布流程 SOP v3", """发布流程 SOP v3

一、发布前准备
1. 代码合并到 release 分支
2. 运行全部单元测试和集成测试
3. 更新 CHANGELOG
4. 通知 QA 团队

二、发布执行
1. 创建生产部署任务
2. 按顺序执行：数据库迁移 → 后端部署 → 前端部署
3. 每一步确认健康检查通过后再继续下一步

三、发布后验证
1. 冒烟测试（核心路径）
2. 监控面板检查（错误率、延迟、QPS）
3. 保持观察 1 小时

四、回滚
1. 如果错误率 > 1% 或 P99 延迟翻倍，立即回滚
2. 回滚顺序：前端 → 后端 → 数据库（最后考虑）
3. 发送回滚通知到团队频道""", 10, 3, "published"),

        ("2026-Q1 周会纪要（第 5 周）", """2026-Q1 周会纪要（第 5 周）

日期：2026-02-02
参会：王明、刘洋、张伟、赵丽、周涛

议题一：知识库项目进展
- 数据库 schema 设计完成
- MCP Server 开发中
- 下周完成测试

议题二：新客户 ABC 需求确认
- 要求支持全文搜索
- 要求文档版本控制
- 需要在 3 月前上线

议题三：团队调整
- 周涛从运维组借调到知识库项目
- 月底前不再排其他任务

待办：
1. 张伟 — 完成 MCP Server 调试（2月5日前）
2. 赵丽 — 准备产品 demo 文案（2月6日前）
3. 刘洋 — 联系 ABC 确认最终需求（2月3日前）""", 11, 1, "published"),

        ("2026-Q1 周会纪要（第 6 周）", """2026-Q1 周会纪要（第 6 周）

日期：2026-02-09
参会：王明、刘洋、张伟、赵丽、周涛

议题一：知识库项目验收
- 功能测试通过
- 性能测试：10 万文档搜索 < 200ms
- 计划 2 月 15 日上线

议题二：ABC 客户 demo 反馈
- 客户满意搜索功能
- 建议增加"搜索结果导出"功能
- 同意 3 月 15 日交付

待办：
1. 张伟 — 上线前安全检查（2月12日前）
2. 赵丽 — 客户培训文档（2月14日前）
3. 周涛 — 生产环境准备（2月13日前）""", 11, 1, "published"),

        ("编码规范 — Go 语言基础", """Go 语言编码规范

一、命名
1. 包名：小写单词，不用下划线
2. 接口：以 er 结尾，如 Reader, Writer
3. 导出函数/变量：首字母大写，如 GetDocument
4. 内部函数/变量：首字母小写

二、错误处理
1. 永远检查 err，不要 _ 忽略
2. 使用 fmt.Errorf("xxx: %w", err) 包装错误
3. 避免 panic，用 error 返回值

三、并发
1. channel 优先，mutex 其次
2. 每个 goroutine 必须有退出条件
3. 使用 context 传递取消信号""", 5, 4, "published"),

        ("编码规范 — SQL 编写标准", """SQL 编写标准

一、格式规范
1. 关键字大写：SELECT, FROM, WHERE, JOIN
2. 表名和列名用下划线分隔（snake_case）
3. 每个 SELECT 的列单独一行
4. 缩进 4 个空格

二、性能原则
1. 禁止 SELECT *（除非确实需要全部列）
2. WHERE 条件避免在列上使用函数
3. JOIN 用 INNER JOIN 优先，明确需要时才用 LEFT JOIN
4. LIMIT 分页配合 ORDER BY 使用

三、安全
1. 禁止拼接 SQL，必须用参数化查询
2. 输入验证在应用层做，不信任数据库约束
3. 最小权限原则：只授予必要的数据库权限""", 5, 5, "draft"),

        ("架构 — 消息队列选型 ADR", """ADR-002: 消息队列选型

背景：
微服务间需要异步通信，需要选择消息队列方案。

候选方案：
1. RabbitMQ — 功能全面，生态成熟
2. Kafka — 高吞吐，适合大数据流
3. Redis Streams — 轻量，适合简单场景

决策：RabbitMQ

理由：
1. 当前业务不需要 Kafka 级别的吞吐量
2. RabbitMQ 支持复杂路由（topic exchange）
3. 团队已有 RabbitMQ 运维经验
4. 未来如果吞吐量需求增长，可引入 Kafka 作为补充

状态：已采纳""", 6, 4, "published"),

        ("架构 — 缓存策略设计", """缓存策略设计

一、缓存层级
1. L1 本地缓存（LruCache，单实例，TTL=60s）
2. L2 分布式缓存（Redis，集群共享，TTL=300s）

二、缓存更新策略
1. 写操作：先更新 DB，再删除缓存（cache-aside）
2. 不用写穿模式——避免缓存和 DB 不一致

三、缓存击穿防护
1. 热点 key 使用互斥锁（setnx）
2. 过期时间加随机偏移，避免同时过期

四、缓存雪崩防护
1. 缓存层做熔断
2. 多级 TTL（随机 ±20%）""", 6, 6, "published"),

        ("产品规格 — 用户认证模块", """产品规格：用户认证模块

功能：
1. 用户名密码登录
2. JWT Token 认证
3. 角色权限检查

Token 设计：
- Access Token：15 分钟过期
- Refresh Token：7 天过期
- 存储：Refresh Token 存数据库，Access Token 只在内存

安全要求：
1. 密码 bcrypt 哈希，至少 12 轮
2. 登录失败 5 次锁定 15 分钟
3. 敏感操作需要二次验证""", 8, 4, "published"),

        ("部署指南 — Docker 容器化", """Docker 容器化部署指南

一、镜像构建
1. 基础镜像用 python:3.12-slim
2. 多阶段构建减小镜像体积
3. .dockerignore 排除测试文件和文档

二、Docker Compose 配置
services:
  app:
    image: enterprise-kb:latest
    ports: ["8080:8080"]
    depends_on: [redis]
    volumes: [./db/enterprise_kb.db:/app/db/enterprise_kb.db]
  redis:
    image: redis:7-alpine
    volumes: [redis_data:/data]

三、生产环境
1. 使用健康检查 endpoint
2. 重启策略: unless-stopped
3. 日志输出到 stdout，由 Docker 日志驱动收集""", 1, 4, "draft"),

        ("项目 README — 知识库系统", """企业知识库系统 README

简介：
基于 SQLite + MCP 的企业知识库，支持全文搜索和版本管理。

快速开始：
1. cd enterprise-kb/db
2. sqlite3 enterprise_kb.db < schema.sql
3. python seed_data.py
4. cd ../server && python main.py

架构：
- 数据库: SQLite (WAL 模式)
- 搜索: FTS5 全文索引
- API: MCP 协议
- 语言: Python 3.10+

依赖：
- mcp (MCP SDK)
- sqlite3 (标准库)

License: MIT""", 4, 1, "published"),
    ]

    cur.executemany(
        """INSERT INTO documents (title, content, category_id, created_by, status)
           VALUES (?, ?, ?, ?, ?)""",
        documents,
    )

    # ──────────────────────────────────────────────
    # 4. Tags (15+ tags)
    # ──────────────────────────────────────────────
    tags = [
        "Python", "JavaScript", "Go", "SQL",
        "架构设计", "数据库", "性能优化", "安全",
        "编码规范", "API", "微服务", "缓存",
        "部署", "客户案例", "SOP", "产品规格",
    ]
    cur.executemany("INSERT INTO tags (name) VALUES (?)", [(t,) for t in tags])

    # ──────────────────────────────────────────────
    # 5. Document-Tag 关联 (M:N)
    # ──────────────────────────────────────────────
    doc_tag_links = [
        # doc_id, tag_id (1-indexed by insertion order)
        (1, 1), (1, 9),     # Python 编码规范 → Python, 编码规范
        (2, 2), (2, 9),     # JavaScript 编码规范 → JS, 编码规范
        (3, 5), (3, 11),    # 微服务架构 ADR → 架构设计, 微服务
        (4, 10), (4, 9),    # REST API 规范 → API, 编码规范
        (5, 6), (5, 9),     # 数据库迁移规范 → 数据库, 编码规范
        (6, 10), (6, 8),    # 用户权限 API → API, 安全
        (7, 16), (7, 10),   # 搜索模块规格 → 产品规格, API
        (8, 16),            # 文档协作规格 → 产品规格
        (9, 6), (9, 7),     # 数据库优化 → 数据库, 性能优化
        (10, 14),           # ABC 客户案例 → 客户案例
        (11, 14),           # XYZ 客户案例 → 客户案例
        (12, 15), (12, 13), # 发布 SOP → SOP, 部署
        (13, 15),           # 周会纪要 5 → SOP
        (14, 15),           # 周会纪要 6 → SOP
        (15, 3), (15, 9),   # Go 规范 → Go, 编码规范
        (16, 4), (16, 9),   # SQL 规范 → SQL, 编码规范
        (17, 5), (17, 11),  # MQ 选型 → 架构设计, 微服务
        (18, 5), (18, 12),  # 缓存策略 → 架构设计, 缓存
        (19, 16), (19, 8),  # 认证模块 → 产品规格, 安全
        (20, 13), (20, 6),  # Docker 部署 → 部署, 数据库
        (21, 13),           # README → 部署
    ]
    cur.executemany(
        "INSERT INTO document_tags (document_id, tag_id) VALUES (?, ?)", doc_tag_links
    )

    # ──────────────────────────────────────────────
    # 6. Document Versions (5+ versions)
    # ──────────────────────────────────────────────
    versions = [
        # (document_id, version_number, title_snapshot, content_snapshot, changed_by, change_summary)
        (1, 1, "Python 编码规范 v1.0", "初版 Python 编码规范，包含命名和注释基本规则。", 4, "初始版本"),
        (1, 2, "Python 编码规范 v1.5", "新增异常处理章节，补充 docstring 风格说明。", 5, "补充异常处理和 docstring 规范"),
        (1, 3, "Python 编码规范 v2.0", "全面更新，新增 import 顺序规范和性能建议。", 4, "v2.0 大版本更新"),
        (2, 1, "JavaScript 编码规范 v1.0", "初版 JS 编码规范。", 5, "初始版本"),
        (2, 2, "JavaScript 编码规范 v1.5", "新增 React 性能优化和模块化规范。", 4, "增加 React 和模块化规范"),
        (3, 1, "微服务架构决策记录 ADR-001", "初版 ADR，包含三个候选方案对比。", 4, "初始版本"),
        (4, 1, "REST API 设计规范 v1.0", "包含 URL 设计和 HTTP 方法规范。", 4, "初始版本"),
        (9, 1, "数据库性能优化指南 v1.0", "仅包含索引优化部分。", 4, "初始版本"),
        (9, 2, "数据库性能优化指南 v2.0", "新增查询优化、连接池和监控章节。", 6, "补充三大章节"),
    ]
    cur.executemany(
        """INSERT INTO document_versions
           (document_id, version_number, title_snapshot, content_snapshot, changed_by, change_summary)
           VALUES (?, ?, ?, ?, ?, ?)""",
        versions,
    )

    # ──────────────────────────────────────────────
    # 7. Attachments (3+ attachments)
    # ──────────────────────────────────────────────
    attachments = [
        # (document_id, filename, file_path, mime_type, file_size, uploaded_by)
        (1, "python_style_guide.pdf", "/uploads/docs/python_style_guide.pdf", "application/pdf", 245000, 4),
        (3, "adr001_diagram.png", "/uploads/docs/adr001_diagram.png", "image/png", 89000, 4),
        (4, "api_postman_collection.json", "/uploads/docs/api_postman.json", "application/json", 12300, 5),
        (12, "release_process_flowchart.svg", "/uploads/docs/release_flow.svg", "image/svg+xml", 5600, 3),
    ]
    cur.executemany(
        """INSERT INTO attachments (document_id, filename, file_path, mime_type, file_size, uploaded_by)
           VALUES (?, ?, ?, ?, ?, ?)""",
        attachments,
    )

    # ──────────────────────────────────────────────
    # 8. Search Log (10+ logs)
    # ──────────────────────────────────────────────
    search_logs = [
        # (user_id, query_text, results_count)
        (9,  "Python 编码规范", 3),
        (10, "微服务架构", 2),
        (11, "发布流程", 1),
        (4,  "API 设计", 2),
        (5,  "数据库优化", 2),
        (9,  "缓存", 1),
        (10, "客户案例", 2),
        (6,  "SOP", 2),
        (11, "权限管理", 1),
        (4,  "部署 Docker", 1),
        (5,  "JavaScript 规范", 1),
        (9,  "版本管理", 1),
    ]
    cur.executemany(
        "INSERT INTO search_log (user_id, query_text, results_count) VALUES (?, ?, ?)",
        search_logs,
    )

    conn.commit()
    conn.close()
    print("Seed data inserted successfully!")

    # ── 打印统计 ──
    conn = sqlite3.connect(DB_PATH)
    for table in ["users", "categories", "documents", "tags", "document_tags", "document_versions", "attachments", "search_log"]:
        count = conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {count} rows")
    conn.close()


if __name__ == "__main__":
    seed()
