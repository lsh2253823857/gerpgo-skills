---
name: gerpgo-api
label: 积加ERP开放平台API
description: 积加ERP开放平台API调用能力，支持运营、采购、物流、库存、财务等167个接口。当用户需要调用积加API、获取ERP数据、查询订单/库存/财务等业务数据时触发。
---

# 积加ERP开放平台API

当用户说"查/看/导出 XX 数据"时，按以下流程执行。

## Phase 0: 理解需求 → 定位接口

从用户的话中提取 3 个要素，查下方映射表：

| 要素 | 说明 | 示例 |
|------|------|------|
| 店铺 | `onSaleStore` 中的店铺名 | 翰融、源桐、希宇 |
| 市场 | US/DE/FR/UK/IT/ES/CA/JP | "美国"→US→20 |
| 数据 | 评论/库存/订单 etc | "差评"→Review+star≤3 |

### 意图→API 映射表

| 用户说 | Endpoint | 请求体关键字段 | 返回后处理 |
|--------|----------|---------------|-----------|
| "XX店的评论" | `/operation/crm/review/page` | `marketIds`, `page`, `pagesize` | 按 `onSaleStore` 过滤店铺 |
| "差评/低分" | 同上 | 同上 | + `star <= 3` |
| "好评" | 同上 | 同上 | + `star >= 4` |
| "近N天" | 同上 | `reviewDateBegin/End` (yyyy-MM-dd) | — |
| "Feedback" | `/operation/crm/feedback/page` | `marketIds`, `page`, `pagesize` | 同上 |
| "库存" | `/inventory/stock/list` | `marketIds`, `page`, `pagesize` | — |
| "采购单" | `/purchase/order/page` | `purchaseStartDate`, `page` | — |
| "FBA货件" | `/fulfillment/fba/shipment/list` | `page`, `pagesize` | — |
| "结算/财务" | `/finance/settlement/page` | `startDate`, `endDate`, `page` | — |

> 其他接口的参数详见 `references/gerpgo_complete_api_docs.json`

### ⏹ 确认
向用户复述 "你要查 [店铺] 在 [市场] 的 [数据]? (筛选条件: XXX)"，等用户确认再进入 Phase 1。说"不是"则回到提取步骤。

## Phase 1: 调用 API

1. 用 `scripts/gerpgo_client.py` 调用（凭证已记忆，无需填写）
2. 传入 endpoint + 请求体 JSON
3. ⏹ 调用前向用户展示 endpoint 和 body，确认后执行

```bash
# 示例：查美国站最近评论
python scripts/gerpgo_client.py /operation/crm/review/page \
  -d '{"marketIds":[20],"page":1,"pagesize":20}' -p

# 示例：导出为Excel
python scripts/gerpgo_client.py /operation/crm/review/page \
  -d '{"marketIds":[20],"page":1,"pagesize":100}' -o reviews.xlsx

# 示例：查德国站库存
python scripts/gerpgo_client.py /inventory/stock/list \
  -d '{"marketIds":[39],"page":1,"pagesize":20}' -p
```

4. 检查 `code: 200`，否则读 `messages` 字段，⏹ 问是否重试

## Phase 2: 输出结果

1. ⏹ 展示前几条预览，问用户要哪种输出：

| 输出方式 | 操作 |
|---------|------|
| **摘要** | 按输出模板提取关键字段，整理为文字/表格 |
| **Excel** | 重新调用加 `-o 文件名.xlsx` |
| **原始 JSON** | 加 `-p` 格式化展示 |

2. 执行后 ⏹ 问"还需要什么？"

### 输出模板

- **评论**: `[★×N] [买家] | [标题] | [日期] | ASIN:[asin] → [内容前100字]`
- **库存**: `[SKU] | [数量] | [库位] | [更新时间]`
- **订单**: `[订单号] | [金额] | [状态] | [日期]`

## 异常处理

| 场景 | 处理 |
|------|------|
| token过期 | 脚本自动获取，静默 |
| API报错(code≠200) | 读 messages，⏹ 问是否调整参数重试 |
| HTTP 4xx/5xx | 提示状态码，⏹ 问是否检查 endpoint |
| 结果空 | 提示无数据，⏹ 问是否换条件 |
| 限流429 | 等1秒自动重试，2次仍失败则 ⏹ 告知用户 |
| 凭证未设 | ⏹ 问是否手动输入 |

## 参考

### 站点 ID
US=20 | DE=39 | FR=40 | UK=36 | IT=30 | ES=29 | CA=35 | JP=25

### 完整接口文档
- 接口列表: `references/积加API接口使用文档.md`
- JSON参数: `references/gerpgo_complete_api_docs.json`
