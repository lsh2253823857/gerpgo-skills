# 积加开放平台 API 接口文档

本文档由自动化工具抓取生成，包含积加开放平台所有 API 接口的详细信息。

## 目录

1. [查询退货订单列表](#1-查询退货订单列表)
2. [查询商品信息列表](#2-查询商品信息列表)
3. [查询订单列表](#3-查询订单列表)
4. [查询订单详情](#4-查询订单详情)
5. [查询退款订单列表](#5-查询退款订单列表)
6. [查询订单发货信息](#6-查询订单发货信息)
7. [查询FBA配送信息列表](#7-查询FBA配送信息列表)
8. [查询FBA移除订单列表](#8-查询FBA移除订单列表)
9. [查询FBA移除订单详情](#9-查询FBA移除订单详情)
10. [查询FBA移除订单-物流信息](#10-查询FBA移除订单-物流信息)
11. [查询订单费用明细详情](#11-查询订单费用明细详情)
12. [保存推广资源](#12-保存推广资源)
13. [查询推广资源列表](#13-查询推广资源列表)
14. [查询推广费用列表](#14-查询推广费用列表)
15. [查询换货订单列表](#15-查询换货订单列表)
16. [ASIN分析](#16-ASIN分析)
17. [关键词表现](#17-关键词表现)
18. [搜索词表现](#18-搜索词表现)
19. [商品广告-关键词报表(V3)](#19-商品广告-关键词报表(V3))
20. [商品广告-商品报表(V3)](#20-商品广告-商品报表(V3))
21. [商品广告-广告活动(V3)](#21-商品广告-广告活动(V3))
22. [商品广告-广告位(V3)](#22-商品广告-广告位(V3))
23. [商品广告-用户搜索词-投放(V3)](#23-商品广告-用户搜索词-投放(V3))
24. [商品广告-用户搜索词-关键词(V3)](#24-商品广告-用户搜索词-关键词(V3))
25. [品牌广告-关键词报表(V3)](#25-品牌广告-关键词报表(V3))
26. [品牌广告-广告活动(V3)](#26-品牌广告-广告活动(V3))
27. [品牌广告-广告创意(V3)](#27-品牌广告-广告创意(V3))
28. [品牌广告-商品投放报表(V3)](#28-品牌广告-商品投放报表(V3))
29. [品牌广告-广告位(V3)](#29-品牌广告-广告位(V3))
30. [品牌广告-用户搜索词(V3)](#30-品牌广告-用户搜索词(V3))
31. [展示广告-广告活动(V3）](#31-展示广告-广告活动(V3）)
32. [展示广告-商品报表(V3)](#32-展示广告-商品报表(V3))
33. [分时策略NEW](#33-分时策略NEW)
34. [秒杀](#34-秒杀)
35. [优惠券](#35-优惠券)
36. [查询管理促销列表](#36-查询管理促销列表)
37. [查询会员折扣列表](#37-查询会员折扣列表)
38. [商品广告-投放(V3)](#38-商品广告-投放(V3))
39. [Feedback](#39-Feedback)
40. [Review](#40-Review)
41. [买家之声列表](#41-买家之声列表)
42. [查询标签管理信息](#42-查询标签管理信息)
43. [查询财务利润分析V2](#43-查询财务利润分析V2)
44. [查询财务利润分析V2-自定义字段](#44-查询财务利润分析V2-自定义字段)
45. [财务利润分析-月度查询V2](#45-财务利润分析-月度查询V2)
46. [财务利润分析-结算明细](#46-财务利润分析-结算明细)
47. [财务利润分析-分摊记录](#47-财务利润分析-分摊记录)
48. [商品统计](#48-商品统计)
49. [店铺统计](#49-店铺统计)
50. [产品表现](#50-产品表现)
51. [商品表现](#51-商品表现)
52. [店铺表现](#52-店铺表现)
53. [销售利润分析](#53-销售利润分析)
54. [流量统计-msku](#54-流量统计-msku)
55. [流量统计-ASIN](#55-流量统计-ASIN)
56. [流量数据-msku](#56-流量数据-msku)
57. [流量数据-ASIN](#57-流量数据-ASIN)
58. [采购/到库成本分析](#58-采购/到库成本分析)
59. [销售表现](#59-销售表现)
60. [查询产品列表](#60-查询产品列表)
61. [查询产品详情](#61-查询产品详情)
62. [查询SKU关联亚马逊MSKU](#62-查询SKU关联亚马逊MSKU)
63. [查询品类信息](#63-查询品类信息)
64. [录入品类信息](#64-录入品类信息)
65. [修改品类信息](#65-修改品类信息)
66. [新增产品资料](#66-新增产品资料)
67. [修改产品资料](#67-修改产品资料)
68. [录入父产品信息](#68-录入父产品信息)
69. [查询捆绑产品列表](#69-查询捆绑产品列表)
70. [查询品牌资料](#70-查询品牌资料)
71. [保存品牌资料](#71-保存品牌资料)
72. [同步产品到仓库](#72-同步产品到仓库)
73. [查询SKU关联多平台MSKU](#73-查询SKU关联多平台MSKU)
74. [查询父产品信息](#74-查询父产品信息)
75. [添加变体属性](#75-添加变体属性)
76. [查询变体属性](#76-查询变体属性)
77. [关联产品变体属性](#77-关联产品变体属性)
78. [查询产品库存](#78-查询产品库存)
79. [查询调拨单列表](#79-查询调拨单列表)
80. [查询调拨单详情](#80-查询调拨单详情)
81. [查询自营仓进销存列表(旧)](#81-查询自营仓进销存列表(旧))
82. [查询站点库存分布](#82-查询站点库存分布)
83. [出入库记录V2](#83-出入库记录V2)
84. [出入库明细V2](#84-出入库明细V2)
85. [查询FBA库存列表（旧）](#85-查询FBA库存列表（旧）)
86. [创建其他出库单-已完成状态](#86-创建其他出库单-已完成状态)
87. [创建其他出库单-草稿状态](#87-创建其他出库单-草稿状态)
88. [创建其他入库单-已完成状态](#88-创建其他入库单-已完成状态)
89. [创建其他入库单-草稿状态](#89-创建其他入库单-草稿状态)
90. [查询FBA库存列表V2](#90-查询FBA库存列表V2)
91. [自发货订单-配货单列表](#91-自发货订单-配货单列表)
92. [查询自配送订单列表](#92-查询自配送订单列表)
93. [自发货订单-销售订单列表](#93-自发货订单-销售订单列表)
94. [查询供应商信息](#94-查询供应商信息)
95. [录入供应商信息](#95-录入供应商信息)
96. [修改供应商信息](#96-修改供应商信息)
97. [查询供应商产品列表](#97-查询供应商产品列表)
98. [新增供应商产品](#98-新增供应商产品)
99. [修改供应商产品](#99-修改供应商产品)
100. [查询采购计划列表](#100-查询采购计划列表)
101. [查询采购计划明细](#101-查询采购计划明细)
102. [创建采购订单-草稿状态](#102-创建采购订单-草稿状态)
103. [采购订单-确认待交货](#103-采购订单-确认待交货)
104. [查询采购订单列表](#104-查询采购订单列表)
105. [查询采购订单详情](#105-查询采购订单详情)
106. [采购订单快捷入库-查询待入库列表](#106-采购订单快捷入库-查询待入库列表)
107. [采购订单快捷入库-确认入库](#107-采购订单快捷入库-确认入库)
108. [采购订单快捷入库-确认入库V2](#108-采购订单快捷入库-确认入库V2)
109. [采购订单变更单新增+自动审核](#109-采购订单变更单新增+自动审核)
110. [查询关联采购订单信息](#110-查询关联采购订单信息)
111. [创建采购交货单](#111-创建采购交货单)
112. [查询交货单列表](#112-查询交货单列表)
113. [查询交货单明细](#113-查询交货单明细)
114. [交货单（待发货状态）快捷入库](#114-交货单（待发货状态）快捷入库)
115. [查询采购退货单列表V2](#115-查询采购退货单列表V2)
116. [查询采购主体](#116-查询采购主体)
117. [查询自定义物流商列表](#117-查询自定义物流商列表)
118. [查询API物流商列表](#118-查询API物流商列表)
119. [物流-查看费用](#119-物流-查看费用)
120. [查询发货单列表](#120-查询发货单列表)
121. [查询发货单明细](#121-查询发货单明细)
122. [查询FBA货件列表](#122-查询FBA货件列表)
123. [查询FBA货件看板](#123-查询FBA货件看板)
124. [发货单-查看实际费用](#124-发货单-查看实际费用)
125. [发货单-查看分摊费用](#125-发货单-查看分摊费用)
126. [发货单-查看预估费用](#126-发货单-查看预估费用)
127. [查询物流费用金额明细](#127-查询物流费用金额明细)
128. [查询物流费用分摊明细](#128-查询物流费用分摊明细)
129. [查询发货单详情-装箱清单](#129-查询发货单详情-装箱清单)
130. [查询FBA货件装箱清单](#130-查询FBA货件装箱清单)
131. [批量新增发货单物流轨迹](#131-批量新增发货单物流轨迹)
132. [查询物流方式列表](#132-查询物流方式列表)
133. [发货单编辑](#133-发货单编辑)
134. [批量查询包裹单详情及费用](#134-批量查询包裹单详情及费用)
135. [查询仓库-FBA仓](#135-查询仓库-FBA仓)
136. [查询仓库-自营仓](#136-查询仓库-自营仓)
137. [查询仓库-供应商仓](#137-查询仓库-供应商仓)
138. [查询仓库信息列表](#138-查询仓库信息列表)
139. [查询库位信息](#139-查询库位信息)
140. [查询入库单列表V2](#140-查询入库单列表V2)
141. [查询仓库进销存](#141-查询仓库进销存)
142. [FBA进销存-成本](#142-FBA进销存-成本)
143. [FBA进销存-数量](#143-FBA进销存-数量)
144. [查询长期仓储费](#144-查询长期仓储费)
145. [查询月度仓储费](#145-查询月度仓储费)
146. [查询赔偿列表](#146-查询赔偿列表)
147. [查询退款单列表](#147-查询退款单列表)
148. [查询销售回款分析](#148-查询销售回款分析)
149. [查询月结算](#149-查询月结算)
150. [查询日期范围报告](#150-查询日期范围报告)
151. [查询付款单列表](#151-查询付款单列表)
152. [广告发票历史记录](#152-广告发票历史记录)
153. [查询其他费用分摊列表](#153-查询其他费用分摊列表)
154. [查询FBA进销存列表](#154-查询FBA进销存列表)
155. [FBA库存分类账-一览视图-按日维度列表查询](#155-FBA库存分类账-一览视图-按日维度列表查询)
156. [FBA库存分类账-详细视图列表查询](#156-FBA库存分类账-详细视图列表查询)
157. [查询库存动作列表](#157-查询库存动作列表)
158. [查询FBA盘库列表](#158-查询FBA盘库列表)
159. [查询已接收库存列表](#159-查询已接收库存列表)
160. [查询FBA库龄列表](#160-查询FBA库龄列表)
161. [FBA库存分类账-一览视图-按月维度列表查询](#161-FBA库存分类账-一览视图-按月维度列表查询)
162. [查询多平台销售订单](#162-查询多平台销售订单)
163. [查询多平台店铺信息](#163-查询多平台店铺信息)
164. [沃尔玛销售订单主列表](#164-沃尔玛销售订单主列表)
165. [沃尔玛销售订单](#165-沃尔玛销售订单)
166. [沃尔玛退货订单](#166-沃尔玛退货订单)
167. [获取多平台仓库列表](#167-获取多平台仓库列表)

---

## 1. 查询退货订单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询退货订单列表 |
| 请求地址 | `/operation/sale/returnOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| orderIds | array<string> | 否 | 订单编号集合，建议一次不要超过50 |
| purchaseStartDate | date | 否 | 订购开始时间(市场时间) [yyyy-MM-dd] |
| purchaseEndDate | date | 否 | 订购开始时间(市场时间) [yyyy-MM-dd] |
| returnStartDate | date | 否 | 退货开始时间(市场时间) [yyyy-MM-dd] |
| returnEndDate | date | 否 | 退货结束时间(市场时间) [yyyy-MM-dd] |
| updateTimeBegin | datetime | 否 | 修改开始时间 [yyyy-MM-dd HH:mm:ss] |
| updateTimeEnd | datetime | 否 | 修改结束时间 [yyyy-MM-dd HH:mm:ss] |
| createTimeBegin | datetime | 否 | 创建开始时间 [yyyy-MM-dd HH:mm:ss] |
| createTimeEnd | datetime | 否 | 创建结束时间 [yyyy-MM-dd HH:mm:ss] |
| marketIds | array<int> | 否 | 站点ID集合 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| orderId | string | 否 | 亚马逊订单编号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
  "createTimeBegin": "2022-12-13 00:14:37",
  "createTimeEnd": "2022-12-13 23:14:37",
  "page": 1,
  "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_dfa1f1ec917c4b62aceeff2f694156d5",
    "code": 200,
    "data": {
        "total": 96934,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "returnOrderQuantity": null,
                "reason": "NO_REASON_GIVEN",
                "purchaseDate": "2018-04-22 14:33:39",
                "fnsku": "FNGJX0000019",
                "orderId": "112-4382573-4467461",
                "tagIds": null,
                "returnDateZero": "2018-06-07 18:21:12",
                "sellableItems": null,
                "categoryName": "001-纯牛奶",
                "productName": "12",
                "tagNames": null,
                "marketId": 1,
                "customerComments": "gj test return sale order",
                "returnDate": "2018-06-07 11:21:12",
                "licensePlateNumber": "LPNGJ32",
                "imageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                "tagEchoVOList": [],
                "id": 32,
                "returnOrderItems": null,
                "sku": "12",
                "tagMemo": null,
                "returnDateTime": "2018-06-07 11:21:12",
                "msku": "TEST_MSKU_GJ ERP-QWE1754",
                "quantity": 1,
                "fulfillmentCenterId": "LEX2",
                "damagedItems": null,
                "listingTitle": "gj erp gogogo listing name",
                "updateTime": "2022-08-11 05:05:31",
                "expiredItems": null,
                "disposition": "CUSTOMER_DAMAGED",
                "createTime": "2022-12-13 21:14:37",
                "carrierDamagedItems": null,
                "defectiveItems": null,
                "asin": "BGJ0000004",
                "customerDamagedItems": null,
                "status": "Unit returned to inventory"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 2. 查询商品信息列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询商品信息列表 |
| 请求地址 | `/operation/sale/selling/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| marketIdList | array<long> | 否 | 店铺ID集合，如果商品数据较多，建议按单个店铺分别同步数据，会更有效率 |
| msku | string | 否 | MSKU，批量查询时使用逗号分隔 |
| asin | string | 否 | 商品ASIN，批量查询时使用逗号分隔 |
| variationAsin | string | 否 | 父ASIN，批量查询时使用逗号分隔 |
| sku | string | 否 | SKU，批量查询时使用逗号分隔 |
| spu | string | 否 | SPU，批量查询时使用逗号分隔 |
| isVague | int | 否 | 0：模糊搜索（默认），1：精确搜索 |
| fulfillment | string | 否 | 配送渠道 [AFN-亚马逊配送，MFN-卖家自配送] |
| addStartDate | date | 否 | 上架开始时间 [yyyy-MM-dd] |
| addEndDate | date | 否 | 上架结束时间 [yyyy-MM-dd] |
| firstSalesStartDate | date | 否 | 开售开始时间 [yyyy-MM-dd] |
| firstSalesEndDate | date | 否 | 开售结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [建议100条/页] |
| state | int | 否 | 销售状态 [0-在售，2-停售，3-不完整，4-删除] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 返回的提示信息 |
| traceId | string | 是 | 链路追踪id |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_febd55ac1f9e401a905ae23529bc37e4",
    "code": 200,
    "data": {
        "total": 2411,
        "size": 1,
        "footer": null,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "packageH": 1.18,
                "fnsku": "FNG*****008",
                "sevenPs": 0,
                "packageWeight": 1.60056,
                "salePriceAmount": {
                    "currencyAmount": 78.99,
                    "currencySymbol": "CA$",
                    "currencyCode": "CAD",
                    "amountWithSymbol": "CA$78.99"
                },
                "packageL": 11.89,
                "b2bPriceAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "CA$",
                    "currencyCode": "CAD",
                    "amountWithSymbol": null
                },
                "childList": null,
                "productName": null,
                "trialWarehouseFeeAmount": {
                    "currencyAmount": 6.49,
                    "currencySymbol": "CA$",
                    "currencyCode": "CAD",
                    "amountWithSymbol": "CA$6.49"
                },
                "packageW": 7.48,
                "asinType": "CHILD",
                "productH": null,
                "productL": null,
                "id": 1,
                "state": 0,
                "avgSevenPs": 0.0,
                "brand": null,
                "itemCondition": "",
                "brandName": "",
                "smallImageUrl": "https://gateway.apist.gerpgo.com/common/file?*******",
                "firstSalesDate": null,
                "listingTitle": "***",
                "upc": "",
                "groupNum": null,
                "variationAsin": "VG*****01",
                "packageHUnits": "inches",
                "mfnFulfillmentLatency": 10,
                "adjustStandardPriceAmount": {
                    "currencyAmount": 78.99,
                    "currencySymbol": "CA$",
                    "currencyCode": "CAD",
                    "amountWithSymbol": "CA$78.99"
                },
                "warehouseId": 3,
                "listingTitlePrint": "***",
                "storageTypeName": "未设置",
                "lastSevenPs": "0,0,0,0,0,0,0",
                "spu": "",
                "fbaQuantity": null,
                "thirtyPs": 0,
                "yesterdayPs": 0,
                "productNamePrint": null,
                "spuName": "",
                "ratingQuantity": 78,
                "listingLevel": null,
                "avgFifteenPs": 0.0,
                "sellingManagerName": null,
                "fifteenPs": 0,
                "categoryName": "未分配品类",
                "sellersRankList": [],
                "todayPs": 0,
                "marketId": 2,
                "adjustStartDate": "2020-11-30",
                "sellerSku": "TES*******E572",
                "productManagerName": null,
                "unBundling": false,
                "product": "",
                "productW": null,
                "packageWUnits": "inches",
                "avgThirtyPs": 0.0,
                "productWeight": null,
                "asinUrl": "https://www.amazon.ca/gp/product*******",
                "addDate": "2018-03-15 23:33:26",
                "adjustEndDate": "2020-12-30",
                "mfnQuantity": 100,
                "packageWeightUnits": "pounds",
                "averageStar": 4.1,
                "marketName": "一号店:CA",
                "normalImageUrl": "https://gateway.apist.gerpgo.com/common/file?******",
                "bindDate": null,
                "storageType": null,
                "asin": "BG******01",
                "fulfillment": "AFN",
                "category": "",
                "packageLUnits": "inches",
                "fbmQuantity": null,
                "listingState": null
            }
        ]
    },
    "messages": []
}
```

---

## 3. 查询订单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询订单列表 |
| 请求地址 | `/operation/sale/order/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | 亚马逊隐私政策要求买家信息有限返回，商品明细部分属性不返回有效值，请参考查询订单详情 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| shipFulfillment | string | 否 | 发货类型 [AFN-亚马逊配送，MFN-自配送] |
| orderType | string | 否 | 订单类型 [StandardOrder-亚马逊销售订单，Multichannel-多渠道订单，Patch-补单，Replace-换货订单，Promotion-促销订单] |
| orderIds | array<string> | 否 | 亚马逊订单ID集合[上限200个] |
| sellerOrderId | string | 否 | 卖家订单号 |
| sellerOrderIds | array<string> | 否 | 卖家订单号数组，建议一次不超过50 |
| marketIds | array<int> | 否 | 站点id数组 |
| shipmentsMethod | string | 否 | 发货方式 [pending-待录入，self_warehouse_shipments-自营仓发货，no_warehouse_shipments-无仓发货] |
| starList | array<int> | 否 | 评分 [0,1,2,3,4,5] |
| buyerEmails | array<string> | 否 | 买家邮箱数组，建议一次不超过50 |
| asins | array<string> | 否 | asin数组，建议一次不超过50 |
| skus | array<string> | 否 | sku数组，建议一次不超过50 |
| mskus | array<string> | 否 | msku数组，建议一次不超过50 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大200条/页] |
| startDate | date | 否 | 订单开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 订单结束时间 [yyyy-MM-dd] |
| lastUpdateStartDate | datetime | 否 | erp系统最后更新时间开始时间 [yyyy-MM-dd HH:mm:ss] |
| lastUpdateEndDate | datetime | 否 | erp系统最后更新时间结束时间 [yyyy-MM-dd HH:mm:ss] |
| orderStatusList | array<int> | 否 | 订单状态 [0-未付款，1-未发货，2-拣货中，3-已发货，4-已取消，5-预定订单，6-部分发货，7-无状态，8-无法配送] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 接口返回内容分页列表 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_1f09534aede64cff8daf3d33d3920a70",
    "code": 200,
    "data": {
        "total": 917164,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "addressPostalcode": null,
                "orderType": "StandardOrder",
                "purchaseDate": "2018-11-11 10:58:33",
                "orderId": "249-3556597-0107800",
                "lastUpdateDate": "2018-11-11 10:58:33",
                "addressCountrycode": null,
                "tbybOrder": 0,
                "orderStatus": 0,
                "salesChannel": "Amazon.co.jp",
                "buyerId": "",
                "serverId": 3,
                "addressStateorregion": null,
                "marketId": 11,
                "evaluation": false,
                "b2b": 0,
                "orderTotalAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "J￥",
                    "currencyCode": "JPY",
                    "amountWithSymbol": "J￥0.00"
                },
                "addressLine1": null,
                "addressLine2": null,
                "id": 67230,
                "addressLine3": null,
                "addressCity": null,
                "blockPrivateInfo": 1,
                "itemVos": [
                    {
                        "fid": 67230,
                        "smallImageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                        "listingTitle": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time jp033-black",
                        "listingLevel": "清尾产品",
                        "quantityOrdered": 1,
                        "asinUrl": "https://www.amazon.co.jp/gp/product/BGJ0000309",
                        "productName": "积加ERP测试产品518319516",
                        "promotionId": "",
                        "itemId": "",
                        "shippingTax": 0.0,
                        "promotionDiscount": 0.0,
                        "shippingPrice": 0.0,
                        "giftMessageText": "",
                        "spu": "",
                        "itemTax": 0.0,
                        "asin": "BGJ0000309",
                        "itemPrice": 2880.0,
                        "id": 109865,
                        "shippingDiscount": 0.0,
                        "buyerRequestedCancel": false,
                        "sellerSku": "TEST_MSKU_GJ ERP-QWE264",
                        "sku": "GJ ERP_TEST_SKU-24",
                        "buyerCancelReason": ""
                    }
                ],
                "vat": 0,
                "timeZone": "Asia/Tokyo",
                "orderTotal": 0.0,
                "addressPhone": null,
                "bogusFlag": false,
                "returns": 0,
                "replacedOrderId": "",
                "addressName": null,
                "fulfillment": "AFN",
                "currencyCode": "JPY",
                "sellerOrderId": "249-3556597-0107800",
                "refund": 0
            }
        ]
    },
    "messages": ["请求成功"]
}
```

---

## 4. 查询订单详情

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询订单详情 |
| 请求地址 | `/operation/sale/order/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | 亚马逊隐私政策要求买家信息有限返回 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| orderId | string | 是 | 亚马逊订单编号 |
| marketId | long | 是 | 站点ID |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 返回的提示信息 |
| traceId | string | 是 | 链路追踪id |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "marketId": 7,
    "orderId": "250-0352094-0012614"
}
```

### 响应示例

```json
{
    "traceId": "open_5b22bdba369840788fb1f0338460b8cd",
    "code": 200,
    "data": {
        "addressPostalcode": null,
        "orderType": "StandardOrder",
        "feedbackTemplate": 0,
        "purchaseDate": "2023-02-21 00:00:00",
        "updateDate": "2019-08-11 18:06:41",
        "orderId": "250-0352094-0012614",
        "addressCountrycode": null,
        "buyerEmail": null,
        "orderStatus": 3,
        "salesChannel": "Amazon.com.au",
        "buyerId": null,
        "serverId": 3,
        "addressStateorregion": null,
        "marketId": 7,
        "evaluation": false,
        "orderTotalAmount": {
            "currencyAmount": 68.19,
            "currencySymbol": "AU$",
            "currencyCode": "AUD",
            "amountWithSymbol": "AU$68.19"
        },
        "addressLine1": null,
        "addressLine2": null,
        "id": 180331,
        "tag": 0,
        "addressLine3": null,
        "addressCity": null,
        "distributionAddress": "",
        "lastDelivery": "2018-03-09 23:59:59",
        "shipmentLevel": "",
        "itemVos": [
            {
                "fid": 180331,
                "productVat": 0.0,
                "shippingDiscountAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "listingLevel": "",
                "quantityOrdered": 1,
                "productName": "",
                "promotionId": "",
                "shippingTax": 0.0,
                "promotionDiscount": 0.0,
                "productCost": 0.0,
                "giftMessageText": "",
                "id": 475779,
                "sellerSku": "TEST_MSKU_GJ ERP-QWE1686",
                "sku": "",
                "promotionDiscountAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "itemTaxAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "productShippingCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "smallImageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                "giftWrapPriceAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "listingTitle": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time K760-BK-AU",
                "productCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "asinUrl": "https://www.amazon.com.au/gp/product/BGJ0000130",
                "productArriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "giftWrapTax": 0.0,
                "itemId": "30569594888782",
                "quantityShipped": 1,
                "productArriveCost": 0.0,
                "shippingPrice": 0.0,
                "giftWrapPrice": 0.0,
                "itemPriceAmount": {
                    "currencyAmount": 68.19,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$68.19"
                },
                "itemTax": 0.0,
                "asin": "BGJ0000130",
                "itemPrice": 68.19,
                "shippingDiscount": 0.0,
                "productVatAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "buyerRequestedCancel": false,
                "giftWrapTaxAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "buyerCancelReason": "",
                "shippingPriceAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                },
                "shippingTaxAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "AU$",
                    "currencyCode": "AUD",
                    "amountWithSymbol": "AU$0.00"
                }
            }
        ],
        "earliestDelivery": "2018-02-22 00:00:00",
        "earliestShip": "2018-02-08 00:00:00",
        "timeZone": "Australia/Sydney",
        "shipmentWarehouse": "CN_GJ1",
        "buyerName": null,
        "shipFulfillment": "MFN",
        "shipServicelevel": "std-5",
        "orderTotal": 68.19,
        "lastShip": "2018-02-09 23:59:59",
        "reviewTemplate": 0,
        "addressPhone": null,
        "carrier": "",
        "shipTrack": "",
        "lastUpdatedate": "2018-02-02 20:59:25",
        "returns": 0,
        "addressName": null,
        "replacedOrderId": "",
        "shipNumber": 1,
        "currencyCode": "AUD",
        "sellerOrderId": "250-0352094-0012614"
    },
    "messages": ["请求成功"]
}
```

---

## 5. 查询退款订单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询退款订单列表 |
| 请求地址 | `/operation/sale/refundOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| orderId | string | 否 | 订单编码 |
| dateType | int | 是 | 搜索时间类型 [0-退款时间(零时区)，1-订购时间，2-退款时间市场时区] |
| startDate | date | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | date | 是 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketIds | array<int> | 否 | 站点集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
	"startDate": "2022-06-01",
	"endDate": "2022-06-16",
	"dateType": 0,
	"page": 1,
	"pagesize": 20
}
```

### 响应示例

```json
{
    "traceId": "open_f3c6a4e29f0a4fb4bd6ca749b3aa316f",
    "code": 200,
    "data": {
        "total": 61,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "purchaseDate": "2021-12-06 14:02:07",
                "settlementTimeMarket": "2021-12-15 04:01:55",
                "msku": "TEST_MSKU_GJ ERP-QWE425",
                "settlementTime": "2022-06-03 08:21:36",
                "orderId": "111-2488082-4277016",
                "price": 9.97,
                "marketAmount": {
                    "currencyAmount": 9.97,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$9.97"
                },
                "currency": "USD",
                "typeDetail": "Commission",
                "baseAmount": {
                    "currencyAmount": 66.4072,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥66.4072"
                },
                "marketId": 4
            }
        ]
    },
    "messages": ["请求成功"]
}
```

---

## 6. 查询订单发货信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询订单发货信息 |
| 请求地址 | `/operation/sale/orderFbaShipmentInfo/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| orderId | int | 是 | 订单主键 [通过订单列表接口获取] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "orderId": 849912
}
```

### 响应示例

```json
{
    "traceId": "open_7aa432147a774950ba8f6acc586c3ae7",
    "code": 200,
    "data": [
        {
            "updateDate": "2022-05-31 06:06:51",
            "msku": "********",
            "quantity": 1,
            "fnsku": null,
            "orderId": null,
            "earliestDelivery": "2022-05-31 20:00:00",
            "listingTitle": "**********",
            "asinUrl": "https://www.amazon.co.jp/gp/product/*****",
            "shipmentWarehouse": null,
            "productName": "",
            "marketId": 13,
            "serialNo": null,
            "wmsCode": null,
            "carrier": "YAMATO",
            "productImage": "https://m.media-amazon.com/images/**********",
            "shipTrack": "*********",
            "asin": "B*****5",
            "shipmentDate": "2022-05-31 01:10:14",
            "serialInfos": null,
            "sku": "",
            "shipmentWarehouseId": 0,
            "oldSku": null
        }
    ],
    "messages": [
        "request.success"
    ]
}
```

---

## 7. 查询FBA配送信息列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA配送信息列表 |
| 请求地址 | `/operation/sale/fbaShipment/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 必传一种时间，且时间范围不能超过14天 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| orderIds | array<string> | 否 | 订单ID |
| dateType | int | 是 | 时间类型 [0-市场时间，1-零时区时间] |
| purchaseStartDate | date | 否 | 订购开始时间 [yyyy-MM-dd] |
| purchaseEndDate | date | 否 | 订购结束时间 [yyyy-MM-dd] |
| shipmentStartDate | date | 否 | 发货开始时间 [yyyy-MM-dd]，请结合站点ID一起查 |
| shipmentEndDate | date | 否 | 发货结束时间 [yyyy-MM-dd]，请结合站点ID一起查 |
| estimatedArrivalDateBegin | date | 否 | 预计到达开始时间 [yyyy-MM-dd]，请结合站点ID一起查 |
| estimatedArrivalDateEnd | date | 否 | 预计到达结束时间 [yyyy-MM-dd]，请结合站点ID一起查 |
| createTimeBegin | datetime | 否 | 创建开始时间 [yyyy-MM-dd HH:mm:ss] |
| createTimeEnd | datetime | 否 | 创建结束时间 [yyyy-MM-dd HH:mm:ss] |
| updateTimeBegin | datetime | 否 | 修改开始时间 [yyyy-MM-dd HH:mm:ss] |
| updateTimeEnd | datetime | 否 | 修改结束时间 [yyyy-MM-dd HH:mm:ss] |
| orderTypes | array<string> | 否 | 订单类型 [StandardOrder-亚马逊销售订单，Multichannel-多渠道订单，Patch-补单，Replace-换货订单] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketIds | array<int> | 否 | 站点ID |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "dateType": 0,
    "updateTimeBegin": "2023-03-13 00:04:51",
    "updateTimeEnd": "2023-03-13 23:04:51"
}
```

### 响应示例

```json
{
    "traceId": "open_0d0516b8bb4d4ce2aabad073af5d146a",
    "code": 200,
    "data": {
        "total": 400,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "orderType": "StandardOrder",
                "orderId": "114-0556080-9513036",
                "buyerEmail": "gj@gerpgo.com",
                "purchaseDateZero": "2021-06-02 01:21:30",
                "shipServiceLevel": "Expedited",
                "shipmentItemId": "D7f55Wt7R",
                "salesChannel": "Amazon.com",
                "productName": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time",
                "shipPhoneNumber": null,
                "recipientName": null,
                "id": 3133919,
                "sku": "12",
                "trackingNumber": "test12345678",
                "itemTaxAmount": {
                    "currencyAmount": 5.08,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$5.08"
                },
                "paymentsDate": "2023-03-03 17:44:43",
                "msku": "TEST_MSKU_GJ ERP-QWE360",
                "giftWrapPriceAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$0.00"
                },
                "listingTitle": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time KBCase-K760RG",
                "shipmentDateZero": "2021-06-03 03:37:16",
                "itemPromotionDiscount": 0.0,
                "quantityShipped": 1,
                "shippingPrice": 0.0,
                "giftWrapPrice": 0.0,
                "shipState": null,
                "itemTax": 5.08,
                "estimatedArrivalDate": "2023-03-03 17:44:43",
                "giftWrapTaxAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$0.00"
                },
                "shipmentWarehouseId": 2,
                "shippingPriceAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$0.00"
                },
                "shippingTaxAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$0.00"
                },
                "purchaseDate": "2023-03-03 17:44:43",
                "updateDate": "2021-06-19 06:04:51",
                "produceName": "12",
                "shipPostalCode": null,
                "shipCountry": null,
                "marketId": 1,
                "shippingTax": 0.0,
                "imageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                "currency": "USD",
                "shipmentDate": "2023-03-03 17:44:43",
                "shipCity": null,
                "estimatedArrivalDateZero": "2021-06-04 03:00:00",
                "shipAddress1": null,
                "orderItemId": null,
                "fulfillmentCenterId": "FTW6",
                "shipAddress2": null,
                "shipmentWarehouseName": "一号店--有广告数据:US_FBA",
                "shipAddress3": null,
                "paymentsDateZero": "2021-06-03 04:53:25",
                "updateTime": "2023-03-13 17:44:43",
                "buyerName": null,
                "shipPromotionDiscount": 0.0,
                "giftWrapTax": 0.0,
                "marketName": "一号店--有广告数据:US",
                "carrier": "AMZN_US",
                "createTime": "2022-08-11 04:57:23",
                "shipmentId": "DvvqF07bf",
                "itemPriceAmount": {
                    "currencyAmount": 58.88,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$58.88"
                },
                "itemPrice": 58.88,
                "sellerOrderId": "114-0556080-9513036"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 8. 查询FBA移除订单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA移除订单列表 |
| 请求地址 | `/purchase/sale/storageRemovalOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| requestDateEnd | date | 否 | 请求结束时间 [yyyy-MM-dd] |
| updateTimeEnd | date | 否 | 更新结束时间 [yyyy-MM-dd] |
| updateTimeBegin | date | 否 | 更新开始时间 [yyyy-MM-dd] |
| page | int | 是 | 当前页 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| orderTypeList | array<string> | 否 | 移除方式 [Return-退货, Disposal-弃置, Liquidations-清算] |
| createWay | string | 否 | 创建方式 [0-亚马逊后台,1-系统内] |
| requestDateBegin | date | 否 | 请求开始时间 [yyyy-MM-dd] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回内容 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_718b4e5e58c040c0a90abf6d773cd6e4",
    "code": 200,
    "data": {
        "total": 2453,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "removeWayValue": "gip.removal.enumerate.Disposal",
                "orderId": "191031QI",
                "cancelledQuantity": 0,
                "updateTime": "2022-03-18 09:30:24",
                "shipWarehouseName": "一号店--有广告数据:US_FBA",
                "requestTime": "2019-10-31 00:18:04",
                "orderTotalQuantity": 45,
                "inventoryButton": false,
                "pendingQuantity": 0,
                "otherQuantity": 45,
                "closeButton": true,
                "shipWarehouseId": 2,
                "businessKey": "",
                "removeWayKey": "Disposal",
                "createWay": "亚马逊后台",
                "orderStatusValue": "已完成",
                "id": 3077,
                "orderStatusKey": "Completed"
            }
        ]
    },
    "messages": ["请求成功"]
}
```

---

## 9. 查询FBA移除订单详情

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA移除订单详情 |
| 请求地址 | `/purchase/sale/storageRemovalOrder/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| orderId | string | 是 | 订单编码 |
| warehouseId | long | 是 | 仓库ID |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "orderId": "211224PH3",
    "warehouseId": 2
}
```

### 响应示例

```json
{
    "traceId": "open_b2be149504514d87a258bd8a0445f6a3",
    "code": 200,
    "data": {
        "total": {
            "removalFeeUsdAmount": {
                "currencyAmount": 0.0,
                "currencySymbol": "$",
                "currencyCode": "USD",
                "amountWithSymbol": "$0.00"
            },
            "totalCostAmount": {
                "currencyAmount": 36.9987,
                "currencySymbol": "￥",
                "currencyCode": "CNY",
                "amountWithSymbol": "￥36.9987"
            },
            "shippedQuantity": 0,
            "requestedQuantity": 45,
            "inProcessQuantity": 0,
            "cancelledQuantity": 0,
            "usdCostAmount": {
                "currencyAmount": 36.9987,
                "currencySymbol": "￥",
                "currencyCode": "CNY",
                "amountWithSymbol": "￥36.9987"
            },
            "disposedAmount": {
                "currencyAmount": 36.9987,
                "currencySymbol": "￥",
                "currencyCode": "CNY",
                "amountWithSymbol": "￥36.9987"
            },
            "disposedQuantity": 45,
            "removalFeeAmount": {
                "currencyAmount": 0.0,
                "currencySymbol": "￥",
                "currencyCode": "CNY",
                "amountWithSymbol": "￥0.0000"
            },
            "usdArriveCostAmount": {
                "currencyAmount": 0.0,
                "currencySymbol": "￥",
                "currencyCode": "CNY",
                "amountWithSymbol": "￥0.0000"
            }
        },
        "removalOrderDetailsVo": {
            "orderType": "Disposal",
            "updateDate": "2020-02-20 22:40:50",
            "requesterDate": "2019-10-31 00:18:04",
            "memo": "",
            "warehouseId": 2,
            "removalFee": {
                "currencyAmount": 0.0,
                "currencySymbol": "￥",
                "currencyCode": "CNY",
                "amountWithSymbol": "￥0.0000"
            },
            "requestedQuantity": 45,
            "removalFeeUsd": {
                "currencyAmount": 0.0,
                "currencySymbol": "$",
                "currencyCode": "USD",
                "amountWithSymbol": "$0.00"
            },
            "requestedCost": {
                "currencyAmount": 36.9987,
                "currencySymbol": "￥",
                "currencyCode": "CNY",
                "amountWithSymbol": "￥36.9987"
            }
        },
        "removalOrderVoList": [
            {
                "orderType": "Disposal",
                "fnsku": "FNGJX0000022",
                "orderId": "191031QI",
                "orderStatus": "Completed",
                "usdArriveCost": 0.0,
                "removalFeeUsdAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$0.00"
                },
                "timezoneRequestDate": "2019-10-31 00:18:04",
                "totalCostAmount": {
                    "currencyAmount": 36.9987,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥36.9987"
                },
                "requestDate": "2019-10-31T07:18:04+00:00",
                "shippedQuantity": 0,
                "requestedQuantity": 1,
                "recordDate": "2020-02-20 22:40:50",
                "currency": "USD",
                "id": 3079,
                "sku": "GJ ERP_TEST_SKU-85",
                "inProcessQuantity": 0,
                "msku": "GJ ERP_TEST_SKU-85",
                "usdCost": 36.9987,
                "cancelledQuantity": 0,
                "usdCostAmount": {
                    "currencyAmount": 36.9987,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥36.9987"
                },
                "disposedAmount": {
                    "currencyAmount": 36.9987,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥36.9987"
                },
                "lastUpdatedDate": "2019-11-11T21:11:26+00:00",
                "disposition": "Sellable",
                "warehouseId": 2,
                "removalFee": "0.00",
                "disposedQuantity": 1,
                "removalFeeAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "usdArriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                }
            },
            {
                "orderType": "Disposal",
                "fnsku": "FNGJX0000023",
                "orderId": "191031QI",
                "orderStatus": "Completed",
                "usdArriveCost": 0.0,
                "removalFeeUsdAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$0.00"
                },
                "timezoneRequestDate": "2019-10-31 00:18:04",
                "totalCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "requestDate": "2019-10-31T07:18:04+00:00",
                "shippedQuantity": 0,
                "requestedQuantity": 18,
                "recordDate": "2020-02-20 22:40:50",
                "currency": "USD",
                "id": 3078,
                "sku": "GJ ERP_TEST_SKU-86",
                "inProcessQuantity": 0,
                "msku": "GJ ERP_TEST_SKU-86",
                "usdCost": 0.0,
                "cancelledQuantity": 0,
                "usdCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "disposedAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "lastUpdatedDate": "2019-11-11T21:11:26+00:00",
                "disposition": "Sellable",
                "warehouseId": 2,
                "removalFee": "0.00",
                "disposedQuantity": 18,
                "removalFeeAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "usdArriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                }
            },
            {
                "orderType": "Disposal",
                "fnsku": "FNGJX0000024",
                "orderId": "191031QI",
                "orderStatus": "Completed",
                "usdArriveCost": 0.0,
                "removalFeeUsdAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$0.00"
                },
                "timezoneRequestDate": "2019-10-31 00:18:04",
                "totalCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "requestDate": "2019-10-31T07:18:04+00:00",
                "shippedQuantity": 0,
                "requestedQuantity": 26,
                "recordDate": "2020-02-20 22:40:50",
                "currency": "USD",
                "id": 3077,
                "sku": "GJ ERP_TEST_SKU-87",
                "inProcessQuantity": 0,
                "msku": "GJ ERP_TEST_SKU-87",
                "usdCost": 0.0,
                "cancelledQuantity": 0,
                "usdCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "disposedAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "lastUpdatedDate": "2019-11-11T21:11:26+00:00",
                "disposition": "Sellable",
                "warehouseId": 2,
                "removalFee": "0.00",
                "disposedQuantity": 26,
                "removalFeeAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "usdArriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                }
            }
        ]
    },
    "messages": ["请求成功"]
}
```

---

## 10. 查询FBA移除订单-物流信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA移除订单-物流信息 |
| 请求地址 | `/purchase/sale/storageRemovalOrderWithShipment/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条] |
| orderIdList | array<string> | 否 | 移除订单编号集合 |
| page | int | 是 | 当前第几页 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 提示信息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page":1,
    "pagesize":1,
    "orderIdList": ["zqg812u+g4"]
}
```

### 响应示例

```json
{
    "traceId": "open_076ccd70b3e74b7b81062a4caeb3e6bc",
    "code": 200,
    "data": {
        "total": 3,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "orderType": "Disposal",
                "orderId": "zqg812u+g4",
                "orderStatus": "Completed",
                "returnWarehouseName": "",
                "updateTime": "2022-05-31 00:03:11",
                "warehouseName": "11:US_FBA",
                "orderTypeName": "弃置",
                "marketId": null,
                "requestTime": "2022-03-05 20:52:01",
                "orderStatusName": "已完成",
                "removalShipmentList": [
                    {
                        "carrier": "",
                        "msku": "********",
                        "fnsku": "*********",
                        "shippedQuantity": 1,
                        "memo": null,
                        "shipmentDateZero": null,
                        "shipmentDateTime": "2022-03-25 05:35:28",
                        "trackingNumber": ""
                    },
                    {
                        "carrier": "",
                        "msku": "P4*******OV",
                        "fnsku": "*******",
                        "shippedQuantity": 1,
                        "memo": null,
                        "shipmentDateZero": null,
                        "shipmentDateTime": "2022-04-21 02:02:51",
                        "trackingNumber": ""
                    }
                ],
                "returnWarehouseId": null,
                "warehouseId": 711
            }
        ]
    },
    "messages": []
}
```

---

## 11. 查询订单费用明细详情

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询订单费用明细详情 |
| 请求地址 | `/operation/sale/orderFee/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| fid | long | 是 | 订单主键 [订单列表接口获取] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示信息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
	"fid": 140477
}
```

### 响应示例

```json
{
    "traceId":"open_afcdf104c147467499eefde00c5598d6",
    "code":200,
    "data":[
        {
            "fid":"140477",
            "product":"GJ ERP_TEST_SKU-41",
            "quantity":1,
            "feeType":"Order",
            "typeDetail":"MarketplaceFacilitatorTax-Principal",
            "usdPrice":-28.67072,
            "settlementTime":"2019-06-13 21:24:15",
            "price":-4.16,
            "lastUpdate":"2019-06-19 00:05:31",
            "sellerSku":"TEST_MSKU_GJ ERP-QWE172",
            "priceAmount":{
                "currencyAmount":-4.16,
                "currencySymbol":"$",
                "currencyCode":"USD",
                "amountWithSymbol":"$-4.16"
            },
            "marketTime":"2019-06-13 14:24:15",
            "usdPriceAmount":{
                "currencyAmount":-28.67,
                "currencySymbol":"￥",
                "currencyCode":"CNY",
                "amountWithSymbol":"￥-28.67"
            }
        }
    ],
    "messages":[]
}
```

---

## 12. 保存推广资源

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 保存推广资源 |
| 请求地址 | `/operation/sale/resource/save` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| codeType | int | 是 | 生成编号方式 [0-系统生成, 1-手动填写] |
| contact | string | 否 | 推广资源联系人 |
| name | string | 是 | 推广资源名称 |
| paymentType | int | 是 | 结算方式 [1-现结, 2-月结] |
| paymentCycle | int | 否 | 结算周期 [结算方式为月结时才会有此参数] |
| paymentRuleCode | string | 否 | 付款条件编码 [财务-付款条件管理页面取值（需满足条件 状态=启用，费用类型=费用，结算方式=接口传入的结算方式），不传值按系统默认的付款条件进行付款] |
| phone1 | string | 否 | 联系人电话 |
| remark | string | 否 | 推广资源备注 |
| state | short | 是 | 状态 [0-启用, 1-停用] |
| receiptList | array<object> | 否 | 收款信息 |
| code | string | 否 | 推广资源编号 [通过code判断新增/修改，生成编号方式为手动填写时此字段为必填] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 返回的提示信息 |
| traceId | string | 是 | 链路追踪id |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "code": "openTest03",
    "codeType": 1,
    "contact": "",
    "name": "开放平台测试03",
    "paymentCycle": 0,
    "paymentRuleCode": "",
    "paymentType": 1,
    "phone1": "",
    "remark": "",
    "state": 0
}
```

### 响应示例

```json
{
    "traceId": "open_cebf986e6eca4583b95d227d4ee9875d",
    "code": 200,
    "data": null,
    "messages": [
        "保存推广资源成功"
    ]
}
```

---

## 13. 查询推广资源列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询推广资源列表 |
| 请求地址 | `/operation/sale/resource/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| state | int | 否 | 推广资源状态 [0-启用，1-停用] |
| timeType | int | 否 | 时间类型 [0-创建时间，1-更新时间] |
| startDate | string | 否 | 开始时间 [yyyy-MM-dd HH:mm:ss] |
| endDate | string | 否 | 结束时间 [yyyy-MM-dd HH:mm:ss] |
| page | int | 是 | 当前第几页 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| code | string | 否 | 推广资源编号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_9f7bb38ef0794ac79e33043c6c2de957",
    "code": 200,
    "data": {
        "total": 30,
        "condition": {
            "code": null,
            "endDate": null,
            "pagesize": 1,
            "name": null,
            "timeType": null,
            "page": 1,
            "sort": "seq",
            "state": null,
            "rows": 1,
            "startDate": null,
            "order": "asc"
        },    
        "pagesize": 1,
        "page": 1,   
        "rows": [
            {
                "code": "489",
                "codeType": null,
                "updateAt": "2020-06-18 17:35:44",
                "remark": "",
                "paymentType": 1,
                "phone1": "",
                "createdAt": "2020-06-18 17:35:17",
                "paymentRuleCode": null,
                "contact": "",
                "name": "站内服务商",
                "creater": "***",
                "state": 0,
                "createrId": 15,
                "receiptInfoList": [
                    {
                        "bankCode": "",
                        "accountType": null,
                        "name": "",
                        "bankName": ""
                    }
                ]
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 14. 查询推广费用列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询推广费用列表 |
| 请求地址 | `/operation/sale/openPromotionFee/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| recodeStartDate | date | 否 | 记录 - 开始日期 [yyyy-MM-dd] |
| recodeEndDate | date | 否 | 记录 - 结束日期 [yyyy-MM-dd] |
| happenStartDate | date | 否 | 费用发生 - 开始日期 [yyyy-MM-dd] |
| happenEndDate | date | 否 | 费用发生 - 结束日期 [yyyy-MM-dd] |
| apportionStartDate | date | 否 | 费用分摊 - 开始日期 [yyyy-MM-dd] |
| apportionEndDate | date | 否 | 费用分摊 - 结束日期 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketIds | array<long> | 否 | 店铺/站点集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_9dd0b20c490144b19a68b88df4b98fbf",
    "code": 200,
    "data": {
        "total": 355,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "recodeUserName": "莱特美特",
                "recodeUserId": 3411,
                "code": "OS2207190034",
                "marketCurrency": "USD",
                "description": null,
                "apportionRuleName": "按销售额均摊",
                "supplierCode": "45",
                "type": "MSKU",
                "baseCurrency": "CNY",
                "marketId": 1,
                "stateName": "已请款",
                "feeCode": "FYX202203070006",
                "currency": "CNY",
                "id": 34,
                "state": 3,
                "sku": "12",
                "supplierName": "德玛西亚",
                "msku": "TEST_MSKU_GJ ERP-QWE1026",
                "happenStartDate": "2023-03-28",
                "totalAmount": 1000.0,
                "marketName": "一号店--有广告数据:US",
                "apportionAmount": 1000.0,
                "happenEndDate": "2023-03-31",
                "apportionEndDate": "2022-06-30",
                "feeName": "KOL 推广_计入费用并请款",
                "recodeTime": "2023-05-15 17:15:22",
                "apportionStartDate": "2023-03-28",
                "category": "001-纯牛奶"
            }
        ]
    },
    "messages": []
}
```

---

## 15. 查询换货订单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询换货订单列表 |
| 请求地址 | `/operation/sale/replaceOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | 必传一种时间参数，且时间跨度不能超过14天 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| shipmentTimeStart | string | 否 | 配送时间开始 [yyyy-MM-dd HH:mm:ss] |
| shipmentTimeEnd | string | 否 | 配送时间开始 [yyyy-MM-dd HH:mm:ss] |
| createTimeStart | string | 否 | 创建时间开始 [yyyy-MM-dd HH:mm:ss] |
| createTimeEnd | string | 否 | 创建时间结束 [yyyy-MM-dd HH:mm:ss] |
| updateTimeStart | string | 否 | 修改时间开始 [yyyy-MM-dd HH:mm:ss] |
| updateTimeEnd | string | 否 | 修改时间结束 [yyyy-MM-dd HH:mm:ss] |
| replacementOrderIdList | array<string> | 否 | 换货订单编号列表 |
| originalOrderIdList | array<string> | 否 | 原订单编号列表 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketIds | array<int> | 否 | 站点ID列表 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 返回的提示信息 |
| traceId | string | 是 | 链路追踪id |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page":1,
    "pagesize":1,
    "createTimeStart": "2022-05-10 00:00:00",
    "createTimeEnd": "2022-05-20 00:00:00"
}
```

### 响应示例

```json
{
    "traceId": "open_c03b284743fc4ff787ae02aeeee0c89a",
    "code": 200,
    "data": {
        "total": 10405,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "replacementOrderId": "11*********401",
                "msku": "K*********U",
                "quantity": 1,
                "fulfillmentCenterid": "LGB3",
                "origFulfillmentCenterid": "LGB3",
                "updateTime": "2022-05-18 22:50:01",
                "shipmentDateTime": "2020-12-26 16:00:00",
                "marketId": 4,
                "skuName": "4*********）",
                "marketName": "****",
                "replacementReasonCode": "2",
                "originalOrderId": "1**********69",
                "createTime": "2022-05-18 22:50:01",
                "asin": "B0******Q",
                "id": 1,
                "shipmentDate": 1609027200000,
                "sku": "T*****W"
            }
        ]
    },
    "messages": [
        "请求成功"
    ]
}
```

---

## 16. ASIN分析

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | ASIN分析 |
| 请求地址 | `/operation/ads/adsAsinAnalytical/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| startDateData | string | 是 | 查询起始时间 [yyyy-MM-dd，开始时间需要等于结束时间] |
| endDateData | string | 是 | 查询结束时间 [yyyy-MM-dd，开始时间需要等于结束时间] |
| searchType | string | 否 | 查询类型 [商品标题: 0; asin: 1; msku: 2] |
| searchText | string | 否 | 查询内容 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页大小[最大100条/页] |
| marketId | long | 是 | 站点ID |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "marketId": 91,
    "startDateData": "2023-01-02",
    "endDateData": "2023-01-02",
    "page": 1,
    "pagesize": 20,
    "searchType":"2",
    "searchText":"********"
}
```

### 响应示例

```json
{
    "traceId": "open_49d70805839f44dba540d4553d9784dc",
    "code": 200,
    "data": {
        "total": 1,
        "pagesize": 20,
        "page": 1,
        "rows": [
            {
                "ctr": 0.15,
                "cost": 16.96,
                "msku": "*******",
                "asoas": null,
                "smallImageUrl": "https://m.media-amazon.com/images******",
                "listingTitle": "***********",
                "currencySymbol": "$",
                "cpu": 1.21,
                "impressions": 12472,
                "acos": 11.73,
                "asinURL": null,
                "sales": 144.56,
                "marketId": 91,
                "cr": 73.68,
                "orderProductSales": null,
                "cpc": 0.89,
                "clicks": 19,
                "roas": 8.52,
                "orders": 14,
                "asin": "********",
                "acoas": null,
                "cvr": 73.68
            }
        ]
    },
    "messages": []
}
```

---

## 17. 关键词表现

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 关键词表现 |
| 请求地址 | `/operation/ads/adsKeywordAnalytical/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketId | long | 是 | 站点ID |
| startDateData | date | 是 | 开始时间 [yyyy-MM-dd，开始时间需要等于结束时间] |
| endDateData | date | 是 | 结束时间 [yyyy-MM-dd，开始时间需要等于结束时间] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "marketId": 91,
    "startDateData": "2023-05-01",
    "endDateData": "2023-05-01",
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_3e40df88d9984836be31822b2a6fe478",
    "code": 200,
    "data": {
        "total": 121,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "ctr": 1.36,
                "cost": 23.6,
                "currencySymbol": "$",
                "cpu": 5.9,
                "impressions": 1399,
                "acos": 51.35,
                "sales": 45.96,
                "marketId": 91,
                "cr": 21.05,
                "keywordText": "*****",
                "cpc": 1.24,
                "clicks": 19,
                "roas": 1.95,
                "orders": 4
            }
        ]
    },
    "messages": []
}
```

---

## 18. 搜索词表现

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 搜索词表现 |
| 请求地址 | `/operation/ads/adsKeywordAnalytical/query` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页大小 [最大100条/页] |
| marketId | long | 是 | 站点ID |
| startDateData | date | 是 | 开始时间 [yyyy-MM-dd，开始时间需要等于结束时间] |
| endDateData | date | 是 | 结束时间 [yyyy-MM-dd，开始时间需要等于结束时间] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "marketId": 91,
    "startDateData": "2023-05-01",
    "endDateData": "2023-05-01",
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_3d1df5c91ee242dd8e31a85e85c99bf1",
    "code": 200,
    "data": {
        "total": 128,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "ctr": 0.43,
                "cost": 1.5,
                "query": "*****
                "currencySymbol": "$",
                "cpu": 0.0,
                "impressions": 235,
                "acos": 0.0,
                "sales": 0.0,
                "marketId": 91,
                "cr": 0.0,
                "cpc": 1.5,
                "adsType": "SP",
                "clicks": 1,
                "roas": 0.0,
                "orders": 0
            }
        ]
    },
    "messages": []
}
```

---

## 19. 商品广告-关键词报表(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品广告-关键词报表(V3) |
| 请求地址 | `/operation/ads/spKeywordsPage/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "startDataDate": "2023-01-01",
  "endDataDate": "2023-01-31",
  "count": 10,
  "marketId": 1,
  "nextId": 0
}
```

### 响应示例

```json
{
    "traceId": "open_2c4a519e3a884d4cba2ac3b0a8d02947",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "keywordId": "249877328010438",
            "otherProductSales": 0.0,
            "matchType": 2,
            "groupId": "245208428781471",
            "marketId": 1,
            "adsProductOrders": 0,
            "servingStatus": null,
            "cpa": 0.0,
            "cpc": 0.0,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "id": "36351",
            "state": 0,
            "portfolioName": null,
            "cvr": 0.0,
            "createDate": "2020-02-06",
            "ctr": 0.0,
            "adsOrders": 0,
            "cost": 0.0,
            "campaignId": 61100333832036,
            "impressions": 53,
            "acos": 0.0,
            "keywordText": "积加测试关键词721369795",
            "groupName": "积加测试广告组名称019883088",
            "portfolioId": null,
            "clicks": 0,
            "bid": 0.6,
            "campaignName": "GL-TYPEC3.0",
            "hash": "62f6e59f22797554e89ca81da852ad89"
        }
    ],
    "extObj": 36351,
    "messages": []
}
```

---

## 20. 商品广告-商品报表(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品广告-商品报表(V3) |
| 请求地址 | `/operation/ads/adsSpProduct/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间参数 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "marketId": 1,
    "count": 1,
    "startDate":"2022-01-15",
    "endDate":"2023-05-17",
    "nextId": 0
}
```

### 响应示例

```json
{
    "traceId": "open_77f725da81414428af4728d3e9e3b769",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "otherProductSales": 0.0,
            "groupId": "245208428781471",
            "marketId": 1,
            "adsProductOrders": 0,
            "servingStatus": "CAMPAIGN_PAUSED",
            "cpa": 0.0,
            "cpc": 0.0,
            "imageUrl": "https://demo.app.gerpgo.com/assets/images/logo.png",
            "adsProductSales": 0.0,
            "roas": 0.0,
            "groupTargetingType": 2,
            "id": "13614",
            "state": 0,
            "portfolioName": null,
            "cvr": 0.0,
            "createDate": "2020-02-06",
            "ctr": 0.0,
            "adsOrders": 0,
            "cost": 0.0,
            "msku": "GL-TYPEC3.0",
            "campaignId": 61100333832036,
            "listingTitle": "USB Type C Cable, GreenLaw 3.3 Feet USB C to USB A 3.0 Charging Cable for 12\", ChromeBook, Pixel, Nexus 6P, LG G5?Nokia N1 Tablet and More USB Type C Devices",
            "impressions": 53,
            "acos": 0.0,
            "groupName": "GL-TYPEC3.0",
            "portfolioId": null,
            "adId": "40223489010920",
            "clicks": 0,
            "asin": "B071YNC89G",
            "campaignName": "GL-TYPEC3.0",
            "hash": "0278c63eed08d2e2f3d481114b29a770"
        }
    ],
    "extObj": 13614,
    "messages": []
}
```

---

## 21. 商品广告-广告活动(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品广告-广告活动(V3) |
| 请求地址 | `/operation/ads/adsSpCampaigns/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "marketId": 1,
    "count": 1,
    "startDate":"2016-01-15",
    "endDate":"2023-05-17"
}
```

### 响应示例

```json
{
    "traceId": "open_6c96138e5b384b7dad76825f7c823be2",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "otherProductSales": 0.0,
            "endDate": null,
            "marketId": 1,
            "adsProductOrders": 0,
            "servingStatus": "CAMPAIGN_PAUSED",
            "cpa": 0.0,
            "cpc": 0.0,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "targetingType": 1,
            "id": "10625",
            "state": 0,
            "portfolioName": null,
            "cvr": 0.0,
            "createDate": "2020-02-06",
            "ctr": 0.0,
            "adsOrders": 0,
            "cost": 0.0,
            "campaignType": 0,
            "campaignId": 61100333832036,
            "impressions": 53,
            "acos": 0.0,
            "portfolioId": null,
            "dailyBudget": 10.0,
            "clicks": 0,
            "placement": null,
            "campaignName": "GL-TYPEC3.0",
            "startDate": "2017-05-30",
            "hash": "fa5a7d3e62448bb9864867e6170b22a6"
        }
    ],
    "extObj": 10625,
    "messages": []
}
```

---

## 22. 商品广告-广告位(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品广告-广告位(V3) |
| 请求地址 | `/operation/ads/adsSpPlacement/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 返回数据 |
| extObj | long | 否 | 返回扩展对象（最后一个id，查下一页的的入参） |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 追踪id |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "startDate": "2022-01-30",
  "endDate": "2023-01-31",
  "count": 1,
  "marketId": 91,
  "nextId": 0
}
```

### 响应示例

```json
{
    "traceId": "open_1f500a01dc664bd5813fddb3686a751a",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "otherProductSales": 0.0,
            "endDate": null,
            "marketId": 91,
            "adsProductOrders": 0,
            "servingStatus": "ACCOUNT_OUT_OF_BUDGET",
            "cpa": 0.0,
            "cpc": 0.0,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "targetingType": 0,
            "id": "228074",
            "state": 0,
            "portfolioName": "********",
            "cvr": 0.0,
            "createDate": "2023-01-04",
            "ctr": 0.0,
            "adsOrders": 0,
            "cost": 0.0,
            "campaignType": 0,
            "campaignId": 259629290038215,
            "impressions": 13,
            "acos": 0.0,
            "portfolioId": "211191311479110",
            "dailyBudget": 3.0,
            "clicks": 0,
            "placement": "D********zon",
            "campaignName": "B0***********品牌",
            "startDate": "2021-02-02",
            "hash": "8652d29898b544fe6098a2e764a038fb"
        }
    ],
    "extObj": 228074,
    "messages": []
}
```

---

## 23. 商品广告-用户搜索词-投放(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品广告-用户搜索词-投放(V3) |
| 请求地址 | `/operation/ads/spSearchTargetingReport/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| startDate | string | 否 | 查询开始时间yyyy-MM-dd （和数据时间至少传一个时间范围） |
| endDate | string | 否 | 查询结束时间yyyy-MM-dd（和数据时间至少传一个时间范围） |
| count | int | 是 | 查询条数（最多500条） |
| nextId | long | 否 | 下次查询ID |
| startDataDate | string | 否 | 数据开始时间：yyyy-MM-dd （和查询时间至少传一个时间范围） |
| endDataDate | string | 否 | 数据结束时间：yyyy-MM-dd（和查询时间至少传一个时间范围） |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 返回数据 |
| extObj | long | 否 | 返回扩展对象（最后一个id，查下一页的的入参） |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 链路ID |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "marketId":4,
    "count":1,
    "startDate":"2022-01-01",
    "endDate":"2022-07-31",
    "startDataDate":"2022-01-01",
    "endDataDate":"2022-07-31"
}
```

### 响应示例

```json
{
    "traceId": "open_efaa4d2efb81482fa3a1d3ec88c3441a",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "groupId": "107807875273335",
            "marketId": 4,
            "cpa": null,
            "cpc": 0.6,
            "roas": 0.0,
            "targetingType": "TARGETING_EXPRESSION_PREDEFINED",
            "id": "25842608",
            "portfolioName": "无人使用123",
            "cvr": 0.0,
            "ctr": 50.0,
            "adsOrders": 0,
            "cost": 0.6,
            "targetId": "146082188455977",
            "campaignId": 122823906686177,
            "query": "20 amp outdoor adapter",
            "impressions": 2,
            "acos": null,
            "targetingText": "loose-match",
            "groupName": "auJL-Christal-6-1-3 low bid-B08PBCJWX4",
            "portfolioId": "229652544801179",
            "clicks": 1,
            "campaignName": "auJL-Christal-6-1-3 low bid-B08PBCJWX4"
        }
    ],
    "extObj": 25842608,
    "messages": []
}
```

---

## 24. 商品广告-用户搜索词-关键词(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品广告-用户搜索词-关键词(V3) |
| 请求地址 | `/operation/ads/spSearchKeywordsReport/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| startDate | string | 否 | 查询开始时间yyyy-MM-dd （和数据时间至少传一个时间范围） |
| endDate | string | 否 | 查询结束时间yyyy-MM-dd（和数据时间至少传一个时间范围） |
| count | int | 是 | 查询条数（最多500条） |
| nextId | long | 否 | 下次查询ID |
| startDataDate | string | 否 | 数据开始时间：yyyy-MM-dd （和查询时间至少传一个时间范围） |
| endDataDate | string | 否 | 数据结束时间：yyyy-MM-dd（和查询时间至少传一个时间范围） |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 返回数据 |
| extObj | long | 否 | 返回扩展对象（最后一个id，查下一页的的入参） |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 链路ID |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "marketId":4,
    "count":1,
    "startDate":"2022-01-01",
    "endDate":"2022-07-31",
    "startDataDate":"2022-01-01",
    "endDataDate":"2022-07-31"
}
```

### 响应示例

```json
{
    "traceId": "open_983176c8d8094cb0860e2d2257687dbb",
    "code": 200,
    "data": [
        {
            "adsSales": 303.92,
            "keywordId": "89364978801944",
            "matchType": 0,
            "groupId": "154228557031875",
            "marketId": 4,
            "cpa": 9.32,
            "cpc": 1.86,
            "roas": 5.43,
            "id": "14158765",
            "portfolioName": "XEP-巨无霸词-B08Z2ZKVXX",
            "cvr": 20.0,
            "ctr": 0.2,
            "adsOrders": 6,
            "cost": 55.94,
            "campaignId": 88401954311988,
            "query": "surge protector",
            "impressions": 14990,
            "acos": 18.41,
            "keywordText": "surge protector",
            "groupName": "Ad group 1",
            "portfolioId": "168824825025250",
            "clicks": 30,
            "campaignName": "EMO-XEP-surge protector-up-top-B08Z2ZKVXX"
        }
    ],
    "extObj": 14158765,
    "messages": []
}
```

---

## 25. 品牌广告-关键词报表(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 品牌广告-关键词报表(V3) |
| 请求地址 | `/operation/ads/sbKeywordsPage/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "startDate": "2022-01-30",
  "endDate": "2023-01-31",
  "count": 1,
  "marketId": 1,
  "nextId": 0
}
```

### 响应示例

```json
{
    "traceId": "open_a86b28348a1e4dca822b3dbc5fb87167",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "keywordId": null,
            "otherProductSales": 0.0,
            "newBuyerOrderRatio": 0.0,
            "matchType": null,
            "groupId": "144244305632377399",
            "viewImpressions": 0,
            "marketId": null,
            "adsProductOrders": 0,
            "cpa": 0.0,
            "adsType": null,
            "cpc": 1.0,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "id": "57",
            "state": null,
            "portfolioName": null,
            "cvr": 0.0,
            "createDate": "2023-03-23",
            "ctr": 1.9,
            "adsOrders": 0,
            "cost": 10.0,
            "campaignId": null,
            "cpv": 0.0,
            "newBuyerOrders": 0,
            "newBuyerSales": 0.0,
            "impressions": 525,
            "acos": 0.0,
            "keywordText": null,
            "groupName": "积加测试广告组名称013507905",
            "portfolioId": null,
            "pageViews": 9,
            "clicks": 10,
            "bid": 0.0,
            "campaignName": null,
            "newBuyerSaleRatio": 0.0,
            "hash": "d0ed5bb11b1e0bcb6262503ec4d6f07b"
        }
    ],
    "extObj": 57,
    "messages": []
}
```

---

## 26. 品牌广告-广告活动(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 品牌广告-广告活动(V3) |
| 请求地址 | `/operation/ads/adsSbCampaign/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "startDate": "2022-01-30",
  "endDate": "2023-01-31",
  "count": 1,
  "marketId": 1,
  "nextId": 0
}
```

### 响应示例

```json
{
    "traceId": "open_5641a20f649a4ffea567d605ae4ad725",
    "code": 200,
    "data": [
        {
            "budgetType": 1,
            "adsSales": 0.0,
            "otherProductSales": 0.0,
            "newBuyerOrderRatio": 0.0,
            "endDate": null,
            "viewImpressions": 0,
            "marketId": 1,
            "adsProductOrders": 0,
            "servingStatus": "landingPageNotAvailable",
            "cpa": 0.0,
            "adsType": "SB",
            "cpc": 0.0,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "targetingType": -1,
            "id": "90",
            "state": 0,
            "portfolioName": "K960",
            "cvr": 0.0,
            "createDate": "2023-03-15",
            "budget": 1.0,
            "ctr": 0.0,
            "adsOrders": 0,
            "cost": 0.0,
            "campaignId": 144297881704259090,
            "cpv": 0.0,
            "newBuyerOrders": 0,
            "newBuyerSales": 0.0,
            "impressions": 35,
            "acos": 0.0,
            "asins": "B07P7KNF2M,B07TNHFS2M,B07SJY944J",
            "portfolioId": "71860224199509",
            "pageViews": 0,
            "clicks": 0,
            "campaignName": "K960 头条 2020.3.3",
            "newBuyerSaleRatio": 0.0,
            "startDate": "2020-03-03",
            "hash": "72363e846058334c1b84119a0cea15e5"
        }
    ],
    "extObj": 90,
    "messages": []
}
```

---

## 27. 品牌广告-广告创意(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 品牌广告-广告创意(V3) |
| 请求地址 | `/operation/ads/adsSbCreative/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array | 否 | 返回数据 |
| extObj | long | 否 | 返回扩展对象（最后一个id，查下一页的的入参） |
| messages | array | 否 | 返回的提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "startDate": "2023-01-30",
  "endDate": "2023-05-31",
  "count": 10,
  "marketId": 1
}
```

### 响应示例

```json
{
  "code": 200,
  "message": "",
  "data": [
    {
      "adsSales": 50.99,
      "otherProductSales": 50.99,
      "newBuyerOrderRatio": 100.00,
      "groupId": "189",
      "viewImpressions": 0,
      "marketId": 1,
      "adsProductOrders": 0,
      "servingStatus": "CAMPAIGN_PAUSED",
      "cpa": 7.57,
      "adsType": "SB",
      "cpc": 0.54,
      "adsProductSales": 0.00,
      "roas": 6.74,
      "id": "4751",
      "state": 0,
      "portfolioName": "****",
      "vcpm": null,
      "cvr": 7.14,
      "createDate": "2022-12-25",
      "ctr": 0.81,
      "adsOrders": 1,
      "adName": null,
      "cost": 7.57,
      "campaignId": 195,
      "cpv": 0.00,
      "newBuyerOrders": 1,
      "newBuyerSales": 50.99,
      "impressions": 1729,
      "acos": 14.85,
      "asins": "B****P,B8888CFD,B01*****W6",
      "groupName": "******",
      "portfolioId": "2707",
      "adId": "1449",
      "pageViews": 88,
      "creativeType": "PRODUCT_COLLECTION",
      "clicks": 14,
      "campaignName": "*****",
      "newBuyerSaleRatio": 100.00
    }
  ],
  "extObj": 4760,
  "messages": []
}
```

---

## 28. 品牌广告-商品投放报表(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 品牌广告-商品投放报表(V3) |
| 请求地址 | `/operation/ads/adsSbTargeting/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "marketId": 1,
    "count":1,
    "startDate":"2016-01-15",
    "endDate":"2023-05-17"
}
```

### 响应示例

```json
{
    "traceId": "open_4dc22fb11d104b348756d3414e63c309",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "otherProductSales": 0.0,
            "newBuyerOrderRatio": 0.0,
            "groupId": "*************",
            "viewImpressions": 0,
            "marketId": 1,
            "adsProductOrders": 0,
            "cpa": 0.0,
            "adsType": "SB",
            "cpc": 0.0,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "state": 0,
            "portfolioName": "*****",
            "cvr": 0.0,
            "createDate": "2022-01-24",
            "ctr": 0.0,
            "adsOrders": 0,
            "cost": 0.0,
            "targetId": "144151326649184543",
            "campaignId": 0,
            "cpv": 0.0,
            "newBuyerOrders": 0,
            "newBuyerSales": 0.0,
            "impressions": 15,
            "acos": 0.0,
            "groupName": "*********",
            "portfolioId": "***********",
            "pageViews": 0,
            "clicks": 0,
            "bid": 1.1,
            "campaignName": "************",
            "newBuyerSaleRatio": 0.0,
            "hash": "3514253579441826dda7d84d5726c269"
        }
    ],
    "extObj": 1966855,
    "messages": []
}
```

---

## 29. 品牌广告-广告位(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 品牌广告-广告位(V3) |
| 请求地址 | `/operation/ads/sbPlacementPage/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象（最后一个id，查下一页的的入参） |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "startDate": "2023-01-01",
  "endDate": "2023-01-31",
  "count": 10,
  "marketId": 1,
  "nextId": 0
}
```

### 响应示例

```json
{
    "traceId": "open_af0087fa73f849468a5e28da4ff3741f",
    "code": 200,
    "data": [
        {
            "budgetType": 1,
            "adsSales": 0.0,
            "otherProductSales": 0.0,
            "newBuyerOrderRatio": 0.0,
            "endDate": null,
            "viewImpressions": 0,
            "marketId": 1,
            "adsProductOrders": 0,
            "servingStatus": "landingPageNotAvailable",
            "cpa": 0.0,
            "adsType": "SB",
            "cpc": 0.0,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "targetingType": -1,
            "id": "90",
            "state": 0,
            "portfolioName": "K960",
            "cvr": 0.0,
            "budget": 1.0,
            "ctr": 0.0,
            "adsOrders": 0,
            "cost": 0.0,
            "campaignId": 144297881704259090,
            "cpv": 0.0,
            "newBuyerOrders": 0,
            "newBuyerSales": 0.0,
            "impressions": 35,
            "acos": 0.0,
            "asins": "B07P7KNF2M,B07TNHFS2M,B07SJY944J",
            "portfolioId": "71860224199509",
            "pageViews": 0,
            "clicks": 0,
            "placement": null,
            "campaignName": "K960 头条 2020.3.3",
            "newBuyerSaleRatio": 0.0,
            "startDate": "2020-03-03",
            "hash": "13d43c135ff007be1f56370b451adebd"
        }
    ],
    "extObj": 90,
    "messages": []
}
```

---

## 30. 品牌广告-用户搜索词(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 品牌广告-用户搜索词(V3) |
| 请求地址 | `/operation/ads/sbSearchKeywordsReport/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| startDate | string | 否 | 查询开始时间yyyy-MM-dd （和数据时间至少传一个时间范围） |
| endDate | string | 否 | 查询结束时间yyyy-MM-dd（和数据时间至少传一个时间范围） |
| count | int | 是 | 查询条数（最多500条） |
| nextId | long | 否 | 下次查询ID |
| startDataDate | string | 否 | 数据开始时间：yyyy-MM-dd （和查询时间至少传一个时间范围） |
| endDataDate | string | 否 | 数据结束时间：yyyy-MM-dd（和查询时间至少传一个时间范围） |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 返回数据 |
| extObj | long | 否 | 返回扩展对象（最后一个id，查下一页的的入参） |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 链路ID |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "marketId":4,
    "count":1,
    "startDate":"2022-01-01",
    "endDate":"2022-07-31",
    "startDataDate":"2022-01-01",
    "endDataDate":"2022-07-31"
}
```

### 响应示例

```json
{
    "traceId": "open_7580c1c8a38b48c18d21fb2522345ce4",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "keywordId": "144361454611318685",
            "matchType": 2,
            "groupId": "144357393016812936",
            "viewImpressions": 0,
            "marketId": 4,
            "cpa": 0.0,
            "cpc": 0.88,
            "roas": 0.0,
            "id": "29804513",
            "portfolioName": "无",
            "cvr": 0.0,
            "ctr": 20.0,
            "adsOrders": 0,
            "cost": 0.88,
            "campaignId": 144336532507969020,
            "query": "plug in surge protector outlet",
            "cpv": 0.0,
            "impressions": 5,
            "acos": 0.0,
            "keywordText": "surge protector outlet",
            "groupName": "SL-Katrina-KW-SquarePS-B085TC9N3K",
            "portfolioId": "182392152650804",
            "clicks": 1,
            "campaignName": "SL-Katrina-KW-SquarePS-B085TC9N3K"
        }
    ],
    "extObj": 29804513,
    "messages": []
}
```

---

## 31. 展示广告-广告活动(V3）

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 展示广告-广告活动(V3） |
| 请求地址 | `/operation/ads/adsSdCampaigns/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象（最后一个id，查下一页的的入参） |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 [成功: 0; 失败:1] |

### 请求示例

```json
{
    "marketId": 1,
    "count":1,
    "nextId":1,
    "startDataDate":"2023-08-31",
    "endDataDate":"2023-09-06"
}
```

### 响应示例

```json
{
    "traceId": "open_40b295e418da485786557c1ecb713062",
    "code": 200,
    "data": [
        {
            "budgetType": 1,
            "adsSales": 0.0,
            "otherProductSales": 0.0,
            "newBuyerOrderRatio": 0.0,
            "endDate": null,
            "viewImpressions": 0,
            "marketId": 1,
            "tactic": "T00020",
            "adsProductOrders": 0,
            "servingStatus": "CAMPAIGN_PAUSED",
            "cpa": 0.0,
            "costType": "cpc",
            "cpc": 1.48,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "id": "5",
            "state": 0,
            "portfolioName": null,
            "cvr": 0.0,
            "createDate": "2023-08-31",
            "budget": 30.0,
            "ctr": 0.3,
            "adsOrders": 0,
            "cost": 2.95,
            "campaignId": 83081736004970,
            "newBuyerOrders": 0,
            "newBuyerSales": 0.0,
            "impressions": 662,
            "acos": 0.0,
            "portfolioId": null,
            "pageViews": 0,
            "clicks": 2,
            "campaignName": "K961-SD 2020.5.31",
            "newBuyerSaleRatio": 0.0,
            "startDate": "2020-05-31",
            "hash": "8ca870dce9fd0ec7e1311e0da37988c1"
        }
    ],
    "extObj": 5,
    "messages": []
}
```

---

## 32. 展示广告-商品报表(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 展示广告-商品报表(V3) |
| 请求地址 | `/operation/ads/adsSdProduct/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据创建开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据创建结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 报表开始时间 [yyyy-MM-dd，对应返参createDate] |
| endDataDate | date | 否 | 报表结束时间 [yyyy-MM-dd，对应返参createDate] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "startDate": "2022-01-30",
  "endDate": "2023-01-31",
  "count": 1,
  "marketId": 1,
  "nextId": 0
}
```

### 响应示例

```json
{
    "traceId": "open_ea07461c4e29440ba09906c07141dd7e",
    "code": 200,
    "data": [
        {
            "adsSales": 0.0,
            "otherProductSales": 0.0,
            "newBuyerOrderRatio": 0.0,
            "groupId": "239817657491161",
            "viewImpressions": 0,
            "marketId": 1,
            "adsProductOrders": 0,
            "servingStatus": "CAMPAIGN_PAUSED",
            "cpa": 0.0,
            "costType": "cpc",
            "cpc": 1.48,
            "adsProductSales": 0.0,
            "roas": 0.0,
            "state": 0,
            "portfolioName": null,
            "cvr": 0.0,
            "createDate": "2023-03-23",
            "ctr": 0.3,
            "adsOrders": 0,
            "cost": 2.95,
            "msku": "K961BK",
            "campaignId": 83081736004970,
            "newBuyerOrders": 0,
            "newBuyerSales": 0.0,
            "impressions": 662,
            "acos": 0.0,
            "groupName": "K961-SD 2020.5.31",
            "portfolioId": null,
            "adId": "172593570417964",
            "pageViews": 0,
            "clicks": 2,
            "asin": "B07Z8P8M4R",
            "campaignName": "K961-SD 2020.5.31",
            "newBuyerSaleRatio": 0.0,
            "hash": "8af73b57114a871212c00982c01ac3b5"
        }
    ],
    "extObj": 5,
    "messages": []
}
```

---

## 33. 分时策略NEW

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 分时策略NEW |
| 请求地址 | `/operation/ads/strategyTemplate/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| model | object | 否 | 查询条件对象 |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page":1,
    "pagesize":10
}
```

### 响应示例

```json
{
    "traceId": "open_9b97a680b4cf40d7b57c36adb5243e47",
    "code": 200,
    "data": {
        "total": 17,
        "records": [
            {
                "templateType": "fixed",
                "createUserId": 5931,
                "templateExpression": "{\"isSetBasicValue\":1,\"adjustingWay\":0,\"timeExpression\":{\"rules\":[{\"date\":0,\"frequencies\":[{\"adjustmentType\":\"increaseByAFixedAmount\",\"placementTop\":0,\"endHour\":4,\"placementProductPage\":0,\"startHour\":1,\"state\":1},{\"adjustmentType\":\"increaseByAFixedAmount\",\"placementTop\":0,\"endHour\":10,\"placementProductPage\":0,\"startHour\":7,\"state\":0}]}],\"adjustFrequency\":0,\"autoParse\":1,\"displayMode\":1,\"dateList\":[0]}}",
                "countryNames": "美国",
                "endDate": "2023-01-31",
                "strategyRulesCode": "timeSharingEnablePause",
                "createUserName": "深圳市鸿鹄集",
                "strategyType": "timeSharingEnablePause",
                "messageType": "no",
                "useNum": 1,
                "countryIds": "1",
                "currency": "USD",
                "id": 25,
                "updateUserId": 5931,
                "updateUserName": "深圳市鸿鹄集",
                "currencySymbol": "$",
                "updateTime": "2023-01-11 14:58:41",
                "strategyRules": "分时启停",
                "templateName": "分时启停",
                "createTime": "2023-01-11 14:58:41",
                "startDate": "2023-01-11",
                "status": 1
            }
        ]
    },
    "messages": []
}
```

---

## 34. 秒杀

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 秒杀 |
| 请求地址 | `/operation/ads/deal/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据更新开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据更新结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 数据开始时间 [yyyy-MM-dd] |
| endDataDate | date | 否 | 数据结束时间 [yyyy-MM-dd] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | number | 是 | 响应码 |
| data | array<object> | 是 | 接口返回数据 |
| extObj | int | 是 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | null | 是 | 接口返回traceId |

### 请求示例

```json
{
    "marketId": 1,
    "count": 1,
    "startDate":"2016-01-15",
    "endDate":"2023-05-17"
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": [
        {
            "endDate": "2021-08-08 23:45:00",
            "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
            "feeRate": 2.15,
            "sales": 13946.2,
            "marketId": 1,
            "unitSales": 252,
            "firstSyncTime": "2021-06-30 03:00:11",
            "salesAmount": {
                "currencyAmount": 13946.2,
                "currencySymbol": "$",
                "currencyCode": "USD",
                "amountWithSymbol": "$13946.20"
            },
            "boutiqueAsinUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
            "id": "137",
            "dealFee": "$300.00",
            "dealType": "BEST_DEAL",
            "adsOpenDealGoodsVOList": [
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE219",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "iPad Keyboard Case for iPad 8th Gen 2020/ 7th Gen 2019 10.2 inch, iPad Air 3rd Gen 10.5 2019, iPad Pro 10.5 2017-7 Color Backlit/ 343 Mixed Mode - Detachable- Thin & Light- Auto Sleep Wake, Black",
                    "sales": 0.0,
                    "marketId": 1,
                    "unitSales": 0,
                    "salesAmount": {
                        "currencyAmount": 0.0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0.00"
                    },
                    "price": 56.06,
                    "averagePriceAmount": {
                        "currencyAmount": 0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0"
                    },
                    "asin": "BGJ0000496",
                    "averagePrice": 0
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE1158",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "iPad Pro 11 Case with Keyboard 2018-360 Rotatable - Wireless/BT - Backlit 17 Color - Auto Sleep Wake - iPad Pro 11 Keyboard Case - Support Apple Pencil 2nd Gen Charging, Black",
                    "sales": 0.0,
                    "marketId": 1,
                    "unitSales": 0,
                    "salesAmount": {
                        "currencyAmount": 0.0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0.00"
                    },
                    "price": 53.54,
                    "averagePriceAmount": {
                        "currencyAmount": 0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0"
                    },
                    "asin": "BGJ0000318",
                    "averagePrice": 0
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE316",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "iPad 8th Generation Case with Keyboard, 7 Color Backlit, 343 Mixed Mode, Detachable Keyboard Case for iPad 7th Gen, Thin & Light, Auto Sleep Wake, iPad 10.2/10.5 inch, iPad Air 3rd Gen, Rose Gold",
                    "sales": 112.12,
                    "marketId": 1,
                    "unitSales": 2,
                    "salesAmount": {
                        "currencyAmount": 112.12,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$112.12"
                    },
                    "price": 56.06,
                    "averagePriceAmount": {
                        "currencyAmount": 56.06,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$56.06"
                    },
                    "asin": "BGJ0000527",
                    "averagePrice": 56.06
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE1690",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "GreenLaw iPad Pro 11 inch 2020/2018 Case with Keyboard - 360° Rotatable-17 Backlit Color-Support Wake/Sleep-Wireless Keyboard Case for iPad Pro 11 2nd/ 1st Generation, Rose Gold",
                    "sales": 2106.78,
                    "marketId": 1,
                    "unitSales": 37,
                    "salesAmount": {
                        "currencyAmount": 2106.78,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$2106.78"
                    },
                    "price": 56.94,
                    "averagePriceAmount": {
                        "currencyAmount": 56.94,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$56.94"
                    },
                    "asin": "BGJ0000415",
                    "averagePrice": 56.94
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE1824",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "iPad Pro 11 Case with Keyboard 2020/2018 (1st/ 2nd Generation) - 360 Rotatable - Wireless/BT - Backlit 17 Color - Auto Sleep Wake - Support Apple Pencil 2nd Gen Charging, Black Sliver",
                    "sales": 0.0,
                    "marketId": 1,
                    "unitSales": 0,
                    "salesAmount": {
                        "currencyAmount": 0.0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0.00"
                    },
                    "price": 54.39,
                    "averagePriceAmount": {
                        "currencyAmount": 0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0"
                    },
                    "asin": "BGJ0000586",
                    "averagePrice": 0
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE397",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "iPad Pro 11 Case with Keyboard 2018-360 Rotatable - Wireless/BT - Backlit 17 Color - Auto Sleep Wake - Thin & Light - iPad Case with Keyboard?Support Apple Pencil 2nd Gen Charging?",
                    "sales": 0.0,
                    "marketId": 1,
                    "unitSales": 0,
                    "salesAmount": {
                        "currencyAmount": 0.0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0.00"
                    },
                    "price": 54.39,
                    "averagePriceAmount": {
                        "currencyAmount": 0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0"
                    },
                    "asin": "BGJ0000395",
                    "averagePrice": 0
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE971",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "iPad Pro 11 Case with Keyboard 2018-360 Rotatable - Wireless/BT - Backlit 17 Color - Auto Sleep Wake - Thin & Light - iPad Case with Keyboard?Support Apple Pencil 2nd Gen Charging?",
                    "sales": 0.0,
                    "marketId": 1,
                    "unitSales": 0,
                    "salesAmount": {
                        "currencyAmount": 0.0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0.00"
                    },
                    "price": 50.99,
                    "averagePriceAmount": {
                        "currencyAmount": 0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0"
                    },
                    "asin": "BGJ0000590",
                    "averagePrice": 0
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE37",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "iPad 8th Generation 2020 Case with Keyboard, 7 Color Backlit, 343 Mixed Mode, Detachable Keyboard Case for iPad 7th Gen, Thin & Light, Auto Sleep Wake, iPad 10.2/10.5 inch, iPad Air 3rd Gen, Sliver",
                    "sales": 56.06,
                    "marketId": 1,
                    "unitSales": 1,
                    "salesAmount": {
                        "currencyAmount": 56.06,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$56.06"
                    },
                    "price": 56.06,
                    "averagePriceAmount": {
                        "currencyAmount": 56.06,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$56.06"
                    },
                    "asin": "BGJ0000525",
                    "averagePrice": 56.06
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE1370",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "GreenLaw iPad Pro 11 2021 Case with Keyboard, 360° Rotatable, 3-Zone 7 Color Backlight Keyboard Case for iPad Air 4th Generation, iPad Pro 11 inch 3rd/ 2nd/ 1st Generation, Tiffany Blue",
                    "sales": 113.88,
                    "marketId": 1,
                    "unitSales": 2,
                    "salesAmount": {
                        "currencyAmount": 113.88,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$113.88"
                    },
                    "price": 56.94,
                    "averagePriceAmount": {
                        "currencyAmount": 56.94,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$56.94"
                    },
                    "asin": "BGJ0000566",
                    "averagePrice": 56.94
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE810",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "GreenLaw iPad Pro 11 inch 2020/2018 Case with Keyboard - 360° Rotatable-17 Backlit Color-Support Wake/Sleep-Wireless Keyboard Case for iPad Pro 11 2nd/ 1st Generation, Papaya",
                    "sales": 967.98,
                    "marketId": 1,
                    "unitSales": 17,
                    "salesAmount": {
                        "currencyAmount": 967.98,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$967.98"
                    },
                    "price": 56.94,
                    "averagePriceAmount": {
                        "currencyAmount": 56.94,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$56.94"
                    },
                    "asin": "BGJ0000385",
                    "averagePrice": 56.94
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE711",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "GreenLaw iPad Pro 11 2021 Case with Keyboard, 360° Rotatable, 3-Zone 7 Color Backlight Keyboard Case for iPad Air 4th Generation, iPad Pro 11 inch 3rd/ 2nd/ 1st Generation, Silver",
                    "sales": 1475.6,
                    "marketId": 1,
                    "unitSales": 31,
                    "salesAmount": {
                        "currencyAmount": 1475.6,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$1475.60"
                    },
                    "price": 47.6,
                    "averagePriceAmount": {
                        "currencyAmount": 47.6,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$47.60"
                    },
                    "asin": "BGJ0000578",
                    "averagePrice": 47.6
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE1452",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "GreenLaw iPad Pro 11 2021 Case with Keyboard, 360° Rotatable, 3-Zone 7 Color Backlight Keyboard Case for iPad Air 4th Generation, iPad Pro 11 inch 3rd/ 2nd/ 1st Generation, Black",
                    "sales": 7291.7,
                    "marketId": 1,
                    "unitSales": 130,
                    "salesAmount": {
                        "currencyAmount": 7291.7,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$7291.70"
                    },
                    "price": 56.09,
                    "averagePriceAmount": {
                        "currencyAmount": 56.09,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$56.09"
                    },
                    "asin": "BGJ0000565",
                    "averagePrice": 56.09
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE579",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "GreenLaw iPad Pro 11 2021 Case with Keyboard, 360° Rotatable, 3-Zone 7 Color Backlight Keyboard Case for iPad Air 4th Generation, iPad Pro 11 inch 3rd/ 2nd/ 1st Generation, Rose Gold",
                    "sales": 1822.08,
                    "marketId": 1,
                    "unitSales": 32,
                    "salesAmount": {
                        "currencyAmount": 1822.08,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$1822.08"
                    },
                    "price": 56.94,
                    "averagePriceAmount": {
                        "currencyAmount": 56.94,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$56.94"
                    },
                    "asin": "BGJ0000818",
                    "averagePrice": 56.94
                },
                {
                    "image": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                    "msku": "TEST_MSKU_GJ ERP-QWE1040",
                    "dealId": "fc42927e29ce3775968240359cad8c2ca1efd21c",
                    "title": "iPad Pro 11 Case with Keyboard 2020/2018 (1st/ 2nd Generation) - 360 Rotatable - Wireless/BT - Backlit 17 Color - Auto Sleep Wake - Support Apple Pencil 2nd Gen Charging, Gray Black",
                    "sales": 0.0,
                    "marketId": 1,
                    "unitSales": 0,
                    "salesAmount": {
                        "currencyAmount": 0.0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0.00"
                    },
                    "price": 54.39,
                    "averagePriceAmount": {
                        "currencyAmount": 0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0"
                    },
                    "asin": "BGJ0000502",
                    "averagePrice": 0
                }
            ],
            "internalDescription": "Deals-2021/06/04 7-37-23-136",
            "marketName": "一号店--有广告数据:US",
            "latestSyncTime": "2021-11-12 07:00:05",
            "startDate": "2021-08-02 00:00:00",
            "status": "ENDED"
        }
    ],
    "extObj": 137
}
```

---

## 35. 优惠券

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 优惠券 |
| 请求地址 | `/operation/ads/coupon/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据更新开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据更新结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 数据开始时间 [yyyy-MM-dd] |
| endDataDate | date | 否 | 数据结束时间 [yyyy-MM-dd] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | array<object> | 是 | 接口返回数据 |
| extObj | long | 是 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "marketId": 1,
    "count": 1,
    "startDate":"2016-01-15",
    "endDate":"2023-05-17"
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": [
        {
            "endDate": "2021-09-16 00:00:00",
            "clips": 43,
            "discount": 5.0,
            "discountAmount": {
                "currencyAmount": 5.0,
                "currencySymbol": "$",
                "currencyCode": "USD",
                "amountWithSymbol": "$5.00"
            },
            "couponId": "3f6206aa-8c51-4af2-8d5c-a52f9017af52",
            "feeRate": 6.0,
            "sales": 572.76,
            "marketId": 1,
            "firstSyncTime": "2021-07-19 03:38:04",
            "exchangeRate": 21.0,
            "salesAmount": {
                "currencyAmount": 572.76,
                "currencySymbol": "$",
                "currencyCode": "USD",
                "amountWithSymbol": "$572.76"
            },
            "spend": 35.55,
            "discountType": "percent",
            "id": "1043",
            "budget": 3000.0,
            "failedAsinCount": "-",
            "internalDescription": "Save 5% on K960RG",
            "marketName": "一号店--有广告数据:US",
            "budgetAmount": {
                "currencyAmount": 3000.0,
                "currencySymbol": "$",
                "currencyCode": "USD",
                "amountWithSymbol": "$3000.00"
            },
            "redemptions": 9,
            "spendAmount": {
                "currencyAmount": 35.55,
                "currencySymbol": "$",
                "currencyCode": "USD",
                "amountWithSymbol": "$35.55"
            },
            "latestSyncTime": "2021-11-19 03:29:25",
            "startDate": "2021-06-22 00:00:00",
            "status": "Canceled"
        }
    ],
    "extObj": 1043
}
```

---

## 36. 查询管理促销列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询管理促销列表 |
| 请求地址 | `/operation/ads/openManagePromotion/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据更新开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据更新结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 数据开始时间 [yyyy-MM-dd] |
| endDataDate | date | 否 | 数据结束时间 [yyyy-MM-dd] |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | array<object> | 是 | 接口返回数据 |
| extObj | long | 是 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "marketId": 4,
    "count": 10,
    "startDataDate":"2016-01-15",
    "endDataDate":"2023-05-17"
}
```

### 响应示例

```json
{
    "traceId": "open_ab8b654faed944e59793773b1337f340",
    "code": 200,
    "data": [
        {
            "needBuyerItem": "86W+拉花笔购买折扣",
            "detailsPageDisplay": "True",
            "managePromotionType": "PURCHASE_DISCOUNT",
            "endDate": "2022-08-25 23:59:00",
            "claimCodeType": "Preferential",
            "managePromotionId": "A1F2XWARXVCLFW",
            "marketingPageLink": "",
            "sales": 0.0,
            "marketId": 4,
            "unitSales": 0,
            "firstSyncTime": "2022-07-18 02:03:48",
            "salesAmount": {
                "currencyAmount": 0.0,
                "currencySymbol": "$",
                "currencyCode": "USD",
                "amountWithSymbol": "$0.00"
            },
            "participateConditionType": "At least this quantity of items",
            "participateCondition": "1",
            "id": "1",
            "discountedItem": "BGJ0000582",
            "timeReminder": "",
            "redemptionRestrictions": "Yes",
            "trackingId": "购买折扣 2022/03/21 6-1-30-452",
            "discountedItemType": "Additional Item",
            "buyerGetDeals": "购买数量：1 50%OFF(5折)",
            "internalDescription": "86W+拉花笔套装10号五折",
            "marketName": "积加测试店铺2:US",
            "adsOpenManagePromotionGoodsVOList": [
                {
                    "msku": "TEST_MSKU_GJ ERP-QWE480",
                    "avgManagePromotionFee": 10.0,
                    "managePromotionId": "A1F2XWARXVCLFW",
                    "title": "100% Kolinsky Sable Nail Brush, Larbois Acrylic Nail Art Brushes Set, Professional Application Lines Dotting Painting Drawing for Home and Salon Use Tools, 3 Pcs (# Size 10)",
                    "sales": 0.0,
                    "marketId": 4,
                    "unitSales": 0,
                    "avgManagePromotionFeeAmount": {
                        "currencyAmount": 10.0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$10.00"
                    },
                    "salesAmount": {
                        "currencyAmount": 0.0,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$0.00"
                    },
                    "price": 24.99,
                    "discountFlag": 2,
                    "asin": "BGJ0000582",
                    "priceAmount": {
                        "currencyAmount": 24.99,
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "amountWithSymbol": "$24.99"
                    }
                }
            ],
            "claimCode": "一次性",
            "latestSyncTime": "2022-07-23 17:03:48",
            "startDate": "2022-07-25 04:00:00",
            "status": "Active"
        }
    ],
    "extObj": 1,
    "messages": []
}
```

---

## 37. 查询会员折扣列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询会员折扣列表 |
| 请求地址 | `/operation/ads/openPrimeDiscount/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间范围 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| count | int | 是 | 查询条数 [最多100条] |
| nextId | long | 否 | 下次查询ID |
| startDate | date | 否 | 数据更新开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 数据更新结束时间 [yyyy-MM-dd] |
| startDataDate | date | 否 | 数据开始时间 [yyyy-MM-dd] |
| endDataDate | date | 否 | 数据结束时间 [yyyy-MM-dd] |
| marketId | int | 是 | 必传一种时间范围 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | array<object> | 是 | 接口返回数据 |
| extObj | int | 是 | 返回扩展对象 [最后一个id，查下一页的的入参] |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "marketId": 4,
    "count": 1,
    "startDataDate":"2016-01-15",
    "endDataDate":"2023-05-17"
}
```

### 响应示例

```json
{
    "traceId": "open_f8dbf203b44d4f91a48a432e9ff1d9b1",
    "code": 200,
    "data": [
        {
            "id": "1",
            "marketId": 91,
            "marketName": "*****",
            "internalDescription": "test prime",
            "status": "Awaiting",
            "startDate": null,
            "endDate": null,
            "productNum": 1,
            "primeId": "a1",
            "lastMarketTime": "2022-04-08",
            "createTime": "2022-04-08 16:52:33",
            "updateTime": "2022-04-08 16:52:02",
            "formatTimeTip": null,
            "event": "true",
            "primeDay": "true",
            "eventName": "PrimeDay",
            "adsOpenPrimeDiscountGoodsVOList": [
                {
                    "marketId": 91,
                    "primeId": "a1",
                    "asin": "B08***P27H",
                    "msku": "Z-GT***1P-BK",
                    "discountType": "PERCENT_OFF",
                    "discountValue": 100,
                    "discountDesc": "100%OFF(0折)",
                    "discount": 0,
                    "discountAmount": {
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "currencyAmount": 0,
                        "amountWithSymbol": "$0"
                    },
                    "lowDiscount": 50,
                    "lowDiscountAmount": {
                        "currencySymbol": "$",
                        "currencyCode": "USD",
                        "currencyAmount": 50,
                        "amountWithSymbol": "$50.00"
                    },
                    "status": "Expired"
                }
            ]
        }
    ],
    "messages": []
}
```

---

## 38. 商品广告-投放(V3)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品广告-投放(V3) |
| 请求地址 | `/operation/ads/adsSpProductTargeting/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 必传一种时间参数 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| startDate | string | 否 | 查询开始时间yyyy-MM-dd （和数据时间至少传一个时间范围） |
| endDate | string | 否 | 查询结束时间yyyy-MM-dd（和数据时间至少传一个时间范围） |
| count | int | 是 | 查询条数（最多500条） |
| nextId | long | 否 | 下次查询ID |
| startDataDate | string | 否 | 数据开始时间：yyyy-MM-dd （和查询时间至少传一个时间范围） |
| endDataDate | string | 否 | 数据结束时间：yyyy-MM-dd（和查询时间至少传一个时间范围） |
| marketId | int | 是 | 店铺id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| extObj | long | 否 | 返回扩展对象（最后一个id，查下一页的的入参） |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "marketId": 1,
    "count": 1,
    "startDate":"2022-01-15",
    "endDate":"2023-05-17",
    "nextId": 0
}
```

### 响应示例

```json
{
    "traceId": "open_d76946cddc0948b290aabdcd981805cc",
    "code": 200,
    "data": [
        {
            "expressionValue": null,
            "adsSales": 0,
            "otherProductSales": null,
            "groupId": "17201201895656",
            "resolvedExpressionValue": "queryHighRelMatches",
            "marketId": 1,
            "adsProductOrders": 0,
            "cpa": null,
            "cpc": 0.76,
            "adsProductSales": 0,
            "roas": 0,
            "id": "1711",
            "portfolioName": "test",
            "cvr": 0,
            "createDate": "2023-03-23",
            "ctr": 0.12,
            "adsOrders": 0,
            "cost": 4.57,
            "expression": "[{\"type\":\"queryHighRelMatches\"}]",
            "resolvedExpression": null,
            "campaignId": 12103451826351,
            "impressions": 4882,
            "acos": null,
            "groupName": "test-自动",
            "portfolioId": "239321024231100",
            "clicks": 6,
            "campaignName": "test-自动"
        }
    ],
    "extObj": 1711,
    "messages": []
}
```

---

## 39. Feedback

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | Feedback |
| 请求地址 | `/operation/crm/feedback/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| recordStartDate | string | 否 | 记录开始时间 [yyyy-MM-dd] |
| recordEndDate | string | 否 | 记录结束时间 [yyyy-MM-dd] |
| results | array<int> | 否 | 跟踪结果 [0-无变化，1-无需处理，2-分数变化，3-已删除，4-邮件无回复] |
| states | array<int> | 否 | Feedback状态 [0-未处理，1-处理中，2-已完成] |
| feedbackStartDate | string | 否 | 评论开始时间 [yyyy-MM-dd] |
| feedbackEndDate | string | 否 | 评论结束时间 [yyyy-MM-dd] |
| marketIds | array<long> | 否 | 站点id集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
	"page": 1,
	"pagesize": 10

}
```

### 响应示例

```json
{
    "traceId": "open_70dbde60ea4b41d7a69be61c168ffa0e",
    "code": 200,
    "data": {
        "total": 7935,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "updateDate": "2023-03-04",
                "orderId": "113-0316156-3773027",
                "responseText": null,
                "tagIds": [
                    "1",
                    "2"
                ],
                "rating": 3,
                "feedbackDate": "2022-12-29 23:54:26",
                "feedbackId": "A8I1TL01WC78Q9",
                "cause": "0",
                "raterRole": "BuyerRatesSeller",
                "tagNames": [
                    "无法连接",
                    "按键问题"
                ],
                "responseDate": null,
                "marketId": 5,
                "result": 0,
                "starFinal": 0,
                "responseSuppressed": false,
                "tagEchoVOList": [
                    {
                        "tagId": 2,
                        "tagName": "无法连接",
                        "tagMemo": null
                    },
                    {
                        "tagId": 1,
                        "tagName": "按键问题",
                        "tagMemo": null
                    }
                ],
                "recordDate": "2023-10-04",
                "id": 7935,
                "suppressed": false,
                "state": 0,
                "unBundingMarket": 0,
                "tagMemo": null,
                "listingDetailList": null,
                "comments": "12-28测试数据",
                "feedDate": "2022-12-28 23:54:26",
                "suppressReasonId": null,
                "raterEmail": "",
                "removalResponse": null,
                "asin": null,
                "responseId": ""
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 40. Review

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | Review |
| 请求地址 | `/operation/crm/review/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| reviewIds | array<string> | 否 | 评论编号 |
| createDateBegin | date | 否 | 记录开始时间 [yyyy-MM-dd HH:mm:ss] |
| createDateEnd | date | 否 | 记录结束时间 [yyyy-MM-dd HH:mm:ss] |
| updateDateBegin | datetime | 否 | 更新开始时间 [yyyy-MM-dd HH:mm:ss] |
| updateDateEnd | datetime | 否 | 更新结束时间 [yyyy-MM-dd HH:mm:ss] |
| reviewDateBegin | date | 否 | 评论开始时间 [yyyy-MM-dd] |
| reviewDateEnd | date | 否 | 评论结束时间 [yyyy-MM-dd] |
| marketIds | array<long> | 否 | 站点id集合 |
| states | array<long> | 否 | Review状态 [0-未处理，1-处理中，2-已完成，3-无] |
| results | array<long> | 否 | 跟踪结果 [0-无，1-无变化-客户不同意，3-已删除，4-无变化-邮件无回复，5-分数变化-调高，6-分数变化-调低] |
| orderIds | array<string> | 否 | 订单编号 |
| nameMatchType | string | 否 | 匹配方式 [fuzzyMatch-模糊匹配，exact-精准匹配，contactBuyer-亚马逊，handAdd-手动发送] |
| asins | array<string> | 否 | asin集合 |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 返回的提示信息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20
}
```

### 响应示例

```json
{
    "traceId": "open_6d51ba54bc8f47729215df5891521493",
    "code": 200,
    "data": {
        "total": 21440,
        "pagesize": 20,
        "page": 1,
        "rows": [
            {
                "reviewMatchOrders": null,
                "handSend": false,
                "orderId": null,
                "buyerEmail": null,
                "userInfoTags": null,
                "memo": "",
                "productName": "",
                "userProfileUrl": "https://www.amazon.de/gp/profile/amzn1.account.AFBRJWM4XP74UP5EYQ6Y37ANMNGA/ref=cm_cr_srp_d_gw_btm?ie=UTF8",
                "reviewUrl": "https://www.amazon.de/review/R1X9M511OUHI50/ref=cm_cr_dp_title?ie=UTF8&ASIN=B09K575J77&channel=detail-glance&store=wireless",
                "doneOrderId": "",
                "tagEchoVOList": [],
                "id": 21723,
                "state": 3,
                "unBundingMarket": 0,
                "uname": " Penzkofer",
                "listingTitle": "",
                "isHandSend": false,
                "stateChange": 0,
                "bogusOrder": false,
                "storeTotal": 1,
                "countryName": "DE",
                "evaluationReview": false,
                "updateDate": "2023-03-24 04:51",
                "purchaseDate": null,
                "productImgUrl": "",
                "onSaleStore": [
                    "一号店1"
                ],
                "tagIds": null,
                "doneEnable": null,
                "cause": null,
                "sellingManagerName": null,
                "title": "Top",
                "categoryName": "",
                "countryId": 4,
                "content": "Genau das, was ich erwartet habe.👍",
                "tagNames": null,
                "marketId": 13,
                "result": 0,
                "uid": "amzn1.account.AFBRJWM4XP74UP5EYQ6Y37ANMNGA",
                "starFinal": 5,
                "nameMatchType": null,
                "reviewDate": "2023-03-16",
                "pendCount": 0,
                "haltStore": [],
                "existImage": 0,
                "tagMemo": null,
                "emailCount": 0,
                "product": "",
                "star": 5,
                "reviewMedia": null,
                "verified": 1,
                "matchCount": 0,
                "asinUrl": "https://www.amazon.de/gp/product/B09K575J77",
                "existVideo": 0,
                "reviewChange": 0,
                "createTime": "2023-03-24 04:51:40",
                "helpfulNum": 0,
                "fasin": "",
                "asin": "B09K575J77",
                "category": null,
                "reviewId": "R1X9M511OUHI50"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 41. 买家之声列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 买家之声列表 |
| 请求地址 | `/operation/crm/customerVoice/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| marketIds | array<int> | 否 | 站点id集合 |
| productName | string | 否 | 产品名称, 模糊查询 |
| skus | array<string> | 否 | sku集合 |
| mskus | array<string> | 否 | msku集合 |
| asins | array<string> | 否 | asin集合 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| pcxHealth | string | 否 | 状态 [Good-良好，Excellent-优秀，Fair-一般，Poor-不佳，Verypoor-极差] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_e687fdc291a24e378cd91482f5b8d423",
    "code": 200,
    "data": {
        "total": 5,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "id": 1,
                "marketId": 1,
                "marketName": "test:US",
                "imageUrl": "https://m.media-amazon.com/images/I/51Un-iEaXUL._SL75_.jpg",
                "itemName": "****",
                "asin": "****",
                "retailUrl": "*****",
                "msku": "test",
                "itemCondition": "New",
                "sku": "test",
                "productName": "test",
                "categoryName": "test",
                "fnsku": "test",
                "fulfillmentChannel": "FBA",
                "ncxRate": 0,
                "ncxCount": 0,
                "orderCount": 4,
                "pcxHealth": "EXCELLENT",
                "lastUpdate": "2024-01-20",
                "mostCommonReturnReasonBucket": "",
                "mostCommonReturnReasonBucketPercent": null,
                "mostCommonReturnReasonBucketCount": null,
                "returnComments": [
                    {
                        "orderId": "114-3557538-9002628",
                        "memo": "Saxophone reeds",
                        "returnTime": "2023-12-29 16:23:33"
                    },
                    {
                        "orderId": "114-8702449-1860261",
                        "memo": "Needed a different size",
                        "returnTime": "2023-12-20 03:48:37"
                    }
                ],
                "createTime": "2024-01-18 22:22:50",
                "updateTime": "2024-01-22 06:11:29"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 42. 查询标签管理信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询标签管理信息 |
| 请求地址 | `/operation/crm/tags/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| messages | array<string> | 是 | 接口返回提示消息 |
| data | array<object> | 是 | 接口返回数据 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
-
```

### 响应示例

```json
{
    "traceId": "open_72da90c69a5047caa8864d27f82b0f6c",
    "code": 200,
    "data": [
        {
            "pincode": "pjqs",
            "code": "01",
            "createTime": "2021-12-27 16:05:15",
            "childrens": [
                {
                    "fid": 7,
                    "pincode": "lsbqs",
                    "code": "001",
                    "createTime": "2022-03-28 13:37:11",
                    "childrens": [
                        {
                            "fid": 12,
                            "pincode": "csd",
                            "code": "dscv",
                            "createTime": "2022-05-27 18:29:04",
                            "childrens": [],
                            "name": "csddf",
                            "memo": null,
                            "updateTime": "2022-05-27 18:29:04",
                            "id": 19,
                            "state": "Active",
                            "userName": "倍思"
                        }
                    ],
                    "name": "螺丝包缺失",
                    "memo": null,
                    "updateTime": "2022-03-28 13:37:11",
                    "id": 12,
                    "state": "Active",
                    "userName": "天熙科技"
                },
                {
                    "fid": 7,
                    "pincode": "wxjqs",
                    "code": "002",
                    "createTime": "2022-03-28 13:37:33",
                    "childrens": [],
                    "name": "五星脚缺失",
                    "memo": null,
                    "updateTime": "2022-03-28 13:37:33",
                    "id": 13,
                    "state": "Active",
                    "userName": "天熙科技"
                },
                {
                    "fid": 7,
                    "pincode": "tzqs",
                    "code": "003",
                    "createTime": "2022-03-28 13:37:53",
                    "childrens": [],
                    "name": "头枕缺失",
                    "memo": null,
                    "updateTime": "2022-03-28 13:37:53",
                    "id": 14,
                    "state": "Active",
                    "userName": "天熙科技"
                }
            ],
            "name": "配件缺失",
            "memo": null,
            "updateTime": "2021-12-27 16:05:15",
            "id": 7,
            "state": "Active",
            "userName": ""
        }
    ],
    "messages": []
}
```

---

## 43. 查询财务利润分析V2

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询财务利润分析V2 |
| 请求地址 | `/finance/sts/financialAnalysis/page/V2` |
| 请求方式 | POST |
| 限流规则 | 每 10秒 1次 |
| 接口说明 | 默认排序 alesAmount desc |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| costValues | int | 是 | 成本取值 [0-先进先出，1-月末平均，2-自定义成本] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| currency | string | 是 | 币种 [参考Q&A-通用参数-币种] |
| dateType | int | 是 | 时间类型 [0-按开始日期与结束日期，1-按月份] |
| monthDate | string | 否 | 月份 [yyyy-MM] |
| startDate | date | 否 | 开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 结束时间 [yyyy-MM-dd] |
| marketIds | array<int> | 否 | 站点ID集合 |
| categoryIds | array<string> | 否 | 品类编码集合 |
| brands | array<string> | 否 | 品牌编码集合 |
| decimalPlaces | int | 否 | 保留小数位 2 --8位 |
| footerExpandDetails | boolean | 否 | 店铺特有数据是否返回详情 |
| queryType | string | 是 | 查询类型 [market，category，father_asin，asin，spu，sku，msku] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | messages |
| array<string> | 是 | 否 | traceId |
| string | 是 | 否 |  |

### 请求示例

```json
{
    "queryType": "asin",
    "costValues": 2,
    "dateType": 1,
    "page": 1,
    "pagesize": 20,
    "currency": "YUAN",
    "monthDate": "2022-05"
}
```

### 响应示例

```json
{
    "traceId": "open_58dd664e738349469a9e4a7920b8a42f",
    "code": 200,
    "data": {
        "total": 1543,
        "footer": [
            {
                "otherCost": 0.0,
                "compensateAdjustAmount": 0,
                "productPatch": 0,
                "vineEvaluationFee": 0.0,
                "refundOtherTransactionFee": 0.0,
                "fbaSalesMoney": 0.0,
                "tcsSgst": 0.0,
                "productManagerAccount": null,
                "giftWrappingTax": 0.0,
                "otherTransactionFees": 0.0,
                "refundPromotionDiscountTax": 0.0,
                "exchangeAmount": 0,
                "monthStorageFee": 0.0,
                "productName": null,
                "standardDate": null,
                "fbaSalesAmount": 0,
                "refundSonOther": 0.0,
                "fbaCarrierFees": 0.0,
                "sku": null,
                "buyerShippingTax": 0.0,
                "brand": null,
                "gradeAndResellFee": 0.0,
                "managerFee": 0.0,
                "salesCommission": 0.0,
                "currentSellingManagerId": null,
                "noSaleableReturnAmount": 0,
                "inventoryRemovalFee": 0.0,
                "orderRetroCharge": 0.0,
                "preProcessingFee": 0.0,
                "saleableReturnAmount": 0,
                "sbFee": 0.0,
                "variantSituation": null,
                "refundTcsigst": 0.0,
                "otherPlatformFees": 0.0,
                "spuName": null,
                "deal": 0.0,
                "internationalFreightAdjustment": 0.0,
                "subscriptionFee": 0.0,
                "markupSalesCommission": 0.0,
                "listingLevel": null,
                "promotionCommissionCost": 0.0,
                "sellingManagerName": null,
                "marketWithholdingTax": 0.0,
                "fbaDeliveryFee": 0.0,
                "refundFbaDeliveryFee": 0.0,
                "promotionDiscount": 0.0,
                "internationalFreightTax": 0.0,
                "tbybSales": 0.0,
                "integral": 0.0,
                "liquidationAdjustSales": 0.0,
                "promotionPrincipalCost": 0.0,
                "currency": "USD",
                "refundAmount": 58,
                "fbmSellerShipping": 0.0,
                "refundGiftWrappingTax": 0.0,
                "spFee": 0.0,
                "refundPromotionDiscount": 0.0,
                "coupon": 0.0,
                "refundRetroCharge": 0.0,
                "liquidationAdjustAmount": 0,
                "currencySymbol": "$",
                "unplannedServiceFee": 0.0,
                "refundTcscgst": 0.0,
                "adjustmentFee": 0.0,
                "amazonMultichannelOtherCost": 0.0,
                "amazonPatchOtherCost": 0.0,
                "giftWrapping": 0.0,
                "liquidationAmount": 0,
                "buyerShipping": 0.0,
                "salesMoney": 0.0,
                "compensate": 0.0,
                "promotionDiscountTax": 0.0,
                "tcsCgst": 0.0,
                "addTax": 0.0,
                "refundTcssgst": 0.0,
                "lossRateAmount": 0.0,
                "refundGiftWrapping": 0.0,
                "putawayDate": null,
                "refundBuyerShippingTax": 0.0,
                "promotionCost": 0.0,
                "liquidationTax": 0.0,
                "consolidationFee": 0.0,
                "returnProcessingFee": 0.0,
                "refundCommodityPriceTax": 0.0,
                "atozComplaintFee": 0.0,
                "refundPrincipal": 0.0,
                "returnAmount": 0,
                "excessStorageFee": 0.0,
                "msku": null,
                "refundBuyerShipping": 0.0,
                "firstSalesDate": null,
                "refundIntegral": 0.0,
                "listingTitle": null,
                "earlyReviewerProgram": 0.0,
                "liquidationSales": 0.0,
                "longStorageFee": 0.0,
                "month": null,
                "compensateAdjust": 0.0,
                "liquidationFee": 0.0,
                "name": "站点维度特有数据",
                "spu": null,
                "tcsIgst": 0.0,
                "refundMarketWithholdingTax": 0.0,
                "alesAmount": 0,
                "amazonWithheldTax": 0.0,
                "currentSellingManagerName": null,
                "advertisingSpend": 0.0,
                "internationalFreight": 0.0,
                "marketId": null,
                "commodityPriceTax": 0.0,
                "productMultichannel": 0,
                "fatherAsin": null,
                "differenceFee": 0.0,
                "otherStorage": 0.0,
                "sellingManagerId": null,
                "imgUrl": null,
                "fbmSalesMoney": 0.0,
                "sdFee": 0.0,
                "fbmSalesAmount": 0,
                "promotionOtherFeeSon": 0.0,
                "asin": null,
                "removeAmount": 0,
                "category": null,
                "categoryId": null,
                "listingState": null,
                "compensateAmount": 0,
                "productManagerAccountId": null
            },
            {
                "otherCost": 0.0,
                "compensateAdjustAmount": 0,
                "productPatch": 0,
                "vineEvaluationFee": 0.0,
                "refundOtherTransactionFee": 0.0,
                "fbaSalesMoney": 0.0,
                "tcsSgst": 0.0,
                "productManagerAccount": null,
                "giftWrappingTax": 0.0,
                "otherTransactionFees": 0.0,
                "refundPromotionDiscountTax": 0.0,
                "exchangeAmount": 0,
                "monthStorageFee": 0.0,
                "productName": null,
                "standardDate": null,
                "fbaSalesAmount": 0,
                "refundSonOther": 0.0,
                "fbaCarrierFees": 0.0,
                "sku": null,
                "buyerShippingTax": 0.0,
                "brand": null,
                "gradeAndResellFee": 0.0,
                "managerFee": 0.0,
                "salesCommission": 0.0,
                "currentSellingManagerId": null,
                "noSaleableReturnAmount": 0,
                "inventoryRemovalFee": -1.05,
                "orderRetroCharge": 0.0,
                "preProcessingFee": 0.0,
                "saleableReturnAmount": 0,
                "sbFee": 0.0,
                "variantSituation": null,
                "refundTcsigst": 0.0,
                "otherPlatformFees": 0.0,
                "spuName": null,
                "deal": 0.0,
                "internationalFreightAdjustment": 0.0,
                "subscriptionFee": 0.0,
                "markupSalesCommission": 0.0,
                "listingLevel": null,
                "promotionCommissionCost": 0.0,
                "sellingManagerName": null,
                "marketWithholdingTax": 0.0,
                "fbaDeliveryFee": 0.0,
                "refundFbaDeliveryFee": 0.0,
                "promotionDiscount": 0.0,
                "internationalFreightTax": 0.0,
                "tbybSales": 0.0,
                "integral": 0.0,
                "liquidationAdjustSales": 0.0,
                "promotionPrincipalCost": 0.0,
                "currency": "USD",
                "refundAmount": 0,
                "fbmSellerShipping": 0.0,
                "refundGiftWrappingTax": 0.0,
                "spFee": 0.0,
                "refundPromotionDiscount": 0.0,
                "coupon": -88.54,
                "refundRetroCharge": 0.0,
                "liquidationAdjustAmount": 0,
                "currencySymbol": "$",
                "unplannedServiceFee": 0.0,
                "refundTcscgst": 0.0,
                "adjustmentFee": 0.0,
                "amazonMultichannelOtherCost": 0.0,
                "amazonPatchOtherCost": 0.0,
                "giftWrapping": 0.0,
                "liquidationAmount": 0,
                "buyerShipping": 0.0,
                "salesMoney": 0.0,
                "compensate": 0.0,
                "promotionDiscountTax": 0.0,
                "tcsCgst": 0.0,
                "addTax": 0.0,
                "refundTcssgst": 0.0,
                "lossRateAmount": 0.0,
                "refundGiftWrapping": 0.0,
                "putawayDate": null,
                "refundBuyerShippingTax": 0.0,
                "promotionCost": 0.0,
                "liquidationTax": 0.0,
                "consolidationFee": 0.0,
                "returnProcessingFee": 0.0,
                "refundCommodityPriceTax": 0.0,
                "atozComplaintFee": 0.0,
                "refundPrincipal": 0.0,
                "returnAmount": 0,
                "excessStorageFee": 0.0,
                "msku": null,
                "refundBuyerShipping": 0.0,
                "firstSalesDate": null,
                "refundIntegral": 0.0,
                "listingTitle": null,
                "earlyReviewerProgram": 0.0,
                "liquidationSales": 0.0,
                "longStorageFee": -0.05,
                "month": null,
                "compensateAdjust": 0.0,
                "liquidationFee": 0.0,
                "name": "分摊异常数据",
                "spu": null,
                "tcsIgst": 0.0,
                "refundMarketWithholdingTax": 0.0,
                "alesAmount": 0,
                "amazonWithheldTax": 0.0,
                "currentSellingManagerName": null,
                "advertisingSpend": 0.0,
                "internationalFreight": 0.0,
                "marketId": null,
                "commodityPriceTax": 0.0,
                "productMultichannel": 0,
                "fatherAsin": null,
                "differenceFee": 0.0,
                "otherStorage": 0.0,
                "sellingManagerId": null,
                "imgUrl": null,
                "fbmSalesMoney": 0.0,
                "sdFee": 0.0,
                "fbmSalesAmount": 0,
                "promotionOtherFeeSon": 0.01,
                "asin": null,
                "removeAmount": 0,
                "category": null,
                "categoryId": null,
                "listingState": null,
                "compensateAmount": 0,
                "productManagerAccountId": null
            },
            {
                "otherCost": 0.0,
                "compensateAdjustAmount": 0,
                "productPatch": 0,
                "vineEvaluationFee": 0.0,
                "refundOtherTransactionFee": 0.0,
                "fbaSalesMoney": 0.0,
                "tcsSgst": 0.0,
                "productManagerAccount": null,
                "giftWrappingTax": 0.0,
                "otherTransactionFees": 0.0,
                "refundPromotionDiscountTax": 0.0,
                "exchangeAmount": 0,
                "monthStorageFee": -30140.95,
                "productName": null,
                "standardDate": null,
                "fbaSalesAmount": 0,
                "refundSonOther": 0.0,
                "fbaCarrierFees": 0.0,
                "sku": null,
                "buyerShippingTax": 0.0,
                "brand": null,
                "gradeAndResellFee": 0.0,
                "managerFee": 0.0,
                "salesCommission": 0.0,
                "currentSellingManagerId": null,
                "noSaleableReturnAmount": 0,
                "inventoryRemovalFee": -8221.41,
                "orderRetroCharge": 0.0,
                "preProcessingFee": 0.0,
                "saleableReturnAmount": 0,
                "sbFee": 0.0,
                "variantSituation": null,
                "refundTcsigst": 0.0,
                "otherPlatformFees": 0.0,
                "spuName": null,
                "deal": -12600.0,
                "internationalFreightAdjustment": 0.0,
                "subscriptionFee": -984.12,
                "markupSalesCommission": 0.0,
                "listingLevel": null,
                "promotionCommissionCost": 0.0,
                "sellingManagerName": null,
                "marketWithholdingTax": 0.0,
                "fbaDeliveryFee": 0.0,
                "refundFbaDeliveryFee": 0.0,
                "promotionDiscount": 0.0,
                "internationalFreightTax": 0.0,
                "tbybSales": 0.0,
                "integral": 0.0,
                "liquidationAdjustSales": 0.0,
                "promotionPrincipalCost": 0.0,
                "currency": "USD",
                "refundAmount": 0,
                "fbmSellerShipping": 0.0,
                "refundGiftWrappingTax": 0.0,
                "spFee": 0.0,
                "refundPromotionDiscount": 0.0,
                "coupon": -13130.4,
                "refundRetroCharge": 0.0,
                "liquidationAdjustAmount": 0,
                "currencySymbol": "$",
                "unplannedServiceFee": 0.0,
                "refundTcscgst": 0.0,
                "adjustmentFee": 0.0,
                "amazonMultichannelOtherCost": 0.0,
                "amazonPatchOtherCost": 0.0,
                "giftWrapping": 0.0,
                "liquidationAmount": 0,
                "buyerShipping": 0.0,
                "salesMoney": 0.0,
                "compensate": 0.0,
                "promotionDiscountTax": 0.0,
                "tcsCgst": 0.0,
                "addTax": 0.0,
                "refundTcssgst": 0.0,
                "lossRateAmount": 0.0,
                "refundGiftWrapping": 0.0,
                "putawayDate": null,
                "refundBuyerShippingTax": 0.0,
                "promotionCost": 0.0,
                "liquidationTax": 0.0,
                "consolidationFee": 0.0,
                "returnProcessingFee": 0.0,
                "refundCommodityPriceTax": 0.0,
                "atozComplaintFee": 0.0,
                "refundPrincipal": 0.0,
                "returnAmount": 0,
                "excessStorageFee": -14450.59,
                "msku": null,
                "refundBuyerShipping": 0.0,
                "firstSalesDate": null,
                "refundIntegral": 0.0,
                "listingTitle": null,
                "earlyReviewerProgram": 0.0,
                "liquidationSales": 0.0,
                "longStorageFee": -4348.81,
                "month": null,
                "compensateAdjust": 0.0,
                "liquidationFee": 0.0,
                "name": "未分摊数据",
                "spu": null,
                "tcsIgst": 0.0,
                "refundMarketWithholdingTax": 0.0,
                "alesAmount": 0,
                "amazonWithheldTax": 0.0,
                "currentSellingManagerName": null,
                "advertisingSpend": -182472.86,
                "internationalFreight": 0.0,
                "marketId": null,
                "commodityPriceTax": 0.0,
                "productMultichannel": 0,
                "fatherAsin": null,
                "differenceFee": 0.0,
                "otherStorage": 0.0,
                "sellingManagerId": null,
                "imgUrl": null,
                "fbmSalesMoney": 0.0,
                "sdFee": 0.0,
                "fbmSalesAmount": 0,
                "promotionOtherFeeSon": -200.0,
                "asin": null,
                "removeAmount": 0,
                "category": null,
                "categoryId": null,
                "listingState": null,
                "compensateAmount": 0,
                "productManagerAccountId": null
            }
        ],
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "otherCost": 0.0,
                "compensateAdjustAmount": 0,
                "productPatch": 0,
                "vineEvaluationFee": 0.0,
                "refundOtherTransactionFee": 0.0,
                "fbaSalesMoney": 0.0,
                "tcsSgst": 0.0,
                "productManagerAccount": "**",
                "giftWrappingTax": 0.0,
                "otherTransactionFees": 0.0,
                "refundPromotionDiscountTax": 0.0,
                "exchangeAmount": 0,
                "monthStorageFee": 0.0,
                "fbaSalesAmount": 0,
                "productName": "****************",
                "amazonPatchProductCost": 0.0,
                "refundSonOther": 0.0,
                "amazonMultichannelArriveCost": 0.0,
                "estimateActualPrice": 0.0,
                "fbaCarrierFees": 0.0,
                "buyerShippingTax": 0.0,
                "sku": "11-********-ND",
                "brand": "未匹配品牌",
                "gradeAndResellFee": 0.0,
                "managerFee": 0.0,
                "salesCommission": 0.0,
                "noSaleableReturnAmount": 0,
                "currentSellingManagerId": null,
                "inventoryRemovalFee": 0.0,
                "orderRetroCharge": 0.0,
                "preProcessingFee": 0.0,
                "saleableReturnAmount": 0,
                "sbFee": 0.0,
                "refundTcsigst": 0.0,
                "variantSituation": null,
                "otherPlatformFees": 0.0,
                "deal": 0.0,
                "internationalFreightAdjustment": 0.0,
                "spuName": "",
                "subscriptionFee": 0.0,
                "markupSalesCommission": 0.0,
                "aggregateData": {
                    "EFPCR23060200055": 0.0,
                    "EFPCR23060200110": 0.0,
                    "EFPCR23060200077": "0.0000",
                    "EFPCR23060200098": 0.0,
                    "EFPCR23060200076": 0.0,
                    "EFPCR23060200131": 0.0,
                    "EFPCR23060200035": 0.0,
                    "EFPCR23072002102": 0,
                    "EFPCR23060200056": "0.0000",
                    "EFPCR23060200078": "0.0000",
                    "alesAmount": 0,
                    "EFPCR23060200114": 0.0,
                    "EFPCR23072002067": 0,
                    "EFPCR23060200138": 0.0,
                    "EFPCR23060200091": 0.0,
                    "EFPCR23072100672": "0.0000",
                    "EFPCR23060200030": "0.0000",
                    "EFPCR23072001718": "0.0000",
                    "EFPCR23060200119": "0.0000",
                    "EFPCR23072500177": "0.0000",
                    "EFPCR23072500257": 0.0,
                    "returnAmount": 0,
                    "EFPCR23072001896": "0.0000",
                    "EFPCR23060200121": 0.0,
                    "EFPCR23060200021": 0.0,
                    "EFPCR23060200065": 0.0,
                    "EFPCR23060200043": "0.0000",
                    "EFPCR23060200120": 0.0,
                    "EFPCR23060200024": 0.0,
                    "EFPCR23060200046": 0.0,
                    "EFPCR23072001661": 0.0,
                    "EFPCR23060200122": "0.0000",
                    "EFPCR23060200125": 0.0,
                    "EFPCR23060200047": "0.0000",
                    "EFPCR23060200104": 0.0,
                    "EFPCR23060200049": 0.0,
                    "EFPCR23072100580": 0,
                    "EFPCR23072100245": 0,
                    "EFPCR23060200041": 0.0,
                    "EFPCR23072100408": 0,
                    "EFPCR23072001529": 0.0,
                    "EFPCR23060200029": "0.0000",
                    "EFPCR23072001903": "0.0000",
                    "salesMoney": 0.0,
                    "EFPCR23072001449": 0
                },
                "promotionCommissionCost": 0.0,
                "listingLevel": null,
                "sellingManagerName": null,
                "marketWithholdingTax": 0.0,
                "fbaDeliveryFee": 0.0,
                "refundFbaDeliveryFee": 0.0,
                "promotionDiscount": 0.0,
                "internationalFreightTax": 0.0,
                "tbybSales": 0.0,
                "integral": 0.0,
                "liquidationAdjustSales": 0.0,
                "promotionPrincipalCost": 0.0,
                "currency": "USD",
                "refundAmount": 0,
                "fbmSellerShipping": 0.0,
                "refundGiftWrappingTax": 0.0,
                "spFee": 0.0,
                "purchaseCost": 0.0,
                "refundPromotionDiscount": 0.0,
                "coupon": 0.0,
                "compensatePurchaseCosts": 0.0,
                "refundRetroCharge": 0.0,
                "liquidationAdjustAmount": 0,
                "unplannedServiceFee": 0.0,
                "currencySymbol": "$",
                "refundTcscgst": 0.0,
                "adjustmentFee": 0.0,
                "amazonMultichannelOtherCost": 0.0,
                "amazonPatchOtherCost": 0.0,
                "giftWrapping": 0.0,
                "liquidationAmount": 0,
                "buyerShipping": 0.0,
                "compensate": -11.31,
                "promotionDiscountTax": 0.0,
                "tcsCgst": 0.0,
                "addTax": 0.0,
                "refundTcssgst": 0.0,
                "lossRateAmount": 0.0,
                "refundGiftWrapping": 0.0,
                "compensateReturnCost": 0.0,
                "putawayDate": "2019-05-13 19:03:07",
                "refundBuyerShippingTax": 0.0,
                "promotionCost": 0.0,
                "liquidationTax": 0.0,
                "consolidationFee": 0.0,
                "returnProcessingFee": 0.0,
                "arrivalCost": 0.0,
                "refundCommodityPriceTax": 0.0,
                "atozComplaintFee": 0.0,
                "refundPrincipal": 0.0,
                "excessStorageFee": 0.0,
                "refundBuyerShipping": 0.0,
                "msku": "11-WCLHS02S85BM-ND",
                "refundIntegral": 0.0,
                "firstSalesDate": "2018-05-09",
                "listingTitle": "*****************************",
                "earlyReviewerProgram": 0.0,
                "liquidationSales": 0.0,
                "longStorageFee": 0.0,
                "amazonPatchArriveCost": 0.0,
                "compensateAdjust": 0.0,
                "liquidationFee": 0.0,
                "spu": "未匹配SPU",
                "tcsIgst": 0.0,
                "refundMarketWithholdingTax": 0.0,
                "amazonWithheldTax": 0.0,
                "currentSellingManagerName": null,
                "advertisingSpend": 0.0,
                "internationalFreight": 0.0,
                "commodityPriceTax": 0.0,
                "marketId": 9,
                "productMultichannel": 0,
                "fatherAsin": "*********",
                "differenceFee": 0.0,
                "otherStorage": 0.0,
                "sellingManagerId": null,
                "imgUrl": "https://m.media-amazon.com/imag************",
                "fbmSalesMoney": 0.0,
                "sdFee": 0.0,
                "fbmSalesAmount": 0,
                "amazonMultichannelProductCost": 0.0,
                "promotionOtherFeeSon": 0.0,
                "removeAmount": 0,
                "asin": "*********",
                "category": "11",
                "compensateAmount": -1,
                "listingState": null,
                "productManagerAccountId": 183
            }
        ]
    },
    "messages": []
}
```

---

## 44. 查询财务利润分析V2-自定义字段

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询财务利润分析V2-自定义字段 |
| 请求地址 | `/finance/sts/colData/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 3次 |
| 接口说明 | 获取财务利润分析V2接口中自定义字段含义 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| dimension | string | 是 | 查询类型 [market，category，father_asin，asin，spu，sku，msku] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | array<object> | 是 | 返回数据 |
| messages | array<string> | 是 | 提示信息 |
| traceId | string | 是 | 链路追踪id |

### 请求示例

```json
{
    "dimension": "msku"
}
```

### 响应示例

```json
{
    "traceId": "open_21711a48cb304900b8f65e8387d3b1c9",
    "code": 200,
    "data": [
        {
            "colName": "店铺:站点",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "marketName"
        },
        {
            "colName": "图片",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "imgUrl"
        },
        {
            "colName": "MSKU",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "msku"
        },
        {
            "colName": "产品名称/SKU",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "productName"
        },
        {
            "colName": "父ASIN/ASIN",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "fatherAsin"
        },
        {
            "colName": "SPU/SPU名称",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "spuName"
        },
        {
            "colName": "商品标题",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "listingTitle"
        },
        {
            "colName": "品类",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "category"
        },
        {
            "colName": "品牌",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "brand"
        },
        {
            "colName": "负责人",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "managerAccount"
        },
        {
            "colName": "商品运营情况",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "listingSituation"
        },
        {
            "colName": "上架时间",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "putawayDate"
        },
        {
            "colName": "开售时间",
            "colType": "TEXT",
            "regionName": "基础信息",
            "detailCols": [],
            "colCode": "firstSalesDate"
        },
        {
            "colName": "销量",
            "colType": "NUMBER",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "FBA销量",
                    "colType": "NUMBER",
                    "colCode": "fbaSalesAmount"
                },
                {
                    "colName": "FBM销量",
                    "colType": "NUMBER",
                    "colCode": "fbmSalesAmount"
                },
                {
                    "colName": "清算销量",
                    "colType": "NUMBER",
                    "colCode": "liquidationAmount"
                },
                {
                    "colName": "清算调整量",
                    "colType": "NUMBER",
                    "colCode": "liquidationAdjustAmount"
                },
                {
                    "colName": "多渠道销量",
                    "colType": "NUMBER",
                    "colCode": "productMultichannel"
                },
                {
                    "colName": "补单销量",
                    "colType": "NUMBER",
                    "colCode": "productPatch"
                },
                {
                    "colName": "赔偿量",
                    "colType": "NUMBER",
                    "colCode": "compensateAmount"
                },
                {
                    "colName": "赔偿调整量",
                    "colType": "NUMBER",
                    "colCode": "compensateAdjustAmount"
                },
                {
                    "colName": "换货量",
                    "colType": "NUMBER",
                    "colCode": "exchangeAmount"
                },
                {
                    "colName": "库存移除量",
                    "colType": "NUMBER",
                    "colCode": "removeAmount"
                }
            ],
            "colCode": "alesAmount"
        },
        {
            "colName": "销售额",
            "colType": "MONEY",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "FBA销售额",
                    "colType": "MONEY",
                    "colCode": "fbaSalesMoney"
                },
                {
                    "colName": "TBYB销售额",
                    "colType": "MONEY",
                    "colCode": "tbybSales"
                },
                {
                    "colName": "FBM销售额",
                    "colType": "MONEY",
                    "colCode": "fbmSalesMoney"
                },
                {
                    "colName": "促销折扣",
                    "colType": "MONEY",
                    "colCode": "promotionDiscount"
                },
                {
                    "colName": "买家运费",
                    "colType": "MONEY",
                    "colCode": "buyerShipping"
                },
                {
                    "colName": "礼品包装费",
                    "colType": "MONEY",
                    "colCode": "giftWrapping"
                }
            ],
            "colCode": "salesMoney"
        },
        {
            "colName": "清算收入",
            "colType": "MONEY",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "清算销售额",
                    "colType": "MONEY",
                    "colCode": "liquidationSales"
                },
                {
                    "colName": "清算调整销售额",
                    "colType": "MONEY",
                    "colCode": "liquidationAdjustSales"
                }
            ],
            "colCode": "EFPCR23060200021"
        },
        {
            "colName": "赔偿",
            "colType": "MONEY",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "赔偿收入",
                    "colType": "MONEY",
                    "colCode": "compensate"
                },
                {
                    "colName": "赔偿调整",
                    "colType": "MONEY",
                    "colCode": "compensateAdjust"
                }
            ],
            "colCode": "EFPCR23060200024"
        },
        {
            "colName": "退款量",
            "colType": "NUMBER",
            "regionName": "平台收入",
            "detailCols": [],
            "colCode": "refundAmount"
        },
        {
            "colName": "退货量",
            "colType": "NUMBER",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "可售退货量",
                    "colType": "NUMBER",
                    "colCode": "saleableReturnAmount"
                },
                {
                    "colName": "不可售退货量",
                    "colType": "NUMBER",
                    "colCode": "noSaleableReturnAmount"
                }
            ],
            "colCode": "returnAmount"
        },
        {
            "colName": "退款率",
            "colType": "PERCENT",
            "regionName": "平台收入",
            "detailCols": [],
            "colCode": "EFPCR23060200029"
        },
        {
            "colName": "退货率",
            "colType": "PERCENT",
            "regionName": "平台收入",
            "detailCols": [],
            "colCode": "EFPCR23060200030"
        },
        {
            "colName": "收入退款",
            "colType": "MONEY",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "退款本金",
                    "colType": "MONEY",
                    "colCode": "refundPrincipal"
                },
                {
                    "colName": "退款其他-买家运费",
                    "colType": "MONEY",
                    "colCode": "refundBuyerShipping"
                },
                {
                    "colName": "退款其他-礼品包装费",
                    "colType": "MONEY",
                    "colCode": "refundGiftWrapping"
                },
                {
                    "colName": "退款其他-促销折扣",
                    "colType": "MONEY",
                    "colCode": "refundPromotionDiscount"
                }
            ],
            "colCode": "EFPCR23060200035"
        },
        {
            "colName": "费用退款",
            "colType": "MONEY",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "退款佣金",
                    "colType": "MONEY",
                    "colCode": "markupSalesCommission"
                },
                {
                    "colName": "退款其他-FBA配送费",
                    "colType": "MONEY",
                    "colCode": "refundFbaDeliveryFee"
                },
                {
                    "colName": "退款其他-积分",
                    "colType": "MONEY",
                    "colCode": "refundIntegral"
                },
                {
                    "colName": "退款其他-其他交易费",
                    "colType": "MONEY",
                    "colCode": "refundOtherTransactionFee"
                },
                {
                    "colName": "退款其他-其他费用",
                    "colType": "MONEY",
                    "colCode": "refundSonOther"
                }
            ],
            "colCode": "EFPCR23060200041"
        },
        {
            "colName": "FBA销售额占比",
            "colType": "PERCENT",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "FBA销售额",
                    "colType": "MONEY",
                    "colCode": "fbaSalesMoney"
                },
                {
                    "colName": "销售额",
                    "colType": "MONEY",
                    "colCode": "salesMoney"
                }
            ],
            "colCode": "EFPCR23072100672"
        },
        {
            "colName": "含税销售额",
            "colType": "MONEY",
            "regionName": "平台收入",
            "detailCols": [
                {
                    "colName": "销售额",
                    "colType": "MONEY",
                    "colCode": "salesMoney"
                },
                {
                    "colName": "销售税",
                    "colType": "MONEY",
                    "colCode": "EFPCR23060200098"
                },
                {
                    "colName": "商品价格税",
                    "colType": "MONEY",
                    "colCode": "commodityPriceTax"
                },
                {
                    "colName": "促销折扣税",
                    "colType": "MONEY",
                    "colCode": "promotionDiscountTax"
                },
                {
                    "colName": "买家运费税",
                    "colType": "MONEY",
                    "colCode": "buyerShippingTax"
                },
                {
                    "colName": "礼品包装税费",
                    "colType": "MONEY",
                    "colCode": "giftWrappingTax"
                },
                {
                    "colName": "市场预扣税",
                    "colType": "MONEY",
                    "colCode": "marketWithholdingTax"
                },
                {
                    "colName": "清算市场预扣税",
                    "colType": "MONEY",
                    "colCode": "liquidationTax"
                },
                {
                    "colName": "增值税",
                    "colType": "MONEY",
                    "colCode": "EFPCR23060200104"
                },
                {
                    "colName": "TCS-CGST",
                    "colType": "MONEY",
                    "colCode": "tcsCgst"
                },
                {
                    "colName": "TCS-SGST",
                    "colType": "MONEY",
                    "colCode": "tcsSgst"
                },
                {
                    "colName": "TCS-IGST",
                    "colType": "MONEY",
                    "colCode": "tcsIgst"
                },
                {
                    "colName": "增值税收",
                    "colType": "MONEY",
                    "colCode": "addTax"
                }
            ],
            "colCode": "EFPCR23072500257"
        },
        {
            "colName": "销售佣金",
            "colType": "MONEY",
            "regionName": "平台支出",
            "detailCols": [],
            "colCode": "salesCommission"
        },
        {
            "colName": "销售佣金占比",
            "colType": "PERCENT",
            "regionName": "平台支出",
            "detailCols": [],
            "colCode": "EFPCR23060200043"
        },
        {
            "colName": "配送费",
            "colType": "MONEY",
            "regionName": "平台支出",
            "detailCols": [
                {
                    "colName": "FBA配送费",
                    "colType": "MONEY",
                    "colCode": "fbaDeliveryFee"
                },
                {
                    "colName": "补单FBA配送费",
                    "colType": "MONEY",
                    "colCode": "amazonPatchOtherCost"
                },
                {
                    "colName": "多渠道FBA配送费",
                    "colType": "MONEY",
                    "colCode": "amazonMultichannelOtherCost"
                }
            ],
            "colCode": "EFPCR23060200046"
        },
        {
            "colName": "FBA配送费占比",
            "colType": "PERCENT",
            "regionName": "平台支出",
            "detailCols": [],
            "colCode": "EFPCR23060200047"
        },
        {
            "colName": "费用调整",
            "colType": "MONEY",
            "regionName": "平台支出",
            "detailCols": [],
            "colCode": "adjustmentFee"
        },
        {
            "colName": "国际货运费（AGL）",
            "colType": "MONEY",
            "regionName": "平台支出",
            "detailCols": [
                {
                    "colName": "国际运输费",
                    "colType": "MONEY",
                    "colCode": "internationalFreight"
                },
                {
                    "colName": "国际运输费调整",
                    "colType": "MONEY",
                    "colCode": "internationalFreightAdjustment"
                },
                {
                    "colName": "国际货运税费",
                    "colType": "MONEY",
                    "colCode": "internationalFreightTax"
                }
            ],
            "colCode": "EFPCR23060200049"
        },
        {
            "colName": "广告费",
            "colType": "MONEY",
            "regionName": "平台支出",
            "detailCols": [
                {
                    "colName": "SP广告金额",
                    "colType": "MONEY",
                    "colCode": "spFee"
                },
                {
                    "colName": "SD广告金额",
                    "colType": "MONEY",
                    "colCode": "sdFee"
                },
                {
                    "colName": "SB广告金额",
                    "colType": "MONEY",
                    "colCode": "sbFee"
                },
                {
                    "colName": "广告差异分摊金额",
                    "colType": "MONEY",
                    "colCode": "differenceFee"
                },
                {
                    "colName": "广告花费",
                    "colType": "MONEY",
                    "colCode": "advertisingSpend"
                }
            ],
            "colCode": "EFPCR23060200055"
        },
        {
            "colName": "广告花费占比",
            "colType": "PERCENT",
            "regionName": "平台支出",
            "detailCols": [],
            "colCode": "EFPCR23060200056"
        },
        {
            "colName": "推广费",
            "colType": "MONEY",
            "regionName": "平台支出",
            "detailCols": [
                {
                    "colName": "积分",
                    "colType": "MONEY",
                    "colCode": "integral"
                },
                {
                    "colName": "DEAL",
                    "colType": "MONEY",
                    "colCode": "deal"
                },
                {
                    "colName": "COUPON",
                    "colType": "MONEY",
                    "colCode": "coupon"
                },
                {
                    "colName": "其他-早期评论人计划",
                    "colType": "MONEY",
                    "colCode": "earlyReviewerProgram"
                },
                {
                    "colName": "VINE测评费",
                    "colType": "MONEY",
                    "colCode": "vineEvaluationFee"
                }
            ],
            "colCode": "EFPCR23060200065"
        },
        {
            "colName": "仓储费",
            "colType": "MONEY",
            "regionName": "平台支出",
            "detailCols": [
                {
                    "colName": "月度仓储费",
                    "colType": "MONEY",
                    "colCode": "monthStorageFee"
                },
                {
                    "colName": "超量仓储费",
                    "colType": "MONEY",
                    "colCode": "excessStorageFee"
                },
                {
                    "colName": "长期仓储费",
                    "colType": "MONEY",
                    "colCode": "longStorageFee"
                },
                {
                    "colName": "并仓费",
                    "colType": "MONEY",
                    "colCode": "consolidationFee"
                },
                {
                    "colName": "库存移除处置费",
                    "colType": "MONEY",
                    "colCode": "inventoryRemovalFee"
                },
                {
                    "colName": "退货处理费",
                    "colType": "MONEY",
                    "colCode": "returnProcessingFee"
                },
                {
                    "colName": "亚马逊物流承运人费",
                    "colType": "MONEY",
                    "colCode": "fbaCarrierFees"
                },
                {
                    "colName": "预处理费",
                    "colType": "MONEY",
                    "colCode": "preProcessingFee"
                },
                {
                    "colName": "计划外服务费",
                    "colType": "MONEY",
                    "colCode": "unplannedServiceFee"
                },
                {
                    "colName": "其他仓储费",
                    "colType": "MONEY",
                    "colCode": "otherStorage"
                }
            ],
            "colCode": "EFPCR23060200076"
        },
        {
            "colName": "月度仓储费占比",
            "colType": "PERCENT",
            "regionName": "平台支出",
            "detailCols": [],
            "colCode": "EFPCR23060200077"
        },
        {
            "colName": "亚马逊物流承运人占比",
            "colType": "PERCENT",
            "regionName": "平台支出",
            "detailCols": [],
            "colCode": "EFPCR23060200078"
        },
        {
            "colName": "其他费",
            "colType": "MONEY",
            "regionName": "平台支出",
            "detailCols": [
                {
                    "colName": "订阅费",
                    "colType": "MONEY",
                    "colCode": "subscriptionFee"
                },
                {
                    "colName": "其他-账号经理费",
                    "colType": "MONEY",
                    "colCode": "managerFee"
                },
                {
                    "colName": "ATOZ投诉费",
                    "colType": "MONEY",
                    "colCode": "atozComplaintFee"
                },
                {
                    "colName": "二次转售费用",
                    "colType": "MONEY",
                    "colCode": "gradeAndResellFee"
                },
                {
                    "colName": "清算费用",
                    "colType": "MONEY",
                    "colCode": "liquidationFee"
                },
                {
                    "colName": "其他交易费用",
                    "colType": "MONEY",
                    "colCode": "otherTransactionFees"
                },
                {
                    "colName": "平台其他费用",
                    "colType": "MONEY",
                    "colCode": "otherPlatformFees"
                },
                {
                    "colName": "其他-未归类费用",
                    "colType": "MONEY",
                    "colCode": "promotionOtherFeeSon"
                }
            ],
            "colCode": "EFPCR23060200091"
        },
        {
            "colName": "测试排序",
            "colType": "NUMBER",
            "regionName": "平台支出",
            "detailCols": [
                {
                    "colName": "清算销量",
                    "colType": "NUMBER",
                    "colCode": "liquidationAmount"
                },
                {
                    "colName": "清算调整量",
                    "colType": "NUMBER",
                    "colCode": "liquidationAdjustAmount"
                }
            ],
            "colCode": "EFPCR23072002102"
        },
        {
            "colName": "销售税",
            "colType": "MONEY",
            "regionName": "税费",
            "detailCols": [
                {
                    "colName": "商品价格税",
                    "colType": "MONEY",
                    "colCode": "commodityPriceTax"
                },
                {
                    "colName": "促销折扣税",
                    "colType": "MONEY",
                    "colCode": "promotionDiscountTax"
                },
                {
                    "colName": "买家运费税",
                    "colType": "MONEY",
                    "colCode": "buyerShippingTax"
                },
                {
                    "colName": "礼品包装税费",
                    "colType": "MONEY",
                    "colCode": "giftWrappingTax"
                },
                {
                    "colName": "市场预扣税",
                    "colType": "MONEY",
                    "colCode": "marketWithholdingTax"
                },
                {
                    "colName": "清算市场预扣税",
                    "colType": "MONEY",
                    "colCode": "liquidationTax"
                }
            ],
            "colCode": "EFPCR23060200098"
        },
        {
            "colName": "增值税",
            "colType": "MONEY",
            "regionName": "税费",
            "detailCols": [
                {
                    "colName": "TCS-CGST",
                    "colType": "MONEY",
                    "colCode": "tcsCgst"
                },
                {
                    "colName": "TCS-SGST",
                    "colType": "MONEY",
                    "colCode": "tcsSgst"
                },
                {
                    "colName": "TCS-IGST",
                    "colType": "MONEY",
                    "colCode": "tcsIgst"
                },
                {
                    "colName": "增值税收",
                    "colType": "MONEY",
                    "colCode": "addTax"
                },
                {
                    "colName": "其他税额",
                    "colType": "MONEY",
                    "colCode": "amazonWithheldTax"
                }
            ],
            "colCode": "EFPCR23060200104"
        },
        {
            "colName": "销售税退款",
            "colType": "MONEY",
            "regionName": "税费",
            "detailCols": [
                {
                    "colName": "退款税金-商品价格税",
                    "colType": "MONEY",
                    "colCode": "refundCommodityPriceTax"
                },
                {
                    "colName": "退款税金-促销折扣税",
                    "colType": "MONEY",
                    "colCode": "refundPromotionDiscountTax"
                },
                {
                    "colName": "退款税金-买家运费税",
                    "colType": "MONEY",
                    "colCode": "refundBuyerShippingTax"
                },
                {
                    "colName": "退款税金-礼品包装税",
                    "colType": "MONEY",
                    "colCode": "refundGiftWrappingTax"
                },
                {
                    "colName": "退款税金-市场预扣税",
                    "colType": "MONEY",
                    "colCode": "refundMarketWithholdingTax"
                }
            ],
            "colCode": "EFPCR23060200110"
        },
        {
            "colName": "增值税退款",
            "colType": "MONEY",
            "regionName": "税费",
            "detailCols": [
                {
                    "colName": "退款税金-TCS-CGST",
                    "colType": "MONEY",
                    "colCode": "refundTcscgst"
                },
                {
                    "colName": "退款税金-TCS-SGST",
                    "colType": "MONEY",
                    "colCode": "refundTcssgst"
                },
                {
                    "colName": "退款税金-TCS-IGST",
                    "colType": "MONEY",
                    "colCode": "refundTcsigst"
                }
            ],
            "colCode": "EFPCR23060200114"
        },
        {
            "colName": "订单退税费",
            "colType": "MONEY",
            "regionName": "税费",
            "detailCols": [],
            "colCode": "orderRetroCharge"
        },
        {
            "colName": "订单退税调整费",
            "colType": "MONEY",
            "regionName": "税费",
            "detailCols": [],
            "colCode": "refundRetroCharge"
        },
        {
            "colName": "采购成本",
            "colType": "MONEY",
            "regionName": "成本",
            "detailCols": [],
            "colCode": "purchaseCost"
        },
        {
            "colName": "头程成本",
            "colType": "MONEY",
            "regionName": "成本",
            "detailCols": [],
            "colCode": "arrivalCost"
        },
        {
            "colName": "头程成本占比",
            "colType": "PERCENT",
            "regionName": "成本",
            "detailCols": [],
            "colCode": "EFPCR23060200119"
        },
        {
            "colName": "平均头程成本",
            "colType": "MONEY",
            "regionName": "成本",
            "detailCols": [],
            "colCode": "EFPCR23060200120"
        },
        {
            "colName": "总成本",
            "colType": "MONEY",
            "regionName": "成本",
            "detailCols": [],
            "colCode": "EFPCR23060200121"
        },
        {
            "colName": "总成本占比",
            "colType": "PERCENT",
            "regionName": "成本",
            "detailCols": [],
            "colCode": "EFPCR23060200122"
        },
        {
            "colName": "退货补回成本",
            "colType": "MONEY",
            "regionName": "成本",
            "detailCols": [
                {
                    "colName": "退货补回采购成本",
                    "colType": "MONEY",
                    "colCode": "compensatePurchaseCosts"
                },
                {
                    "colName": "退货补回头程成本",
                    "colType": "MONEY",
                    "colCode": "compensateReturnCost"
                }
            ],
            "colCode": "EFPCR23060200125"
        },
        {
            "colName": "其他采购成本",
            "colType": "MONEY",
            "regionName": "成本",
            "detailCols": [
                {
                    "colName": "补单采购成本",
                    "colType": "MONEY",
                    "colCode": "amazonPatchProductCost"
                },
                {
                    "colName": "多渠道采购成本",
                    "colType": "MONEY",
                    "colCode": "amazonMultichannelProductCost"
                },
                {
                    "colName": "盘库采购成本",
                    "colType": "MONEY",
                    "colCode": "inventoryPurchaseCost"
                },
                {
                    "colName": "移除采购成本",
                    "colType": "MONEY",
                    "colCode": "removePurchaseCost"
                },
                {
                    "colName": "替换采购成本差异",
                    "colType": "MONEY",
                    "colCode": "saleReplaceDiffPurchaseCost"
                }
            ],
            "colCode": "EFPCR23060200131"
        },
        {
            "colName": "其他头程成本",
            "colType": "MONEY",
            "regionName": "成本",
            "detailCols": [
                {
                    "colName": "估实差异金额",
                    "colType": "MONEY",
                    "colCode": "estimateActualPrice"
                },
                {
                    "colName": "补单头程成本",
                    "colType": "MONEY",
                    "colCode": "amazonPatchArriveCost"
                },
                {
                    "colName": "多渠道头程成本",
                    "colType": "MONEY",
                    "colCode": "amazonMultichannelArriveCost"
                },
                {
                    "colName": "盘库头程成本",
                    "colType": "MONEY",
                    "colCode": "inventoryArrivalCost"
                },
                {
                    "colName": "移除头程成本",
                    "colType": "MONEY",
                    "colCode": "removeArrivalCost"
                },
                {
                    "colName": "替换头程成本差异",
                    "colType": "MONEY",
                    "colCode": "saleReplaceDiffArrivalCost"
                }
            ],
            "colCode": "EFPCR23060200138"
        },
        {
            "colName": "测试排序1111",
            "colType": "NUMBER",
            "regionName": "成本",
            "detailCols": [
                {
                    "colName": "FBA销量",
                    "colType": "NUMBER",
                    "colCode": "fbaSalesAmount"
                },
                {
                    "colName": "FBM销量",
                    "colType": "NUMBER",
                    "colCode": "fbmSalesAmount"
                }
            ],
            "colCode": "EFPCR23072002067"
        },
        {
            "colName": "FBM卖家运费",
            "colType": "MONEY",
            "regionName": "自定义费用",
            "detailCols": [],
            "colCode": "fbmSellerShipping"
        },
        {
            "colName": "推广订单本金",
            "colType": "MONEY",
            "regionName": "自定义费用",
            "detailCols": [],
            "colCode": "promotionPrincipalCost"
        },
        {
            "colName": "推广订单佣金",
            "colType": "MONEY",
            "regionName": "自定义费用",
            "detailCols": [],
            "colCode": "promotionCommissionCost"
        },
        {
            "colName": "推广费用",
            "colType": "MONEY",
            "regionName": "自定义费用",
            "detailCols": [],
            "colCode": "promotionCost"
        },
        {
            "colName": "汇兑损益",
            "colType": "MONEY",
            "regionName": "自定义费用",
            "detailCols": [],
            "colCode": "lossRateAmount"
        },
        {
            "colName": "其他费用",
            "colType": "MONEY",
            "regionName": "自定义费用",
            "detailCols": [],
            "colCode": "otherCost"
        },
        {
            "colName": "zml-站外费用",
            "colType": "NUMBER",
            "regionName": "自定义费用",
            "detailCols": [
                {
                    "colName": "FBA销量",
                    "colType": "NUMBER",
                    "colCode": "fbaSalesAmount"
                }
            ],
            "colCode": "EFPCR23072100580"
        },
        {
            "colName": "销售毛利-自定义",
            "colType": "MONEY",
            "regionName": "利润",
            "detailCols": [],
            "colCode": "EFPCR23072001529"
        },
        {
            "colName": "销售净利-自定义",
            "colType": "MONEY",
            "regionName": "利润",
            "detailCols": [],
            "colCode": "EFPCR23072001661"
        },
        {
            "colName": "ROI-自定义",
            "colType": "PERCENT",
            "regionName": "利润",
            "detailCols": [],
            "colCode": "EFPCR23072001718"
        },
        {
            "colName": "销售毛利率-自定义",
            "colType": "PERCENT",
            "regionName": "利润",
            "detailCols": [],
            "colCode": "EFPCR23072001896"
        },
        {
            "colName": "销售净利率-自定义",
            "colType": "PERCENT",
            "regionName": "利润",
            "detailCols": [],
            "colCode": "EFPCR23072001903"
        },
        {
            "colName": "退款占比",
            "colType": "PERCENT",
            "regionName": "占比",
            "detailCols": [
                {
                    "colName": "退款量",
                    "colType": "NUMBER",
                    "colCode": "refundAmount"
                },
                {
                    "colName": "销量",
                    "colType": "NUMBER",
                    "colCode": "alesAmount"
                }
            ],
            "colCode": "EFPCR23072500177"
        },
        {
            "colName": "排序字段123",
            "colType": "NUMBER",
            "regionName": "测试分类排序2",
            "detailCols": [
                {
                    "colName": "FBA销量",
                    "colType": "NUMBER",
                    "colCode": "fbaSalesAmount"
                },
                {
                    "colName": "FBM销量",
                    "colType": "NUMBER",
                    "colCode": "fbmSalesAmount"
                }
            ],
            "colCode": "EFPCR23072001449"
        },
        {
            "colName": "测试分类排序22",
            "colType": "NUMBER",
            "regionName": "分类1",
            "detailCols": [
                {
                    "colName": "FBA销量",
                    "colType": "NUMBER",
                    "colCode": "fbaSalesAmount"
                },
                {
                    "colName": "FBM销量",
                    "colType": "NUMBER",
                    "colCode": "fbmSalesAmount"
                }
            ],
            "colCode": "EFPCR23072100245"
        },
        {
            "colName": "zml-test-销量差异",
            "colType": "NUMBER",
            "regionName": "zml-test",
            "detailCols": [
                {
                    "colName": "FBA销量",
                    "colType": "NUMBER",
                    "colCode": "fbaSalesAmount"
                },
                {
                    "colName": "FBM销量",
                    "colType": "NUMBER",
                    "colCode": "fbmSalesAmount"
                }
            ],
            "colCode": "EFPCR23072100408"
        }
    ],
    "messages": []
}
```

---

## 45. 财务利润分析-月度查询V2

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 财务利润分析-月度查询V2 |
| 请求地址 | `/finance/sts/financialAnalysisMonth/query/V2` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| marketIds | array<int> | 否 | 站点id集合 |
| startDate | date | 是 | 开始时间 [yyyy-MM-dd 入参到月的某一天实际查询的是整月] |
| endDate | date | 是 | 结束时间 [yyyy-MM-dd 入参到月的某一天实际查询的是整月] |
| currency | string | 是 | 币种 [参考Q&A-通用参数-币种] |
| costValues | int | 是 | 成本取值 [0-先进先处理，1-月末平均，2-自定义成本] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 提示消息 |
| traceId | string | 是 | 链路追踪id |

### 请求示例

```json
{
    "costValues": 0,
    "startDate": "2023-06-01",
    "endDate": "2023-07-01",
    "currency": "USD"
}
```

### 响应示例

```json
{
    "traceId": "open_051c2a91d08c42dc99f62fd8ec1cee3e",
    "code": 200,
    "data": {
        "date": [
            "2023-07",
            "2023-06"
        ],
        "data": [
            {
                "total": 0.0,
                "children": [
                    {
                        "total": 0.0,
                        "children": [],
                        "hint": "",
                        "currencySymbol": "",
                        "currency": "",
                        "label": "zml-test-销量差异",
                        "map": {
                            "2023-06": 0,
                            "2023-07": 0
                        }
                    }
                ],
                "hint": "",
                "currencySymbol": "$",
                "currency": "USD",
                "label": "zml-test",
                "map": {
                    "2023-06": 0,
                    "2023-07": 0
                }
            }
        ]
    },
    "messages": []
}
```

---

## 46. 财务利润分析-结算明细

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 财务利润分析-结算明细 |
| 请求地址 | `/finance/sts/financialProfitAnalysis/page` |
| 请求方式 | POST |
| 限流规则 | 每 2秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| marketIds | array<int> | 否 | 站点id集合 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| startDate | date | 是 | 开始时间（市场时间） [yyyy-MM-dd] |
| endDate | date | 是 | 截止时间（市场时间） [yyyy-MM-dd] |
| currency | string | 是 | 币种 [参考Q&A-通用参数-币种] |
| feeType | string | 否 | 费用类型，查询的是feeType字段 [mergerFee-并仓费，removeFee-移除处置费，returnFee-退货处理费，dealFee-Deal，couponFee-Coupon，compensation-赔偿费用，order-订单费用，refund-退款费用，other-未归类费用，transfer-转账，storage-月度仓储费，longStorage-长期仓储费，adCost-广告花费，chargeBackRefund-退款费，amazonLogistics-亚马逊物流承运人费，atozComplaint-AtoZ投诉费，subscribe-订阅费，excessStorage-超量仓储费，earlyReviewer-早期评论人计划费，returnCardTransfer-转出失败，cardTransfer-信用卡转入，disbursementCorrect-付款更正，addTax-增值税收，otherStorage-其他仓储费，managerFee-账号经理费，liquidation-清算费用，adjustmentFee-费用调整，intFreight-国际运输费，intFreightAdjustment-国际运输费调整，intFreightTax-国际货运税费，liquidationAdjust-清算调整，trialOrder-试用订单，trialShipment-试用运费，orderRetroCharge-订单退税费，refundRetroCharge-订单退税调整费，unplannedServiceFee-计划外服务费，shippingServiceFee-航运服务费，adjustment-调整费用，preProcessingFee-预处理费，gradeAndResellFee-二次转售费，vineEvaluationFee-VINE测评费，deliveryServices-送货服务，fbmDeliveryFee-FBM配送费，compensationAdjust-赔偿调整，withholdingIncomeTax-预扣所得税] |
| type | string | 否 | 类型 |
| platformCodes | array<string> | 否 | 平台编码，默认亚马逊：AMAZON |
| saleOrderType | array<string> | 否 | 订单类型 [StandardOrder-正常订单，Multichannel-多渠道，Patch-补单，Replace-换货订单] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page":1,
    "pagesize":10,
    "currency":"USD",
    "startDate": "2020-01-01",
    "endDate":"2023-01-31"
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "total": 628867,
        "size": 0,
        "footer": [],
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "orderType": 0,
                "orderId": "",
                "otherTransactionFees": 0.0,
                "type": "Debt",
                "standardDate": "2020-04-06 15:54:25",
                "productName": "",
                "orderState": "",
                "saleOrderCostVOList": [],
                "pointsGranted": 0.0,
                "testOrderName": "",
                "marketDate": "2020-04-06 15:54:25",
                "saleOrderType": "",
                "productSales": 0.0,
                "testOrder": false,
                "id": 1,
                "promotionalRebates": 0.0,
                "sku": "",
                "fbaFees": 0.0,
                "sellingFees": 0.0,
                "zeroDate": "2020-04-06 22:54:25",
                "taxCollectionModel": "",
                "tipoDeConta": "",
                "msku": "",
                "marketplace": "",
                "tcsigst": 0.0,
                "feeType": "",
                "promotionalRebatesTax": 0.0,
                "productSalesTax": 0.0,
                "other": 0.0,
                "updateDate": "",
                "shippingCreditsTax": 0.0,
                "description": "amzn1.cam.v1.sgid.12733098381",
                "settlementId": "12794775751",
                "marketId": 2,
                "giftWrapCreditsTax": 0.0,
                "total": 0.0,
                "tcssgst": 0.0,
                "countryCode": "",
                "currency": "USD",
                "shippingCredits": 0.0,
                "marketplaceWithheldTax": 0.0,
                "createDate": "2020-04-06 7:54:25 AM PDT",
                "dataBatchNo": "",
                "product": "",
                "quantity": 0,
                "currencySymbol": "$",
                "tcscgst": 0.0,
                "orderPostal": "",
                "bogusFlag": "0",
                "orderCity": "",
                "giftWrapCredits": 0.0,
                "fulfillment": ""
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 47. 财务利润分析-分摊记录

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 财务利润分析-分摊记录 |
| 请求地址 | `/finance/sts/allocationDetail/page` |
| 请求方式 | POST |
| 限流规则 | 每 2秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| feeType | string | 否 | 费用类型 [atozComplaint-AtoZ投诉费，mergerFee-并仓费，couponFee-Coupon，longStorage-长期仓储费，excessStorage-超量仓储费，dealFee-Deal，subscribe-订阅费，adCost-广告花费，removeFee-移除处置费，other-未归类费用，amazonLogistics-亚马逊物流承运人费，storage-月度仓储费，earlyReviewer-早期评论人计划费，intFreight-国际货运费(AGL)，otherStorage-其他仓储费，managerFee-账号经理费，adjustmentFee-费用调整，gradeAndResellFee-二次转售费，vineEvaluationFee-VINE测评费] |
| marketDate | string | 否 | 分摊月份 [yyyy-MM] |
| allocationStatus | string | 否 | 分摊状态 [wait-待分摊，success-已分摊，unneed-无需分摊，failed-分摊异常] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketIds | array<int> | 否 | 站点id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize":10
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "total": 4040,
        "size": 1,
        "footer": [],
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "months": [],
                "allocationFee": 0.0,
                "currencySymbol": "₹",
                "allocationRule": "financial_logic",
                "updateTime": "2022-08-02 07:37:22",
                "feeTypeName": "费用调整",
                "allocationRuleName": "按销售订单关联的商品数量占比分摊",
                "marketIds": [],
                "feeType": "adjustmentFee",
                "feeTypes": [],
                "allocationStatusDesc": "无需分摊",
                "marketId": 23,
                "marketName": "积加测试店铺2:IN",
                "createTime": "2022-08-01 07:00:13",
                "marketDate": "2022-08",
                "currency": "INR",
                "id": "20197",
                "allocationDesc": "",
                "allocationStatus": "unneed"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 48. 商品统计

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品统计 |
| 请求地址 | `/operation/sts/listingAnalyze/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| viewType | string | 是 | 日期类型 [day-日，week-周，month-月] |
| showCurrencyType | string | 是 | 显示币种 [参考Q&A-通用参数-币种] |
| beginDate | string | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | string | 是 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| target | string | 是 | 查询显示的字段 [unitsOrdered-销量，orders-订单量，orderProductSales-销售额] |
| marketList | array<int> | 否 | 站点ID列表 |
| asin | string | 否 | asin |
| msku | string | 否 | msku |
| sku | string | 否 | sku |
| groupByType | string | 是 | 查询维度 [seller_sku; asin] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10,
    "target": "unitsOrdered",
    "groupByType": "seller_sku",
    "viewType": "day",
    "beginDate": "2020-08-01",
    "endDate": "2020-08-30",
    "showCurrencyType": "YUAN"
}
```

### 响应示例

```json
{
    "traceId": "open_53aabbd5887c49e0bf969d6cd6c86bae",
    "code": 200,
    "data": {
        "total": 366,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "country": 1,
                "dateline": null,
                "fbaTurnover": 0.0,
                "productManagerAccount": "-",
                "listingLevel": "-",
                "sellingManagerName": "-",
                "title": null,
                "serverId": 1,
                "categoryName": "-",
                "productName": null,
                "marketId": 1,
                "sellingPrice": null,
                "planStorageQuantity": 0,
                "shippedQuantity": 0,
                "receivingQuantity": 0,
                "sku": "11 inch protector",
                "brand": "-",
                "reservedTrocessing": 0,
                "brandCode": null,
                "msku": "11 inch protector",
                "isParent": false,  
                "crawlTitle": "",
                "firstSalesDate": null,
                "asinUrl": "https://www.amazon.com/gp/product/B07MD5CZKJ",
                "variationAsin": "-",
                "addDate": "2018-12-24 17:15:41",
                "subtotalAmount": {
                    "amount": "0",
                    "prefix": ""
                },
                "imgUrl": "",
                "marketName": "一号店--有广告数据:US",
                "subtotal": "0",
                "reservedTransfers": 0,
                "asin": "B07MD5CZKJ",
                "amountVoMap": {
                    "2023-01-01": {
                        "amount": "0",
                        "prefix": "",
                        "format": null
                    }
                },
                "countryName": "US",
                "selfDeliveryQuantity": 0,
                "category": "NO",
                "fbaQuantity": 0,
                "listingState": "-",
                "fbmQuantity": 0
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 49. 店铺统计

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 店铺统计 |
| 请求地址 | `/operation/sts/marketAnalyze/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| marketList | array<int> | 否 | 店铺ID列表 |
| showCurrencyType | string | 是 | 显示币种 [参考Q&A-通用参数-币种] |
| beginDate | string | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | string | 是 | 结束时间 [yyyy-MM-dd] |
| viewType | string | 是 | 查询维度类型 [day-日，week-周，month-月] |
| target | string | 是 | 查询显示的字段 [unitsOrdered-销量，orders-订单量] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "target": "unitsOrdered",
    "viewType": "day",
    "beginDate": "2020-08-01",
    "endDate": "2020-08-31",
    "showCurrencyType": "YUAN"
}
```

### 响应示例

```json
{
    "traceId": "open_cf9e7c0e926d4debbcf1852898b1a09f",
    "code": 200,
    "data": {
        "total": 0,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "marketId": 4,
                "subtotalAmount": {
                    "amount": "31393",
                    "prefix": ""
                },
                "marketName": "JYStore:US",
                "amountVoMap": {
                    "2020-08-29": {
                        "amount": "883",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-07": {
                        "amount": "843",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-28": {
                        "amount": "945",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-06": {
                        "amount": "942",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-27": {
                        "amount": "1035",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-05": {
                        "amount": "905",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-26": {
                        "amount": "1063",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-04": {
                        "amount": "991",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-09": {
                        "amount": "805",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-08": {
                        "amount": "754",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-21": {
                        "amount": "1048",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-20": {
                        "amount": "1108",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-25": {
                        "amount": "1098",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-03": {
                        "amount": "1058",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-24": {
                        "amount": "1073",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-02": {
                        "amount": "1337",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-23": {
                        "amount": "907",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-01": {
                        "amount": "1002",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-22": {
                        "amount": "865",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-18": {
                        "amount": "1141",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-17": {
                        "amount": "1184",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-16": {
                        "amount": "961",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-15": {
                        "amount": "945",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-19": {
                        "amount": "1225",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-10": {
                        "amount": "1061",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-31": {
                        "amount": "1052",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-30": {
                        "amount": "851",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-14": {
                        "amount": "1158",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-13": {
                        "amount": "1061",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-12": {
                        "amount": "1052",
                        "prefix": "",
                        "format": null
                    },
                    "2020-08-11": {
                        "amount": "1040",
                        "prefix": "",
                        "format": null
                    }
                }
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 50. 产品表现

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 产品表现 |
| 请求地址 | `/operation/sts/productAnalyzeMultiIndex/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| beginDate | string | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | string | 是 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| showCurrencyType | string | 是 | 显示币种类型 [参考Q&A-通用参数-币种] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10,
    "beginDate": "2023-01-01",
    "endDate": "2023-01-10",
    "showCurrencyType": "USD"
}
```

### 响应示例

```json
{
    "traceId": "open_211b347ea55d4d0685ef724e18252a70",
    "code": 200,
    "data": {
        "total": 76,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "storageFeeAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "fbaTurnover": null,
                "mainSellerRank": null,
                "buyBoxPercentage": null,
                "bogusOthersCost": null,
                "bogusPurchaseCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "discountCost": null,
                "multichannelAmazonCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "bogusVatCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "bogusVatCost": null,
                "platformFeeAmount": null,
                "brand": "-",
                "reservedTrocessing": null,
                "ctr": null,
                "bogusSalesCost": null,
                "refundDiscountCost": null,
                "avgUnitsOrderedSales": null,
                "shippingCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "discountCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "reviewQuantity": null,
                "patchAmazonCost": null,
                "reservedTransfers": null,
                "returns": 0,
                "averagePrice": null,
                "orderProductSalesB2b": 0.0,
                "discountCostSales": 0.0,
                "listingLevel": null,
                "fbmShippingCost": null,
                "patchArriveCost": null,
                "avgOrderItemsSales": 0,
                "sellingPrice": null,
                "amazonTaxAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "averagePriceAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "currency": null,
                "vatCostAmount": null,
                "cvr": null,
                "purchaseCost": null,
                "star": null,
                "asinUrl": null,
                "addDate": null,
                "cr": null,
                "marketName": null,
                "sellerRankCategory": null,
                "country": null,
                "unitSessionPercentage": null,
                "patchAmazonCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "platformFee": null,
                "bogusArriveCost": null,
                "naturalOrders": 0,
                "returnsPurchaseCost": null,
                "orderBogusCount": null,
                "adsSpendAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "returnProductSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "totalRevenue": null,
                "refundCost": null,
                "shippingCost": null,
                "isParent": null,
                "returnsArriveCost": null,
                "sellerRank": null,
                "returnsRate": 0.0,
                "multichannelPurchaseCost": null,
                "adsCvr": null,
                "unitsOrderedB2b": 0,
                "patchUnitsOrdered": null,
                "productShippingCost": null,
                "countryName": null,
                "fbaQuantity": null,
                "vatCost": null,
                "returnsArriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "refundTaxCost": null,
                "fbmShippingCostAmount": null,
                "sellable": null,
                "orderItems": null,
                "marketId": 4,
                "salesNetProfitRate": 0.0,
                "multichannelPurchaseCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "shippedQuantity": null,
                "asoAS": null,
                "salesNetProfit": null,
                "bogusDiscountCost": null,
                "multichannelAmazonCost": null,
                "refundCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "asin": null,
                "acoAS": null,
                "unitsOrdered": 0,
                "adsSales": null,
                "patchPurchaseCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "productManagerAccount": "",
                "multichannelArriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "patchPurchaseCost": null,
                "productName": "ANK-B",
                "roAS": null,
                "salesNetProfitAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "id": null,
                "orderIds": "",
                "sku": "ANK-B",
                "adsOrders": null,
                "sessions": null,
                "productShippingCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "costPerClick": null,
                "returnsSellable": null,
                "crawlTitle": null,
                "purchaseAccount": null,
                "orderItemsB2b": null,
                "variationAsin": null,
                "productCostRate": null,
                "totalSpend": null,
                "pageViews": null,
                "warehouseId": null,
                "brandId": null,
                "orders": 0,
                "returnsPurchaseCostAmount": null,
                "bogusQuantity": null,
                "refundTaxCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "arriveCost": null,
                "serverName": null,
                "sellingManagerName": null,
                "acoS": null,
                "grossProfitRate": 0.0,
                "refunds": 0,
                "naturalOrdersRate": 0,
                "returnProductSales": 0.0,
                "mainSellerRankCategory": null,
                "bogusOrders": null,
                "fbmTurnover": null,
                "salesGrossProfitAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "adsClicks": null,
                "orderProductSales": 0.0,
                "refundsRate": 0.0,
                "orderProductSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "fbmQuantity": null,
                "storageFee": null,
                "othersCostAmount": null,
                "onInventory": 1944.04,
                "serverId": null,
                "amazonTax": null,
                "unitsOrderedTraffic": null,
                "purchaseCostRate": null,
                "bogusOthersCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "cpc": null,
                "planStorageQuantity": null,
                "fbaShippingCost": null,
                "patchArriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "msku": null,
                "discountCostSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "commissionCostAmount": null,
                "firstSalesDate": null,
                "bogusArriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "arriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "avgOrderItems": 0,
                "multichannelArriveCost": null,
                "adsSpend": null,
                "bogusSalesCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "categoryName": "01-地垫",
                "bogusDiscountCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "statisticsDate": null,
                "receivingQuantity": null,
                "salesGrossProfit": null,
                "refundDiscountCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "adsImpressions": null,
                "fbaShippingCostAmount": null,
                "arriveCostRate": null,
                "purchaseCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "costPerClickSale": null,
                "imgUrl": "",
                "multiChannelOrders": 0,
                "adsSalesAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "othersCost": null,
                "bogusPurchaseCost": null,
                "commissionCost": null,
                "fulfillment": null,
                "category": "01",
                "listingState": null
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 51. 商品表现

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 商品表现 |
| 请求地址 | `/operation/sts/listingAnalyzeMultiIndex/page` |
| 请求方式 | POST |
| 限流规则 | 每 5秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| showCurrencyType | string | 是 | 显示币种 [参考Q&A-通用参数-币种] |
| beginDate | date | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | date | 是 | 结束时间 [yyyy-MM-dd] |
| isShowTotal | boolean | 是 | 是否显示合计 [显示合计: true; 不显示合计： false] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketList | array<int> | 否 | 站点ID列表 |
| sku | string | 否 | sku |
| asin | string | 否 | asin |
| asinList | array<string> | 否 | asin集合（一次建议不超过20） |
| msku | string | 否 | msku |
| mskuList | array<string> | 否 | msku集合（一次建议不超过20） |
| groupByType | string | 是 | 查询维度 [asin-ASIN维度，seller_sku-MSKU维度] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20,
    "showCurrencyType": "USD",
    "isShowTotal": false,
    "groupByType":"asin",
    "beginDate":"2022-09-07",
    "endDate":"2022-09-08"
}
```

### 响应示例

```json
{
    "traceId": "open_160f5d95ad8c432fafdabc90fe57b3cf",
    "code": 200,
    "data": {
        "total": 151,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "storageFeeAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "fbaTurnover": 0.0,
                "bogusPurchaseCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "discountCost": 0.0,
                "multichannelAmazonCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "bogusVatCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "brand": "-",
                "reservedTrocessing": 0,
                "ctr": 0.0,
                "bogusSalesCost": 0.0,
                "avgUnitsOrderedSales": 36.85,
                "shippingCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "discountCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "reservedTransfers": 0,
                "returns": 0,
                "averagePrice": 36.85,
                "orderProductSalesB2b": 0.0,
                "discountCostSales": 36.85,
                "listingLevel": "-",
                "avgOrderItemsSales": 36.85,
                "sellingPrice": 0.0,
                "amazonTaxAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "averagePriceAmount": {
                    "currencyAmount": 36.85,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$36.85"
                },
                "currency": "USD",
                "asinUrl": "https://www.amazon.co.jp/gp/product/B087F4ZYTB",
                "cr": 0.0,
                "marketName": "一号店-有广告数据:JP",
                "country": 2,
                "patchAmazonCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "naturalOrders": 1,
                "adsSpendAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "returnProductSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "isParent": false,
                "returnsRate": 0.0,
                "adsCvr": 0.0,
                "unitsOrderedB2b": 0,
                "patchUnitsOrdered": 0,
                "countryName": "JP",
                "fbaQuantity": 200,
                "returnsArriveCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "orderItems": 1,
                "marketId": 12,
                "salesNetProfitRate": 84.67,
                "multichannelPurchaseCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "shippedQuantity": 0,
                "asoAS": 0.0,
                "salesNetProfit": 31.2,
                "refundCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "asin": "B087F4ZYTB",
                "acoAS": 0.0,
                "unitsOrdered": 1,
                "adsSales": 0.0,
                "patchPurchaseCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "productManagerAccount": "-",
                "multichannelArriveCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "roAS": 0.0,
                "salesNetProfitAmount": {
                    "currencyAmount": 31.2,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$31.20"
                },
                "id": 30642623,
                "orderIds": "",
                "sku": "HB245-RG-JP",
                "adsOrders": 0,
                "productShippingCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "orderItemsB2b": 0,
                "variationAsin": "-",
                "warehouseId": 13,
                "orders": 1,
                "bogusQuantity": 0,
                "refundTaxCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "sellingManagerName": "-",
                "acoS": 0.0,
                "grossProfitRate": 84.67,
                "refunds": 0,
                "naturalOrdersRate": 100.0,
                "returnProductSales": 0.0,
                "bogusOrders": 0,
                "salesGrossProfitAmount": {
                    "currencyAmount": 31.2,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$31.20"
                },
                "adsClicks": 0,
                "orderProductSales": 36.85,
                "refundsRate": 0.0,
                "orderProductSalesAmount": {
                    "currencyAmount": 36.85,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$36.85"
                },
                "fbmQuantity": 0,
                "serverId": 1,
                "unitsOrderedTraffic": 0,
                "bogusOthersCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "cpc": 0.0,
                "planStorageQuantity": 0,
                "patchArriveCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "msku": "HB245-RG-JP",
                "discountCostSalesAmount": {
                    "currencyAmount": 36.85,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$36.85"
                },
                "bogusArriveCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "arriveCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "avgOrderItems": 1.0,
                "adsSpend": 0.0,
                "bogusSalesCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "categoryName": "-",
                "bogusDiscountCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "statisticsDate": "2022-09-08",
                "receivingQuantity": 0,
                "salesGrossProfit": 31.2,
                "refundDiscountCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "adsImpressions": 0,
                "purchaseCostAmount": {
                    "currencySymbol": "$",
                    "currencyCode": "USD"
                },
                "imgUrl": "",
                "multiChannelOrders": 0,
                "adsSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "category": "-",
                "listingState": "-"
            }
        ]
    },
    "messages": ["request.success"]
}
```

---

## 52. 店铺表现

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 店铺表现 |
| 请求地址 | `/operation/sts/storeSalesPerformance/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| showCurrencyType | string | 是 | 显示的币种 [参考Q&A-通用参数-币种] |
| beginDate | string | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | string | 是 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketList | array<int> | 否 | 站点ID列表 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10,
    "beginDate": "2023-01-01",
    "endDate": "2023-01-10",
    "showCurrencyType": "USD"
}
```

### 响应示例

```json
{
    "traceId": "open_75eb050957a94b019a20e552bb94db15",
    "code": 200,
    "data": {
        "total": 14,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "storageFeeAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "fbaTurnover": null,
                "mainSellerRank": null,
                "buyBoxPercentage": null,
                "bogusOthersCost": null,
                "bogusPurchaseCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "discountCost": null,
                "multichannelAmazonCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "bogusVatCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "bogusVatCost": null,
                "platformFeeAmount": null,
                "brand": null,
                "reservedTrocessing": 0,
                "ctr": null,
                "bogusSalesCost": null,
                "refundDiscountCost": null,
                "avgUnitsOrderedSales": null,
                "shippingCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "discountCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "reviewQuantity": null,
                "patchAmazonCost": null,
                "reservedTransfers": 0,
                "returns": 0,
                "averagePrice": null,
                "orderProductSalesB2b": 0.0,
                "discountCostSales": 0.0,
                "listingLevel": null,
                "fbmShippingCost": null,
                "patchArriveCost": null,
                "avgOrderItemsSales": 0,
                "sellingPrice": null,
                "amazonTaxAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "averagePriceAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "currency": "USD",
                "vatCostAmount": null,
                "cvr": 0.0,
                "purchaseCost": null,
                "star": null,
                "asinUrl": null,
                "addDate": null,
                "cr": null,
                "marketName": "一号店:CA",
                "sellerRankCategory": null,
                "country": null,
                "unitSessionPercentage": null,
                "patchAmazonCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "platformFee": null,
                "bogusArriveCost": null,
                "naturalOrders": 0,
                "returnsPurchaseCost": null,
                "orderBogusCount": null,
                "adsSpendAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "returnProductSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "totalRevenue": null,
                "refundCost": null,
                "shippingCost": null,
                "isParent": null,
                "returnsArriveCost": null,
                "sellerRank": null,
                "returnsRate": 0.0,
                "multichannelPurchaseCost": null,
                "adsCvr": 0.0,
                "unitsOrderedB2b": 0,
                "patchUnitsOrdered": 0,
                "productShippingCost": null,
                "countryName": "CA",
                "fbaQuantity": 123,
                "vatCost": null,
                "returnsArriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "refundTaxCost": null,
                "fbmShippingCostAmount": null,
                "sellable": 77931.36,
                "orderItems": 0,
                "marketId": 2,
                "salesNetProfitRate": 0.0,
                "multichannelPurchaseCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "shippedQuantity": 0,
                "asoAS": 0.0,
                "salesNetProfit": 0.0,
                "bogusDiscountCost": null,
                "multichannelAmazonCost": null,
                "refundCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "asin": null,
                "acoAS": 0.0,
                "unitsOrdered": 0,
                "adsSales": 0.0,
                "patchPurchaseCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "productManagerAccount": null,
                "multichannelArriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "patchPurchaseCost": null,
                "productName": null,
                "roAS": 0.0,
                "salesNetProfitAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "id": null,
                "orderIds": null,
                "sku": null,
                "adsOrders": 0,
                "sessions": null,
                "productShippingCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "costPerClick": null,
                "returnsSellable": null,
                "crawlTitle": null,
                "purchaseAccount": null,
                "orderItemsB2b": null,
                "variationAsin": null,
                "productCostRate": null,
                "totalSpend": null,
                "pageViews": null,
                "warehouseId": null,
                "brandId": null,
                "orders": 0,
                "returnsPurchaseCostAmount": null,
                "bogusQuantity": null,
                "refundTaxCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "arriveCost": null,
                "serverName": null,
                "sellingManagerName": null,
                "acoS": 0.0,
                "grossProfitRate": 0.0,
                "refunds": 0,
                "naturalOrdersRate": 0,
                "returnProductSales": 0.0,
                "mainSellerRankCategory": null,
                "bogusOrders": null,
                "fbmTurnover": null,
                "salesGrossProfitAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "adsClicks": 0,
                "orderProductSales": 0.0,
                "refundsRate": 0.0,
                "orderProductSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "fbmQuantity": 5008,
                "storageFee": null,
                "othersCostAmount": null,
                "onInventory": null,
                "serverId": null,
                "amazonTax": null,
                "unitsOrderedTraffic": null,
                "purchaseCostRate": null,
                "bogusOthersCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "cpc": 0.0,
                "planStorageQuantity": 0,
                "fbaShippingCost": null,
                "patchArriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "msku": null,
                "discountCostSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "commissionCostAmount": null,
                "firstSalesDate": null,
                "bogusArriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "arriveCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "avgOrderItems": 0,
                "multichannelArriveCost": null,
                "adsSpend": 0.0,
                "bogusSalesCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "categoryName": null,
                "bogusDiscountCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "statisticsDate": null,
                "receivingQuantity": 0,
                "salesGrossProfit": 0.0,
                "refundDiscountCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "adsImpressions": null,
                "fbaShippingCostAmount": null,
                "arriveCostRate": null,
                "purchaseCostAmount": {
                    "currencyAmount": null,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": null
                },
                "costPerClickSale": null,
                "imgUrl": null,
                "multiChannelOrders": 0,
                "adsSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "othersCost": null,
                "bogusPurchaseCost": null,
                "commissionCost": null,
                "fulfillment": null,
                "category": null,
                "listingState": null
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 53. 销售利润分析

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 销售利润分析 |
| 请求地址 | `/operation/sts/saleProfit/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| beginDate | date | 否 | 查询开始时间 [yyyy-MM-dd]，日期维度与月维度请传一种 |
| endDate | date | 否 | 查询结束时间 [yyyy-MM-dd]，日期维度与月维度请传一种 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| type | string | 是 | 查询维度类型 [PARENT-父ASIN维度，ASIN-ASIN维度，MSKU-MSKU维度，MARKET-店铺维度] |
| year | string | 否 | 开始年(月维度)，日期维度与月维度请传一种 |
| month | string | 否 | 开始月(月维度)，日期维度与月维度请传一种 |
| endYear | string | 否 | 结束年(月维度)，日期维度与月维度请传一种 |
| endMonth | string | 否 | 结束月(月维度)，日期维度与月维度请传一种 |
| showCurrencyType | string | 是 | 显示币种，参考Q&A文档-通用参数-币种 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10,
    "type": "MSKU",
    "showCurrencyType": "USD",
    "beginDate":"2023-01-01",
    "endDate":"2023-01-15"
}
```

### 响应示例

```json
{
    "traceId": "open_fb8fa47cbd83498a81d45eeff4fef04e",
    "code": 200,
    "data": {
        "total": 366,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "storageFeeAmount": {
                    "currencyAmount": -0.17,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$-0.17"
                },
                "fbaTurnover": null,
                "mainSellerRank": null,
                "buyBoxPercentage": null,
                "bogusOthersCost": 0.0,
                "bogusPurchaseCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "discountCost": 0.0,
                "multichannelAmazonCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "bogusVatCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "bogusVatCost": 0.0,
                "platformFeeAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "brand": "-",
                "reservedTrocessing": null,
                "ctr": null,
                "bogusSalesCost": 0.0,
                "refundDiscountCost": 0.0,
                "avgUnitsOrderedSales": null,
                "shippingCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "discountCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "reviewQuantity": null,
                "patchAmazonCost": 0.0,
                "reservedTransfers": null,
                "returns": 0,
                "averagePrice": 0.0,
                "orderProductSalesB2b": null,
                "discountCostSales": 0.0,
                "listingLevel": "-",
                "fbmShippingCost": 0.0,
                "patchArriveCost": 0.0,
                "avgOrderItemsSales": 0,
                "sellingPrice": null,
                "amazonTaxAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "averagePriceAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "currency": "USD",
                "vatCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "cvr": null,
                "purchaseCost": 0.0,
                "star": null,
                "asinUrl": "https://www.amazon.com/gp/product/B07MD5CZKJ",
                "addDate": null,
                "cr": null,
                "marketName": "一号店--有广告数据:US",
                "adsItemOrders": 0,
                "sellerRankCategory": null,
                "country": 1,
                "unitSessionPercentage": null,
                "patchAmazonCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "platformFee": 0.0,
                "bogusArriveCost": 0.0,
                "naturalOrders": 0,
                "returnsPurchaseCost": 0.0,
                "orderBogusCount": null,
                "adsSpendAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "returnProductSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "totalRevenue": null,
                "refundCost": 0.0,
                "shippingCost": 0.0,
                "isParent": false,
                "returnsArriveCost": 0.0,
                "adsNaturalOrders": 0,
                "sellerRank": null,
                "returnsRate": 0.0,
                "multichannelPurchaseCost": 0.0,
                "adsCvr": null,
                "unitsOrderedB2b": null,
                "patchUnitsOrdered": 0,
                "productShippingCost": 0.0,
                "countryName": "US",
                "fbaQuantity": null,
                "vatCost": 0.0,
                "returnsArriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "refundTaxCost": 0.0,
                "fbmShippingCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "sellable": null,
                "orderItems": null,
                "marketId": 1,
                "salesNetProfitRate": 0.0,
                "multichannelPurchaseCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "shippedQuantity": null,
                "asoAS": null,
                "salesNetProfit": -0.17,
                "bogusDiscountCost": 0.0,
                "multichannelAmazonCost": 0.0,
                "refundCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "asin": "B07MD5CZKJ",
                "acoAS": null,
                "unitsOrdered": 0,
                "adsSales": 0.0,
                "patchPurchaseCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "productManagerAccount": "-",
                "multichannelArriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "patchPurchaseCost": 0.0,
                "productName": null,
                "roAS": null,
                "salesNetProfitAmount": {
                    "currencyAmount": -0.17,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$-0.17"
                },
                "id": 30656216,
                "orderIds": null,
                "sku": "11 inch protector",
                "adsOrders": 0,
                "sessions": null,
                "productShippingCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "costPerClick": 0.0,
                "returnsSellable": 0,
                "crawlTitle": "",
                "purchaseAccount": "",
                "orderItemsB2b": null,
                "variationAsin": "-",
                "adsItemSales": 0.0,
                "productCostRate": 0.0,
                "totalSpend": null,
                "pageViews": null,
                "warehouseId": null,
                "brandId": null,
                "orders": 0,
                "returnsPurchaseCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "bogusQuantity": 0,
                "refundTaxCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "arriveCost": 0.0,
                "serverName": null,
                "sellingManagerName": "-",
                "acoS": null,
                "grossProfitRate": 0.0,
                "refunds": 0,
                "naturalOrdersRate": 0,
                "returnProductSales": 0.0,
                "mainSellerRankCategory": null,
                "bogusOrders": null,
                "fbmTurnover": null,
                "adsItemSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "salesGrossProfitAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "adsClicks": null,
                "orderProductSales": 0.0,
                "refundsRate": 0.0,
                "orderProductSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "fbmQuantity": null,
                "storageFee": -0.17,
                "othersCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "onInventory": null,
                "serverId": 1,
                "amazonTax": 0.0,
                "unitsOrderedTraffic": null,
                "purchaseCostRate": 0.0,
                "bogusOthersCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "cpc": null,
                "planStorageQuantity": null,
                "fbaShippingCost": 0.0,
                "patchArriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "msku": "11 inch protector",
                "discountCostSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "commissionCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "firstSalesDate": null,
                "bogusArriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "arriveCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "avgOrderItems": 0,
                "multichannelArriveCost": 0.0,
                "adsSpend": 0.0,
                "bogusSalesCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "categoryName": "-",
                "bogusDiscountCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "adsNaturalOrdersRate": 0,
                "statisticsDate": "2023-01-01",
                "receivingQuantity": null,
                "salesGrossProfit": 0.0,
                "refundDiscountCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "adsImpressions": null,
                "fbaShippingCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "arriveCostRate": 0.0,
                "purchaseCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "costPerClickSale": 0.0,
                "imgUrl": null,
                "multiChannelOrders": 0,
                "adsSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "othersCost": 0.0,
                "bogusPurchaseCost": 0.0,
                "commissionCost": 0.0,
                "fulfillment": null,
                "category": "-",
                "listingState": "-"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 54. 流量统计-msku

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 流量统计-msku |
| 请求地址 | `/operation/sts/trafficSku/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| currency | string | 是 | 展示币种 [参考Q&A-通用参数-币种] |
| beginDate | date | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | date | 是 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| viewType | string | 是 | 查询维度类型 [day-日，week-周，month-月] |
| marketList | array<int> | 否 | 站点ID列表 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10,
    "currency": "USD",
    "beginDate":"2023-01-01",
    "endDate":"2023-02-15",
    "viewType": "day"
}
```

### 响应示例

```json
{
    "traceId": "open_c197e2f99a67413aaafa2de9d2be39f2",
    "code": 200,
    "data": {
        "total": 564,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "totalOrderItems": 3,
                "memo": "",
                "browserSessions": 38,
                "appSessions": 71,
                "productName": "-",
                "browserSessionPer": 48.1,
                "marketString": null,
                "unitsOrderedB2B": 0,
                "buyBoxPer": 100.0,
                "id": 204090,
                "sku": "GLUK-K11BI11B-7Ha8B9",
                "brand": null,
                "sessions": 109,
                "brandName": "-",
                "msku": "GLUK-K11BI11B-7Ha8B9",
                "totalOrderItemsB2B": 0,
                "firstSalesDate": "2022-09-15",
                "sessionPer": 53.96,
                "orderedProductSalesB2B": 0.0,
                "browserPageViews": 45,
                "browserPageViewsPer": 43.69,
                "pageViews": 177,
                "spu": "-",
                "countryName": null,
                "operationLogList": [],
                "parentAsin": "B0B55SNNB7",
                "orderedProductSalesB2BAmountExportString": null,
                "orderedProductSalesAmountExportString": null,
                "dateline": "2023-01-01",
                "listingLevel": "-",
                "lossTraffics": null,
                "sellingManagerName": "-",
                "title": "",
                "unitSessionPer": 2.75,
                "categoryName": "-",
                "marketId": 26,
                "operationLogId": null,
                "orderedProductSalesB2BAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "imageUrl": null,
                "recordDate": "2023-01-01",
                "appPageViewsPer": 58.93,
                "currency": null,
                "productManagerName": "-",
                "orderedProductSales": 235.95,
                "orderedProductSalesAmount": {
                    "currencyAmount": 235.95,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$235.95"
                },
                "appPageViews": 132,
                "appSessionPer": 57.72,
                "pageViewsPer": 54.13,
                "unitSessionPerB2B": 0.0,
                "asinUrl": "https://www.amazon.co.uk/gp/product/B0B55SNNB7",
                "addDate": "2022-07-21 09:02:47",
                "marketName": "36UK:UK",
                "asin": "B0B55SNNB7",
                "category": null,
                "unitsOrdered": 3,
                "listingState": "-"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 55. 流量统计-ASIN

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 流量统计-ASIN |
| 请求地址 | `/operation/sts/traffic/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| currency | string | 是 | 币种 [参考Q&A-通用参数-币种] |
| beginDate | string | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | string | 是 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| viewType | string | 是 | 查询维度类型 [day-日，week-周，month-月] |
| marketList | array<int> | 否 | 站点ID数组 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10,
    "currency": "USD",
    "beginDate":"2023-01-01",
    "endDate":"2023-02-15",
    "viewType": "day"
}
```

### 响应示例

```json
{
    "traceId": "open_a498faa9dcd74a96b1861067bdb4aba5",
    "code": 200,
    "data": {
        "total": 938,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "totalOrderItems": 6,
                "memo": null,
                "browserSessions": 57,
                "marketIds": null,
                "appSessions": 62,
                "productName": "",
                "browserSessionPer": 4.12,
                "marketString": null,
                "unitsOrderedB2B": 0,
                "buyBoxPer": 100.0,
                "id": 352588,
                "sku": "-",
                "brand": "NO",
                "sessions": 119,
                "brandName": "-",
                "isParent": false,
                "targetCurrency": null,
                "totalOrderItemsB2B": 0,
                "sessionPer": 3.5,
                "orderedProductSalesB2B": 0.0,
                "browserPageViews": 81,
                "browserPageViewsPer": 4.17,
                "pageViews": 182,
                "spu": "",
                "countryName": null,
                "operationLogList": [],
                "parentAsin": "B0BMZYTJPP",
                "orderedProductSalesB2BAmountExportString": null,
                "orderedProductSalesAmountExportString": null,
                "dateline": "2023-02-03",
                "lossTraffics": null,
                "sellingManagerName": "-",
                "title": "",
                "unitSessionPer": 5.04,
                "categoryName": "-",
                "countryId": 3,
                "marketId": 26,
                "operationLogId": null,
                "orderedProductSalesB2BAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "imageUrl": null,
                "recordDate": null,
                "appPageViewsPer": 2.95,
                "productManagerName": "-",
                "orderedProductSales": 296.297719047,
                "orderedProductSalesAmount": {
                    "currencyAmount": 296.297719047,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$296.297719047"
                },
                "appPageViews": 101,
                "appSessionPer": 3.08,
                "pageViewsPer": 3.39,
                "unitSessionPerB2B": 0.0,
                "asinUrl": "https://www.amazon.co.uk/gp/product/B0B4NR36DS",
                "marketName": "36UK:UK",
                "asin": "B0B4NR36DS",
                "category": "NO",
                "unitsOrdered": 6
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 56. 流量数据-msku

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 流量数据-msku |
| 请求地址 | `/operation/sts/trafficSkuAnalysis/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| currency | string | 是 | 展示币种 [参考Q&A-通用参数-币种] |
| beginDate | string | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | string | 是 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| viewType | string | 是 | 查询维度类型 [day-日，week-周，month-月] |
| marketList | array<int> | 否 | 站点ID列表 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "viewType": "day",
    "currency": "YUAN",
    "beginDate": "2023-03-25",
    "endDate": "2023-03-29",
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_6d0bcf52b2cf41369b0964679abc9acd",
    "code": 200,
    "data": {
        "total": 1,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "totalOrderItems": 7,
                "memo": "",
                "browserSessions": 51,
                "appSessions": 90,
                "productName": "-",
                "browserSessionPer": 50.0,
                "marketString": null,
                "unitsOrderedB2B": 0,
                "buyBoxPer": 100.0,
                "id": 204256,
                "sku": "G*******9",
                "brand": null,
                "sessions": 141,
                "brandName": "-",
                "msku": "GLU*******B9",
                "totalOrderItemsB2B": 0,
                "firstSalesDate": "2022-09-15",
                "sessionPer": 53.41,
                "orderedProductSalesB2B": 0.0,
                "browserPageViews": 75,
                "browserPageViewsPer": 51.37,
                "pageViews": 238,
                "spu": "-",
                "countryName": null,
                "operationLogList": [],
                "parentAsin": "B0*****B7",
                "orderedProductSalesB2BAmountExportString": null,
                "orderedProductSalesAmountExportString": null,
                "dateline": "2023-03-25",
                "listingLevel": "-",
                "lossTraffics": null,
                "sellingManagerName": "-",
                "title": "",
                "unitSessionPer": 4.96,
                "categoryName": "-",
                "marketId": 26,
                "operationLogId": null,
                "orderedProductSalesB2BAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￡",
                    "currencyCode": "YUAN",
                    "amountWithSymbol": "0"
                },
                "imageUrl": null,
                "recordDate": "2023-03-25",
                "appPageViewsPer": 61.74,
                "currency": null,
                "productManagerName": "-",
                "orderedProductSales": 456.98,
                "orderedProductSalesAmount": {
                    "currencyAmount": 456.98,
                    "currencySymbol": "￡",
                    "currencyCode": "YUAN",
                    "amountWithSymbol": "￡456.98"
                },
                "appPageViews": 163,
                "appSessionPer": 55.56,
                "pageViewsPer": 58.05,
                "unitSessionPerB2B": 0.0,
                "asinUrl": "https://www.amazon.co.uk/gp/product/******",
                "addDate": "2022-07-21 09:02:47",
                "marketName": "36UK:UK",
                "asin": "B******",
                "category": null,
                "unitsOrdered": 7,
                "listingState": "-"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 57. 流量数据-ASIN

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 流量数据-ASIN |
| 请求地址 | `/operation/sts/trafficAnalysis/page` |
| 请求方式 | POST |
| 限流规则 | 每 1分钟 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| currency | string | 是 | 币种 [参考Q&A-通用参数-币种] |
| beginDate | date | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | date | 是 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketList | array<int> | 否 | 站点ID数组 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10,
    "currency": "USD",
    "beginDate":"2023-01-01",
    "endDate":"2023-02-15"
}
```

### 响应示例

```json
{
    "traceId": "open_dd3c700a17424d428c2b60ee51151a08",
    "code": 200,
    "data": {
        "total": 204,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "totalOrderItems": 0,
                "marketIds": "1",
                "productName": "12",
                "marketString": null,
                "unitsOrderedB2B": 0,
                "buyBoxPer": 2.17,
                "id": null,
                "sku": "12",
                "brand": "NO",
                "sessions": 1,
                "brandName": "-",
                "isParent": false,
                "targetCurrency": null,
                "totalOrderItemsB2B": 0,
                "sessionPer": 0.01,
                "orderedProductSalesB2B": 0.0,
                "pageViews": 1,
                "countryName": "US",
                "parentAsin": "B07MD5CZKJ",
                "orderedProductSalesB2BAmountExportString": null,
                "orderedProductSalesAmountExportString": null,
                "lossTraffics": [
                    {
                        "parentAsin": "B07MD5CZKJ",
                        "marketName": "一号店--有广告数据:US",
                        "sessions": null,
                        "msku": null,
                        "pageViews": null,
                        "buyBoxPer": null,
                        "recordDate": "2023-02-15",
                        "asin": "BGJ0000043",
                        "countryId": null,
                        "marketId": 1
                    }
                ],
                "sellingManagerName": "积加测试用户2",
                "title": "Screen Protector Compatible iPad pro 11 inch, [Face ID Recognition] Tempered Glass Screen Protector iPad 2018 11 inch Anti-Fingerprint HD Scratch Resistance Film for Apple iPad Pro New by Greenlaw",
                "unitSessionPer": 0.0,
                "categoryName": "001-纯牛奶",
                "countryId": 1,
                "marketId": 1,
                "orderedProductSalesB2BAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "imageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                "recordDate": "2023-02-11",
                "productManagerName": "-",
                "orderedProductSales": 0.0,
                "orderedProductSalesAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "0"
                },
                "pageViewsPer": 0.0,
                "unitSessionPerB2B": 0.0,
                "asinUrl": "https://www.amazon.com/gp/product/BGJ0000043",
                "marketName": "一号店--有广告数据:US",
                "asin": "BGJ0000043",
                "category": "001",
                "unitsOrdered": 0
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 58. 采购/到库成本分析

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 采购/到库成本分析 |
| 请求地址 | `/finance/sts/profitCostAnalysis/page` |
| 请求方式 | POST |
| 限流规则 | 每 5秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| beginDate | date | 是 | 开始时间 [yyyy-MM-dd] |
| endDate | date | 是 | 结束时间 [yyyy-MM-dd] |
| currency | string | 否 | 币种 [参考Q&A-通用参数-币种] |
| costType | int | 否 | 成本类型 [0-销售成本，1-补回成本] |
| shippmentType | string | 否 | 配送方式 [FBA配送: AFN; 自发货: MFN] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| platformCodes | array<string> | 否 | 平台编码，默认亚马逊：AMAZON |
| costValues | int | 否 | 成本取值 [先进先出成本: 0; 月末加权平均成本: 1; 自定义成本: 2] |
| marketIds | array<int> | 否 | 站点ID |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page":1,
    "pagesize":10,
    "beginDate": "2020-08-01",
    "endDate": "2020-08-30"
}
```

### 响应示例

```json
{
    "traceId": "open_5cf483f6ba8e4db58fdedbef7a027214",
    "code": 200,
    "data": {
        "total": 443416,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "orderType": 0,
                "purchaseDate": "2020-08-30 11:30:36",
                "arriveCurrency": "USD",
                "orderId": "113-7194056-3074600",
                "marketCurrency": "",
                "arriveCost": -0.1906,
                "purchaseCurrency": "USD",
                "productName": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time",
                "marketId": 8,
                "updateBy": "",
                "costType": 0,
                "serialOutNum": "",
                "id": 1,
                "sku": "GJ ERP_TEST_SKU-335",
                "purchaseCost": -16.3134,
                "msku": "TEST_MSKU_GJ ERP-QWE312",
                "quantity": 1,
                "costGainType": 1,
                "arriveCostAmount": {
                    "currencyAmount": -0.19,
                    "currencySymbol": "",
                    "currencyCode": "",
                    "amountWithSymbol": "-0.19"
                },
                "updateTime": "2021-12-22T11:01:26.000+00:00",
                "purchaseCostAmount": {
                    "currencyAmount": -16.31,
                    "currencySymbol": "",
                    "currencyCode": "",
                    "amountWithSymbol": "-16.31"
                },
                "createBy": "",
                "settlementTime": "2020-08-31 05:35:13",
                "shippmentType": "AFN",
                "warehouseType": ""
            }
        ]
    },
    "messages": ["request.success"]
}
```

---

## 59. 销售表现

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 销售表现 |
| 请求地址 | `/operation/sts/salesAnalysis/page` |
| 请求方式 | POST |
| 限流规则 | 每 5秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| showCurrencyType | string | 是 | 显示币种，如原币种：YUAN，币种枚举查看QA说明 |
| beginDate | date | 是 | 开始时间，yyyy-MM-dd |
| endDate | date | 是 | 结束时间，yyyy-MM-dd |
| sku | string | 否 | sku |
| variationAsin | string | 否 | 父asin |
| productName | string | 否 | 产品名称 |
| asin | string | 否 | asin |
| msku | string | 否 | msku |
| page | number | 是 | 页码 |
| pagesize | number | 是 | 一页显示多少 |
| groupByType | string | 是 | 查询维度，msku：seller_sku、asin、父asin：variation_asin、sku、spu、国家：country、店铺：market |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | number | 是 | 响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20,
    "showCurrencyType": "USD",
    "isShowTotal": false,
    "groupByType":"asin",
    "beginDate":"2022-09-07",
    "endDate":"2022-09-08"
}
```

### 响应示例

```json
{}
```

---

## 60. 查询产品列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询产品列表 |
| 请求地址 | `/purchase/goods/product/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| categoryList | array<string> | 否 | 品类资料表编码 |
| pageInfo | object | 否 | 分页对象，直接分页与分页对象必须传一种 |
| page | int | 否 | 页码，直接分页与分页对象必须传一种 |
| pagesize | int | 否 | 每页条数 [最大100条/页] |
| skuList | array<string> | 否 | skuList |
| platformMskuList | array<string> | 否 | 多平台MSKU |
| mskuList | array<string> | 否 | 亚马逊MSKU |
| state | int | 否 | 状态 [0-正常，1-停用] |
| dateType | int | 否 | 时间类型 [0-创建时间，1-更新时间] |
| startDate | date | 否 | 开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 结束时间 [yyyy-MM-dd] |
| brandList | array<string> | 否 | 品牌资料表编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "skuList": ["alypushtest"]
}
```

### 响应示例

```json
{
    "traceId": "open_dd493ed85c054b11970d351b40ba386f",
    "code": 200,
    "data": {
        "total": 1,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "productDeliveryDays": 6,
                "packageH": 4.0,
                "packageWeight": 5.0,
                "pasteAttribute": false,
                "packageL": 2.0,
                "productManagerAccount": "****",
                "packageW": 3.0,
                "quote": 7.0,
                "property": "0",
                "productUsage": "",
                "id": 12170,
                "state": 0,
                "sku": "alypushtest",
                "brand": "",
                "assemblyPackage": "",
                "singleProductSizeH": 8.0,
                "singleProductSizeL": 8.0,
                "briefName": "简称啊啊啊",
                "purchaseAccount": "***",
                "singleProductSizeW": 8.0,
                "magneticAttribute": false,
                "mskuList": [
                    "alypushtest",
                    "alypushtestmsku35",
                    "alypushtestmsku36",
                    "alypushtestmsku37",
                    "alypushtestmsku38",
                    "alypushtestmsku39",
                    "alypushtestmsku40",
                    "alypushtestmsku41",
                    "alypushtestmsku411",
                    "alypushtestmsku412",
                    "alypushtestmsku415",
                    "alypushtestmsku445",
                    "alypushtestmsku4487",
                    "alypushtestmsku4517",
                    "alypushtestmsku6667"
                ],
                "customsCode": "55",
                "spuName": null,
                "woodenAttribute": false,
                "assembly": null,
                "assemblyLaborCost": null,
                "pmsMskuDTOS": [
                    {
                        "msku": "alypushtestmsku6667",
                        "shopName": null,
                        "memo": "推送啊啊",
                        "platformId": "AMAZON",
                        "warehouseId": 42,
                        "recordDate": "2023-07-19 19:03:32",
                        "shopId": null,
                        "platformName": "Amazon"
                    }
                ],
                "purchaseAccountId": 13,
                "addDate": "2023-07-19 11:23:56",
                "englishCustomsName": "552",
                "powderAttribute": false,
                "liquidAttribute": false,
                "singleProductNetWeight": 9.0,
                "productTypeName": "成品",
                "lastDate": "2023-07-19 19:03:31",
                "brandName": "-",
                "smallImageUrl": "",
                "unit": "个",
                "name": "*********",
                "batteryAttribute": true,
                "spu": null,
                "clothing": true,
                "chargedAttribute": false,
                "description": "0",
                "remark": "ddd",
                "title": "0",
                "categoryName": "aly4_2-第三级品类_页面新增",
                "quoteAmount": {
                    "currencyAmount": 7.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥7.0000"
                },
                "chineseCustomsName": "55",
                "productType": 0,
                "purchase": 1,
                "isInspection": 0,
                "specification": "0",
                "material": "",
                "transferGroup": "1212",
                "category": "aly4_2",
                "productManagerAccountId": 5
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 61. 查询产品详情

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询产品详情 |
| 请求地址 | `/purchase/goods/product/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| id | long | 是 | 产品ID |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | number | 否 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | null | 否 | 接口返回traceId |

### 请求示例

```json
{
    "id": 12170
}
```

### 响应示例

```json
{
    "traceId": "open_503f38d36b764908937c82ff4f79c33b",
    "code": 200,
    "data": {
        "assemblyForbidInfo": null,
        "productVoInfo": {
            "productDeliveryDays": 6,
            "packageH": 4.0,
            "packageWeight": 5.0,
            "pasteAttribute": false,
            "packageL": 2.0,
            "productManagerAccount": "***",
            "moq": null,
            "estimatedAssemblyDays": null,
            "packageW": 3.0,
            "quote": 7.0,
            "property": "0",
            "productUsage": "",
            "id": 12170,
            "state": 0,
            "sku": "alypushtest",
            "brand": "",
            "dutyPrice": null,
            "assemblyPackage": "",
            "singleProductSizeH": 8.0,
            "singleProductSizeL": 8.0,
            "briefName": "简称啊啊啊",
            "purchaseAccount": "***",
            "recordAccountId": 1,
            "singleProductSizeW": 8.0,
            "magneticAttribute": false,
            "customsCode": "55",
            "spuName": null,
            "namePrint": "",
            "assembly": null,
            "assemblyLaborCost": null,
            "purchaseAccountId": 13,
            "levelName": "爆品",
            "addDate": "2023-07-19 11:23:56",
            "assembleParentId": null,
            "englishCustomsName": "552",
            "euFreightEvaluate": {
                "ukToFrFee": {
                    "currencyAmount": 3.9,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€3.90"
                },
                "ukLocalFee": {
                    "currencyAmount": 1.64,
                    "currencySymbol": "￡",
                    "currencyCode": "GBP",
                    "amountWithSymbol": "￡1.64"
                },
                "flLocalFee": {
                    "currencyAmount": 1.81,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€1.81"
                },
                "frAmazonEuFee": {
                    "currencyAmount": 2.62,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€2.62"
                },
                "volumeWeight": 4.8,
                "seEuFee": {
                    "currencyAmount": 48.62,
                    "currencySymbol": "Kr",
                    "currencyCode": "SEK",
                    "amountWithSymbol": "Kr48.62"
                },
                "frEuFee": {
                    "currencyAmount": 4.88,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€4.88"
                },
                "plLocalFee": {
                    "currencyAmount": 4.53,
                    "currencySymbol": "zł",
                    "currencyCode": "PLN",
                    "amountWithSymbol": "zł4.53"
                },
                "ukEuFee": null,
                "plAmazonEuFee": {
                    "currencyAmount": 4.53,
                    "currencySymbol": "zł",
                    "currencyCode": "PLN",
                    "amountWithSymbol": "zł4.53"
                },
                "ukToEuFee": {
                    "currencyAmount": 3.79,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€3.79"
                },
                "esAmazonEuFee": {
                    "currencyAmount": 2.65,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€2.65"
                },
                "ukAmazonEuFee": {
                    "currencyAmount": 1.64,
                    "currencySymbol": "￡",
                    "currencyCode": "GBP",
                    "amountWithSymbol": "￡1.64"
                },
                "plEuFee": {
                    "currencyAmount": 20.91,
                    "currencySymbol": "zł",
                    "currencyCode": "PLN",
                    "amountWithSymbol": "zł20.91"
                },
                "height": 4,
                "itLocalFee": {
                    "currencyAmount": 3.0,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€3.00"
                },
                "frLocalFee": {
                    "currencyAmount": 2.62,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€2.62"
                },
                "length": 2,
                "weight": 5,
                "deLocalFee": {
                    "currencyAmount": 1.98,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€1.98"
                },
                "flAmazonEuFee": {
                    "currencyAmount": 1.81,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€1.81"
                },
                "firstLevelName": "标准尺寸",
                "seLocalFee": {
                    "currencyAmount": 26.76,
                    "currencySymbol": "Kr",
                    "currencyCode": "SEK",
                    "amountWithSymbol": "Kr26.76"
                },
                "seAmazonEuFee": {
                    "currencyAmount": 26.76,
                    "currencySymbol": "Kr",
                    "currencyCode": "SEK",
                    "amountWithSymbol": "Kr26.76"
                },
                "secondLevelName": "标准信封",
                "esLocalFee": {
                    "currencyAmount": 2.65,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€2.65"
                },
                "deAmazonEuFee": {
                    "currencyAmount": 1.98,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€1.98"
                },
                "nonUkEuFee": {
                    "currencyAmount": 4.74,
                    "currencySymbol": "￡",
                    "currencyCode": "GBP",
                    "amountWithSymbol": "￡4.74"
                },
                "deliveryWeight": 5,
                "width": 3,
                "euToUkFee": {
                    "currencyAmount": 3.46,
                    "currencySymbol": "￡",
                    "currencyCode": "GBP",
                    "amountWithSymbol": "￡3.46"
                },
                "itAmazonEuFee": {
                    "currencyAmount": 3.0,
                    "currencySymbol": "€",
                    "currencyCode": "EUR",
                    "amountWithSymbol": "€3.00"
                }
            },
            "powderAttribute": false,
            "productCustomsVos": [
                {
                    "customsClearTax": 5.0,
                    "defaultFlag": 0,
                    "productId": 12170,
                    "customsClearCode": "55",
                    "dutyCurrency": "CNY",
                    "id": 17115,
                    "nationaCustoms": [
                        "ALL"
                    ],
                    "dutyPrice": 555.0
                }
            ],
            "dataPermission": [],
            "warrantyTime": null,
            "completeState": 0,
            "liquidAttribute": false,
            "singleProductNetWeight": 9.0,
            "lastDate": "2023-08-25 14:40:46",
            "brandName": "-",
            "smallImageUrl": "",
            "level": 3,
            "usFreightEvaluate": {
                "sizeType": "大号标准",
                "heightInch": 0.79,
                "freight": {
                    "currencyAmount": 4.43,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$4.43"
                },
                "length": 2,
                "weight": 5,
                "deliveryWeightOunce": 0.18,
                "volumeWeight": 0.17,
                "weightOunce": 0.18,
                "width": 3,
                "widthInch": 1.18,
                "clothing": true,
                "lengthInch": 1.57,
                "height": 4
            },
            "unit": "个",
            "dutyCurrency": null,
            "name": "*****",
            "batteryAttribute": true,
            "spu": null,
            "clothing": true,
            "chargedAttribute": false,
            "wayOfPacking": "0",
            "description": "0",
            "remark": "ddd",
            "title": "0",
            "categoryName": "aly4_2-第三级品类_页面新增",
            "chineseCustomsName": "55",
            "productType": 0,
            "manufacturingCountry": "",
            "productCartonVos": [
                {
                    "defaultFlag": 0,
                    "productId": 12170,
                    "cartonSizeW": 9.0,
                    "singleQuantity": 7,
                    "singleNetWeight": 7.0,
                    "cartonSizeH": 9.0,
                    "id": 19863,
                    "singleWeight": 7.0,
                    "cartonSizeL": 9.0,
                    "nationaCarton": [
                        "ALL"
                    ]
                }
            ],
            "purchase": 1,
            "isInspection": 0,
            "specification": "0",
            "material": "",
            "transferGroup": "1212",
            "countryOfOrigin": null,
            "category": "aly4_2",
            "productManagerAccountId": 5
        },
        "productImg": null,
        "productMsku": [
            {
                "msku": "alypushtestmsku6667",
                "warehouseId": 42,
                "memo": "推送啊啊",
                "recordDate": "2023-07-19 19:03:32",
                "id": 8124,
                "sku": "alypushtest",
                "warehouseName": "**********",
                "account": "admin"
            }
        ],
        "productAssembly": null,
        "id": 12170,
        "productPackage": null,
        "allPlatformMsku": [
            {
                "platformMskuUpdateVOS": [
                    {
                        "msku": "123123",
                        "memo": null,
                        "recordDate": "2023-08-25 14:40:44",
                        "id": 12,
                        "platformId": 1,
                        "sku": "alypushtest",
                        "shopAndCountryList": [
                            {
                                "country": "US",
                                "shopAndCountry": "***********",
                                "shopName": null,
                                "shopId": 1523483286158598145,
                                "shopIdStr": "1523483286158598145"
                            }
                        ],
                        "account": "admin",
                        "status": 1
                    }
                ],
                "platformId": 1
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 62. 查询SKU关联亚马逊MSKU

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询SKU关联亚马逊MSKU |
| 请求地址 | `/purchase/goods/amazonMsku/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| endDate | datetime | 否 | 查询结束时间 [yyyy-MM-dd HH:mm:ss] |
| page | int | 否 | 第几页 |
| pagesize | int | 否 | 每页显示多少条 [最大值：100] |
| startDate | datetime | 否 | 查询开始时间 [yyyy-MM-dd HH:mm:ss] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 追踪id |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
   "page": 1,
   "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_6cd8eb22f2144fcdb7da7b5ee060544d",
    "code": 200,
    "data": {
        "total": 6196,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "msku": "Mondjaaaalyimport83",
                "memo": "",
                "warehouseId": 445,
                "recordDate": "2023-11-28 18:14:23",
                "sku": "mondjaaaalyimport83"
            }
        ]
    },
    "messages": []
}
```

---

## 63. 查询品类信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询品类信息 |
| 请求地址 | `/purchase/goods/category/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| valueList | array<string> | 否 | 品类编码集合 |
| state | string | 否 | 状态 [Active-启用，Inactive-停用] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| messages | array<string> | 是 | 提示信息 |
| traceId | string | 是 | 接口返回traceId |
| data | object | 否 | 接口返回数据 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "total": 136,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "name": "苹果不锈钢三珠",
                "memo": "苹果不锈钢三珠",
                "parentCategory": "",
                "state": "Active",
                "value": "SSOyster"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 64. 录入品类信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 录入品类信息 |
| 请求地址 | `/purchase/goods/category/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| parentCategory | string | 否 | 父品类编码 |
| name | string | 是 | 名称 |
| state | string | 是 | 状态 [Active-启用，Inactive-停用] |
| memo | string | 否 | 描述 |
| value | string | 是 | 编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| data | object | 否 | 接口返回数据 |

### 请求示例

```json
{
    "value": "open-test2",
    "name": "开放平台测试3",
    "state": "Active",
    "memo": "测试"
}
```

### 响应示例

```json
{
    "traceId": "open_e8b7c16eb9de4f25926e455141c6b7ad",
    "code": 200,
    "data": {
        "marketNames": null,
        "name": "开放平台测试3",
        "memo": "测试",
        "parentCategory": "",
        "id": 146,
        "state": "Active",
        "value": "open-test2",
        "marketList": null
    },
    "messages": []
}
```

---

## 65. 修改品类信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 修改品类信息 |
| 请求地址 | `/purchase/goods/category/update` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| name | string | 是 | 名称 |
| state | string | 是 | 状态 [Active-启用，Inactive-停用] |
| memo | string | 否 | 描述 |
| parentCategory | string | 否 | 父品类编码 |
| value | string | 是 | 品类编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| messages | array<object> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| data | object | 否 | 接口返回数据 |

### 请求示例

```json
{
    "value": "open-test2",
    "name": "开放平台测试332",
    "state": "Active",
    "memo": "测试"
}
```

### 响应示例

```json
{
    "traceId": "open_22346a9f58ba46eab7104fe7e7cfc0f3",
    "code": 200,
    "data": {
        "marketNames": null,
        "name": "开放平台测试33",
        "memo": "测试",
        "parentCategory": "",
        "id": 117,
        "state": "Active",
        "value": "1",
        "marketList": null
    },
    "messages": []
}
```

---

## 66. 新增产品资料

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 新增产品资料 |
| 请求地址 | `/purchase/goods/product/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| productCartons | array<object> | 否 | 装箱信息 |
| productCustoms | array<object> | 否 | 清关信息 |
| productImage | object | 否 | 产品图片 |
| productMskus | array<object> | 否 | 亚马逊关联MSKU |
| productPlatformMskus | array<object> | 否 | 多平台关联MSKU |
| product | object | 是 | 产品资料基础类 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 跟踪号 |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "product": {
        "category": "open-test2",
        "isInspection": 0,
        "name": "EoLink-新增-SKU001",
        "packageH": 1,
        "packageL": 1,
        "packageW": 1,
        "packageWeight": 1,
        "productDeliveryDays": "1",
        "productType": 0,
        "purchase": 0,
        "purchaseAccountId": 10,
        "sku": "EoLink-New-SKU001",
        "smallImageUrl": "https://gerposs.app.gerpgo.com/public/522/20221122/9dbed94ead014fefa57b091babe51077/001932-1667146772b316.jpg",
        "state": 0,
        "unit": "双"
    },
    "productImage": {
        "sku": "EoLink-New-SKU001",
        "attachImageIdList": ["3995"]
    },
    "productMskus":[]
}
```

### 响应示例

```json
{
    "traceId": "open_27d43f79e875421a9bb7b2401c177362",
    "code": 200,
    "data": null,
    "messages": [
        "新增成功"
    ]
}
```

---

## 67. 修改产品资料

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 修改产品资料 |
| 请求地址 | `/purchase/goods/product/update` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| productCartons | array<object> | 否 | 装箱信息 |
| productCustoms | array<object> | 否 | 清关信息 |
| productImage | object | 否 | 产品图片 |
| productMskus | array<object> | 否 | 亚马逊关联MSKU |
| productPlatformMskus | array<object> | 否 | 多平台关联MSKU |
| product | object | 是 | 产品资料基础类 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 跟踪号 |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "product": {
        "category": "open-test2",
        "isInspection": 0,
        "name": "EoLink-新增-SKU001",
        "packageH": 1,
        "packageL": 1,
        "packageW": 1,
        "packageWeight": 1,
        "productDeliveryDays": "1",
        "productType": 0,
        "purchase": 0,
        "purchaseAccountId": 10,
        "sku": "EoLink-New-SKU001",
        "smallImageUrl": "https://gerposs.app.gerpgo.com/public/522/20221122/9dbed94ead014fefa57b091babe51077/001932-1667146772b316.jpg",
        "state": 0,
        "unit": "双"
    },
    "productImage": {
        "sku": "EoLink-New-SKU001",
        "attachImageIdList": ["3995"]
    },
    "productMskus":[]
}
```

### 响应示例

```json
{
    "traceId": "open_27d43f79e875421a9bb7b2401c177362",
    "code": 200,
    "data": null,
    "messages": [
        "更新成功"
    ]
}
```

---

## 68. 录入父产品信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 录入父产品信息 |
| 请求地址 | `/purchase/goods/parentProduct/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| name | string | 是 | 父产品名称 |
| code | string | 是 | spu |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| data | object | 否 | 接口返回数据 |

### 请求示例

```json
{
    "code": "parent-test2",
    "name": "开放平台测试332"
}
```

### 响应示例

```json
{
    "traceId": "open_f913766baf314fa4ab4df3870d6f2fd8",
    "code": 200,
    "data": null,
    "messages": [
        "request.success"
    ]
}
```

---

## 69. 查询捆绑产品列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询捆绑产品列表 |
| 请求地址 | `/purchase/goods/kbProduct/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| skuName | string | 否 | 捆绑产品sku名称模糊查询 |
| relSku | string | 否 | 捆绑产品的关联sku模糊查询 |
| relSkuName | string | 否 | 捆绑产品的关联sku名称模糊查询 |
| msku | string | 否 | msku模糊查询 |
| createStartTime | date | 否 | 创建时间查询开始时间 [yyyy-MM-dd] |
| createEndTime | date | 否 | 创建时间查询结束时间 [yyyy-MM-dd] |
| updateStartTime | date | 否 | 更新时间查询开始时间 [yyyy-MM-dd] |
| updateEndTime | date | 否 | 更新时间查询结束时间 [yyyy-MM-dd] |
| createId | long | 否 | 创建人ID |
| updateId | long | 否 | 更新人ID |
| categoryList | array<string> | 否 | 品类列表 |
| page | int | 是 | 第几页 |
| pagesize | int | 是 | 每页显示多少条 [最大值：100] |
| sku | string | 否 | 捆绑产品sku模糊查询 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 追踪id |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_247ed3ebfa9d4ecebb527862c4c7998a",
    "code": 200,
    "data": {
        "total": 2,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "smallImageUrl": "",
                "skuRelVOList": [
                    {
                        "quantity": 1,
                        "smallImageUrl": "",
                        "productTypeName": "成品",
                        "id": 7,
                        "relSkuName": "GMAX 车身-YXSBG001",
                        "relSku": "YXSBG001",
                        "productType": 0
                    },
                    {
                        "quantity": 1,
                        "smallImageUrl": "",
                        "productTypeName": "成品",
                        "id": 6,
                        "relSkuName": "GMAX屏幕YXSBG001B",
                        "relSku": "YXSBG001B",
                        "productType": 0
                    }
                ],
                "description": "",
                "updateTime": "2023-06-09 17:36:31",
                "categoryName": "B-动感单车",
                "updateName": "demoC1139",
                "updateId": 13731,
                "createTime": "2023-06-09 17:36:31",
                "createId": 13731,
                "name": "G1MAX动感单车",
                "id": 4,
                "sku": "YXSBGMAX001",
                "category": "B",
                "createName": "demoC1139",
                "mskuRelVOList": [
                    {
                        "country": "Global",
                        "shopName": "shopify-gg3355",
                        "memo": "",
                        "id": 4,
                        "platformId": "SHOPIFY",
                        "shopId": "1584461959666221159",
                        "relMsku": "YXSBGMAX001"
                    }
                ]
            }
        ]
    },
    "messages": []
}
```

---

## 70. 查询品牌资料

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询品牌资料 |
| 请求地址 | `/purchase/goods/brand/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| name | string | 否 | 品牌名称模糊查询 |
| state | string | 否 | 状态 [Active-启用，Inactive-停用] |
| page | int | 是 | 第几页 |
| pagesize | int | 是 | 每页显示多少条 |
| code | string | 否 | 品牌编码模糊查询 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 链路追踪id |
| data | object | 否 | 返回结果 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_089b89be38bc4d18b602d88dcb8a374b",
    "code": 200,
    "data": {
        "total": 32,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "code": "FF111",
                "name": "FF111",
                "memo": null,
                "id": 32,
                "state": "Active"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 71. 保存品牌资料

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 保存品牌资料 |
| 请求地址 | `/purchase/goods/brand/save` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| name | string | 是 | 品牌名称 |
| state | string | 是 | 状态 [Active-启用，Inactive-停用] |
| memo | string | 否 | 描述 |
| code | string | 是 | 品牌编码 [通过品牌编码判断新增还是更新] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 链路追踪id |
| data | object | 否 | 返回结果 |

### 请求示例

```json
{
    "code": "jijiatest",
    "name": "积加test01",
    "state": "Active",
    "memo": "测试"
}
```

### 响应示例

```json
{
    "traceId": "open_97da35f94370425385ead06efe5b7d2d",
    "code": 200,
    "data": null,
    "messages": [
        "更新成功！"
    ]
}
```

---

## 72. 同步产品到仓库

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 同步产品到仓库 |
| 请求地址 | `/purchase/base/productToStore/sync` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| warehouseIds | array<int> | 是 | 仓库ids |
| self | boolean | 否 | 是否自营仓 |
| supplier | boolean | 否 | 是否供应商仓 |
| productIds | array<int> | 是 | 产品ids |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 返回提示消息 |
| traceId | string | 否 | 返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "productIds":[1],
    "warehouseIds":[1]
}
```

### 响应示例

```json
{
    "traceId": "open_132f0f0fe8974d31b7c91342a3e1fb56",
    "code": 200,
    "data": null,
    "messages": [
        "同步产品到仓库成功"
    ]
}
```

---

## 73. 查询SKU关联多平台MSKU

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询SKU关联多平台MSKU |
| 请求地址 | `/platform/base/platformMsku/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| platformIdList | array<string> | 否 | 取值参考 [Q&A-通用参数-多平台编码] |
| skuType | string | 否 | sku类型 [NORMAL-产品资料sku（默认），KB-捆绑sku] |
| startTime | string | 否 | 开始时间(yyyy-MM-dd HH:mm:ss) |
| endTime | string | 否 | 结束时间(yyyy-MM-dd HH:mm:ss) |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_47fc149524164befa3951f2291efc191",
    "code": 200,
    "data": {
        "total": 12,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "country": "US",
                "msku": "123123",
                "memo": null,
                "platformId": "WALMART",
                "skuType": "NORMAL",
                "recordDate": "2023-08-25 14:40:44",
                "shopId": "1523483286158598145",
                "sku": "alypushtest",
                "platformName": "Walmart"
            }
        ]
    },
    "messages": []
}
```

---

## 74. 查询父产品信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询父产品信息 |
| 请求地址 | `/purchase/goods/parentProduct/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页面 |
| pagesize | int | 是 | 页大小 |
| updateEndTime | string | 否 | 更新时间止 |
| updateStartTime | string | 否 | 更新时间起 |
| code | string | 否 | SPU编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{"page":1,"pagesize":100}
```

### 响应示例

```json
{}
```

---

## 75. 添加变体属性

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 添加变体属性 |
| 请求地址 | `/purchase/goods/attribute/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| attributeName | string | 是 | 属性名(唯一) |
| attributeItemCreateDTOS | array<object> | 是 | 属性明细集合 |
| id | long | 否 | id,更新需要传入 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | string | 否 | 返回数据，根据响应码判断是否成功 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{}
```

---

## 76. 查询变体属性

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询变体属性 |
| 请求地址 | `/purchase/goods/attribute/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 3次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| attributeName | string | 是 | 属性名 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{}
```

---

## 77. 关联产品变体属性

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 关联产品变体属性 |
| 请求地址 | `/purchase/goods/attributeSku/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| openParamArray | array<object> | 是 | 数据集 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | boolean | 否 | 是否成功 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{}
```

---

## 78. 查询产品库存

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询产品库存 |
| 请求地址 | `/purchase/store/inventory/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页大小[最大100条/页] |
| productState | int | 否 | 产品状态 [0-正常，1-停用] |
| productTypeList | array<int> | 否 | 产品类型 [0-成品，1-包材，2-组合产品，3-半成品] |
| state | int | 否 | 商品状态 [0-异常，1-正常] |
| warehouseIds | array<long> | 否 | 仓库id集合 |
| productManagerAccountIdList | array<int> | 否 | 产品负责人id集合 |
| skuList | array<string> | 否 | sku集合 [最大50条] |
| asinList | array<string> | 否 | asin集合 [最大50条] |
| mskuList | array<string> | 否 | msku集合 [最大50条] |
| filterQuantity | boolean | 否 | 过滤所有库存指标数据为0 |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20
}
```

### 响应示例

```json
{
    "traceId": "open_da2f920757ea4bf999844a8a6da34656",
    "code": 200,
    "data": {
        "total": 40454,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "countryListingLevelsStr": "-",
                "skuImageUrl": "",
                "productDeliveryDays": 22,
                "unsalableAmount": 0,
                "ps": 0.0,
                "fnsku": "",
                "addTime": "2022-11-25 13:38:51",
                "inboundWorking": 0,
                "reservedQuantity": 0,
                "erpInboundWorking": 0,
                "erpInboundReceiving": 0,
                "lnQuantity": 0,
                "shippedTurnover": 0.0,
                "inventoryAge9to12Month": 0,
                "arrivedCost": 0.0,
                "overseasQuantity": 0,
                "stateName": "正常",
                "fbaWarehouse": false,
                "computePses": "",
                "productTypeName": "成品",
                "defectiveQuantity": 0,
                "id": 40238,
                "state": 1,
                "sku": "00001",
                "brand": "NO",
                "reservedProcessed": 0,
                "countryListingStates": [],
                "brandName": "-",
                "msku": "00001",
                "inventoryTotalAmount": 0.0,
                "productId": 1134,
                "assemblyRule": "",
                "inboundQuantity": 0,
                "reservedFCTransfer": 0,
                "totalTurnover": 0.0,
                "inventoryAge1to2Month": 0,
                "productState": 0,
                "sum7ps": 0,
                "unit": "件",
                "fbaInboundQuantity": 0,
                "warehouseId": 1,
                "purchaseQuantity": 0,
                "inventoryAge0to1Month": 0,
                "poQuantity": 0,
                "warehouseType": "SELF",
                "inboundAmount": 0.0,
                "computeYesterday9Pses": "0,0,0,0,0,0,0",
                "sum30ps": 0,
                "updateDate": 1674102040551,
                "reservedUntreated": 0,
                "inventoryAge3to6Month": 0,
                "inventoryAge2to3Month": 0,
                "inventoryQuantity": 0,
                "warehouseName": "CN_GJ1",
                "categoryName": "001-纯牛奶",
                "skuName": "纯牛奶",
                "reservedFCProcessing": 0,
                "inventoryAge12MonthUp": 0,
                "sum15ps": 0,
                "countryListingStatesStr": "-",
                "waitInboundAmount": 0.0,
                "goodAvailableQuantity": 0,
                "childQuantity": 0,
                "turnover": 0.0,
                "productType": 0,
                "inventoryAge0to3Month": 0,
                "availableQuantity": 0,
                "inventoryAmount": 0.0,
                "unsalableQuantity": 0,
                "purchaseCost": 0.0,
                "unsalableRate": 0,
                "warehouseCountry": "CN",
                "plQuantity": 0,
                "reservedCustomerOrders": 0,
                "erpInboundShipped": 0,
                "onInventoryAmount": 0.0,
                "updateTime": "2023-01-19 12:20:40",
                "inboundShipped": 0,
                "addDate": 1669354731508,
                "productStateName": "正常",
                "countryListingLevels": [],
                "defectiveAmount": 0.0,
                "inventoryAge6to9Month": 0,
                "asin": "",
                "category": "001",
                "erpInboundWaitShipped": 0,
                "inboundReceiving": 0,
                "erpInbound": true,
                "productManagerAccountId": 0
            }
        ]
    },
    "messages": ["请求成功"]
}
```

---

## 79. 查询调拨单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询调拨单列表 |
| 请求地址 | `/fulfillment/inventory/transfer/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| codeList | array<string> | 否 | 单号 |
| createDateEnd | date | 否 | 创建时间结束 [yyyy-MM-dd] |
| createDateStart | date | 否 | 创建时间开始 [yyyy-MM-dd] |
| flag | int | 否 | 出库 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| pick | int | 否 | 拣货，0：未拣货，1：已拣货，2：拣货中 |
| status | string | 否 | 状态 [audit-审核中，wait_audit-审核驳回，approve-审核通过，on_the_way-调拨在途，finish-已完成，cancelled-已作废，processingStatus-进行中，draft-草稿] |
| statusList | array<string> | 否 | 状态集合 |
| updateTimeEnd | datetime | 否 | 结束更新时间 [yyyy-MM-dd HH:mm:ss] |
| updateTimeStart | datetime | 否 | 起始更新时间 [yyyy-MM-dd HH:mm:ss] |
| warehouseIds | array<long> | 否 | 调出仓库 |
| actualDeliveryDateStart | date | 否 | 实际出库日期开始 [yyyy-MM-dd] |
| actualDeliveryDateEnd | date | 否 | 实际出库日期结束 [yyyy-MM-dd] |
| executorDateStart | date | 否 | 操作出库日期开始 [yyyy-MM-dd] |
| executorDateEnd | date | 否 | 操作出库日期结束 [yyyy-MM-dd] |
| pickTimeStart | date | 否 | 拣货完成时间开始[yyyy-MM-dd] |
| pickTimeEnd | date | 否 | 拣货完成时间结束[yyyy-MM-dd] |
| arrivalWarehouseIds | array<long> | 否 | 调入仓库 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page":1,
    "pagesize":10
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "total": 2547,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "totalVolume": 0.18144,
                "cartonTotalWeight": 0.0,
                "transportName": "空运1",
                "totalPriceAmount": {
                    "currencyAmount": 18846.8,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥18846.80"
                },
                "memo": "gj test memo",
                "totalQuantity": 280,
                "pick": 0,
                "executor": "积加测试用户11",
                "id": 1,
                "verificationResults": "已作废",
                "printListFlag": "",
                "arrivalWarehouseId": 12,
                "pickName": "未拣货",
                "printListFlagName": "",
                "fbaArrivalWarehouseFlag": true,
                "packages": 14,
                "warehouseId": 1,
                "flagName": "未出库",
                "detail": [
                    {
                        "fid": 1,
                        "fnsku": "FNGJX0000303",
                        "pickQuantity": 0,
                        "singleQuantity": 20.0,
                        "locationDetailsJson": "",
                        "volumeWeight": 0.108,
                        "viewPs28": 0.0,
                        "viewAvailableQuantity": 0,
                        "price": 67.31,
                        "viewTotalTurnover": 0.0,
                        "productTypeName": "成品",
                        "id": 1,
                        "state": 1,
                        "arrivalWarehouseId": 12,
                        "cartonSizeW": 28.5,
                        "inboundQuantity": 0,
                        "weight": 0.776,
                        "viewPurchaseQuantity": 0,
                        "viewProductManagerAccountId": 0,
                        "volume": 6.48E-4,
                        "unit": "",
                        "warehouseId": 1,
                        "viewPlanQuantity": 0,
                        "cartonSizeH": 21.0,
                        "viewPs7": 0.0,
                        "cartonSizeL": 59.5,
                        "reducePackage": false,
                        "isLockMarket": false,
                        "viewWarehouseTurnover": 0.0,
                        "totalPrice": 67.31,
                        "arriveCost": 0.0,
                        "diffQuantity": 0,
                        "baseCurrencySymbol": "￥",
                        "packageRule": "",
                        "marketId": 0,
                        "tfCode": "",
                        "skuName": "积加ERP测试产品485711077",
                        "viewShippedTurnover": 0.0,
                        "specialProperties": "",
                        "assemblyCode": "",
                        "imageUrl": "https://img.app.gerpgo.com/demo%2F2022%2F08%2Fattachments%2Fdemo%2F1660703536294a49cb857de5a40f9a193138bd80c8a75_origin_img_v2_393eebf0-88dc-46ab-9844-a8fded06555g.png",
                        "skuNamePrint": "积加ERP测试产品485711077",
                        "currency": "USD",
                        "sellerSku": "TEST_MSKU_GJ ERP-QWE1918",
                        "arrivalMarketId": 0,
                        "singleWeight": 14.1,
                        "productType": 0,
                        "viewLotNoQuantity": 0,
                        "viewProductManagerAccount": "system",
                        "product": "GJ ERP_TEST_SKU-241",
                        "purchaseCost": 67.31,
                        "quantity": 80,
                        "shipmentQuantity": 0,
                        "viewDeliveryDay": 0,
                        "arriveCostUsd": 0.0,
                        "viewPs14": 0.0,
                        "marketName": "共享",
                        "viewPurchaseShippedQuantity": 0,
                        "asin": "BGJ0000416",
                        "viewUnsalableQuantity": 0
                    },
                    {
                        "fid": 1,
                        "fnsku": "FNGJX0000304",
                        "pickQuantity": 0,
                        "singleQuantity": 20.0,
                        "locationDetailsJson": "",
                        "volumeWeight": 0.108,
                        "viewPs28": 0.0,
                        "viewAvailableQuantity": 0,
                        "price": 67.31,
                        "viewTotalTurnover": 0.0,
                        "productTypeName": "成品",
                        "id": 2,
                        "state": 1,
                        "arrivalWarehouseId": 12,
                        "cartonSizeW": 28.5,
                        "inboundQuantity": 0,
                        "weight": 0.776,
                        "viewPurchaseQuantity": 0,
                        "viewProductManagerAccountId": 0,
                        "volume": 6.48E-4,
                        "unit": "",
                        "warehouseId": 1,
                        "viewPlanQuantity": 0,
                        "cartonSizeH": 21.0,
                        "viewPs7": 0.0,
                        "cartonSizeL": 59.5,
                        "reducePackage": false,
                        "isLockMarket": false,
                        "viewWarehouseTurnover": 0.0,
                        "totalPrice": 67.31,
                        "arriveCost": 0.0,
                        "diffQuantity": 0,
                        "baseCurrencySymbol": "￥",
                        "packageRule": "",
                        "marketId": 0,
                        "tfCode": "",
                        "skuName": "积加ERP测试产品407118911",
                        "viewShippedTurnover": 0.0,
                        "specialProperties": "",
                        "assemblyCode": "",
                        "imageUrl": "https://img.app.gerpgo.com/demo%2F2022%2F08%2Fattachments%2Fdemo%2F1660703536294a49cb857de5a40f9a193138bd80c8a75_origin_img_v2_393eebf0-88dc-46ab-9844-a8fded06555g.png",
                        "skuNamePrint": "积加ERP测试产品407118911",
                        "currency": "USD",
                        "sellerSku": "TEST_MSKU_GJ ERP-QWE162",
                        "arrivalMarketId": 0,
                        "singleWeight": 14.1,
                        "productType": 0,
                        "viewLotNoQuantity": 0,
                        "viewProductManagerAccount": "system",
                        "product": "GJ ERP_TEST_SKU-240",
                        "purchaseCost": 67.31,
                        "quantity": 100,
                        "shipmentQuantity": 0,
                        "viewDeliveryDay": 0,
                        "arriveCostUsd": 0.0,
                        "viewPs14": 0.0,
                        "marketName": "共享",
                        "viewPurchaseShippedQuantity": 0,
                        "asin": "BGJ0000306",
                        "viewUnsalableQuantity": 0
                    },
                    {
                        "fid": 1,
                        "fnsku": "FNGJX0000301",
                        "pickQuantity": 0,
                        "singleQuantity": 20.0,
                        "locationDetailsJson": "",
                        "volumeWeight": 0.108,
                        "viewPs28": 0.0,
                        "viewAvailableQuantity": 0,
                        "price": 67.31,
                        "viewTotalTurnover": 0.0,
                        "productTypeName": "成品",
                        "id": 3,
                        "state": 1,
                        "arrivalWarehouseId": 12,
                        "cartonSizeW": 28.5,
                        "inboundQuantity": 0,
                        "weight": 0.776,
                        "viewPurchaseQuantity": 0,
                        "viewProductManagerAccountId": 0,
                        "volume": 6.48E-4,
                        "unit": "",
                        "warehouseId": 1,
                        "viewPlanQuantity": 0,
                        "cartonSizeH": 21.0,
                        "viewPs7": 0.0,
                        "cartonSizeL": 59.5,
                        "reducePackage": false,
                        "isLockMarket": false,
                        "viewWarehouseTurnover": 0.0,
                        "totalPrice": 67.31,
                        "arriveCost": 0.0,
                        "diffQuantity": 0,
                        "baseCurrencySymbol": "￥",
                        "packageRule": "",
                        "marketId": 0,
                        "tfCode": "",
                        "skuName": "积加ERP测试产品207198685",
                        "viewShippedTurnover": 0.0,
                        "specialProperties": "",
                        "assemblyCode": "",
                        "imageUrl": "https://img.app.gerpgo.com/demo%2F2022%2F08%2Fattachments%2Fdemo%2F1660703536294a49cb857de5a40f9a193138bd80c8a75_origin_img_v2_393eebf0-88dc-46ab-9844-a8fded06555g.png",
                        "skuNamePrint": "积加ERP测试产品207198685",
                        "currency": "USD",
                        "sellerSku": "TEST_MSKU_GJ ERP-QWE1704",
                        "arrivalMarketId": 0,
                        "singleWeight": 14.1,
                        "productType": 0,
                        "viewLotNoQuantity": 0,
                        "viewProductManagerAccount": "system",
                        "product": "GJ ERP_TEST_SKU-242",
                        "purchaseCost": 67.31,
                        "quantity": 100,
                        "shipmentQuantity": 0,
                        "viewDeliveryDay": 0,
                        "arriveCostUsd": 0.0,
                        "viewPs14": 0.0,
                        "marketName": "共享",
                        "viewPurchaseShippedQuantity": 0,
                        "asin": "BGJ0000269",
                        "viewUnsalableQuantity": 0
                    }
                ],
                "warehouseType": "SELF",
                "totalCost": 18846.8,
                "status": "cancelled",
                "isFbaWarehouse": true,
                "code": "TF1903050001",
                "flag": false,
                "totalPrice": 18846.8,
                "detailSize": 3,
                "cartonTotalVolume": "0.0000",
                "warehouseName": "CN_GJ1",
                "baseCurrencySymbol": "￥",
                "cartonTotalVolumeWeight": 0.0,
                "expectShipmentDate": "2019-03-08",
                "statusName": "已作废",
                "arrivalMarketId": 0,
                "deliveryDate": "2019-03-05",
                "skuSpecies": 3,
                "thirdPartyFlag": false,
                "createDate": "2019-03-05 16:58:24",
                "actualDeliveryDate": "2019-03-05",
                "creator": "积加测试用户11",
                "shipmentQuantity": 0,
                "executorDate": "2019-03-26 18:08:53",
                "auditor": "",
                "updateTime": "2022-05-13 01:12:29",
                "transport": "1",
                "totalVolumeWeight": 30.24,
                "arrivalWarehouseName": "积加测试店铺3:JP_FBA",
                "shipmentIds": [
                    "FBA15C0ZRPWH"
                ],
                "flCode": "FL2002210001",
                "totalWeight": 217.28,
                "cnWarehouse": false
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 80. 查询调拨单详情

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询调拨单详情 |
| 请求地址 | `/fulfillment/inventory/transfer/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 是 | 调拨单号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "code":"TF2302132552"
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "totalVolume": 0.1962752,
        "transportName": "积加测试物流5",
        "totalPriceAmount": {
            "currencyAmount": 3139.4,
            "currencySymbol": "￥",
            "currencyCode": "CNY",
            "amountWithSymbol": "￥3139.40"
        },
        "totalQuantity": 110,
        "pick": 0,
        "executor": "",
        "id": 2552,
        "printListFlag": "yes",
        "arrivalWarehouseId": 43,
        "pickName": "未拣货",
        "packages": 0,
        "warehouseId": 95,
        "auditTime": "2023-02-13",
        "flagName": "未出库",
        "items": [
            {
                "fid": 2552,
                "totalVolume": 0.196275,
                "fnsku": "FNGJX0000070",
                "pickQuantity": 0,
                "singleQuantity": 20,
                "locationDetailsJson": "",
                "volumeWeight": 0.2974,
                "viewPs28": 0.0,
                "viewAvailableQuantity": 1899,
                "price": 28.54,
                "viewTotalTurnover": 71515.0,
                "id": 5619,
                "state": 0,
                "arrivalWarehouseId": 43,
                "cartonSizeW": 36.6,
                "inboundQuantity": 0,
                "listingTitle": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time KBcase-k760SR-uk",
                "weight": 0.9,
                "viewPurchaseQuantity": 12,
                "viewProductManagerAccountId": 7,
                "volume": 0.00178432,
                "unit": "箱",
                "warehouseId": 95,
                "listingTitlePrint": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time KBcase-k760SR-uk",
                "fbaInventoryBarcode": "gj erp listing name, Tex...ng time KBcase-k760SR-uk",
                "viewPlanQuantity": 20,
                "cartonSizeH": 30.6,
                "viewPs7": 0.0,
                "cartonSizeL": 41.7,
                "reducePackage": true,
                "isLockMarket": true,
                "viewWarehouseTurnover": 0.0,
                "totalPrice": 28.54,
                "arriveCost": 0.0,
                "diffQuantity": 0,
                "baseCurrencySymbol": "￥",
                "packageRule": "",
                "marketId": 3,
                "tfCode": "TF2302132552",
                "skuName": "FBA海外商品蒙牛",
                "viewShippedTurnover": 36774.0,
                "specialProperties": "",
                "assemblyCode": "",
                "imageUrl": "https://img.app.gerpgo.com/demo%2F2022%2F08%2Fattachments%2Fdemo%2F1660703536294a49cb857de5a40f9a193138bd80c8a75_origin_img_v2_393eebf0-88dc-46ab-9844-a8fded06555g.png",
                "skuNamePrint": "积加ERP测试产品752436519",
                "assembly": false,
                "currency": "CNY",
                "sellerSku": "TEST_MSKU_GJ ERP-QWE1924",
                "arrivalMarketId": 3,
                "singleWeight": 14.12,
                "productType": 0,
                "viewLotNoQuantity": 34709,
                "viewProductManagerAccount": "积加测试用户7",
                "availableQuantity": 1899,
                "product": "GJ ERP_TEST_SKU-1",
                "purchaseCost": 28.54,
                "quantity": 110,
                "shipmentQuantity": 0,
                "viewDeliveryDay": 0,
                "specification": "1",
                "asinUrl": "https://www.amazon.co.uk/gp/product/B07GJPBZTQ",
                "arriveCostUsd": 0.0,
                "viewPs14": 0.0,
                "totalVolumeWeight": 32.714,
                "marketName": "一号店:UK",
                "viewPurchaseShippedQuantity": 0,
                "totalWeight": 99.0,
                "asin": "B07GJPBZTQ",
                "viewUnsalableQuantity": 0
            }
        ],
        "status": "approve",
        "openLocation": false,
        "isFbaWarehouse": true,
        "code": "TF2302132552",
        "flag": false,
        "totalPrice": 3139.4,
        "detailSize": 1,
        "warehouseName": "CHC_CN",
        "attachmentVOList": [],
        "expectShipmentDate": "2023-02-28",
        "arrivalMarketName": "一号店:UK",
        "arrivalMarketId": 3,
        "deliveryDate": "2023-02-25",
        "skuSpecies": 1,
        "thirdPartyFlag": false,
        "createDate": "2023-02-13 14:53:48",
        "creator": "品链电子",
        "shipmentQuantity": 0,
        "auditor": "品链电子",
        "updateTime": "2023-02-13 14:55:14",
        "transport": "5",
        "totalVolumeWeight": 32.714,
        "arrivalWarehouseName": "一号店:UK_FBA",
        "totalWeight": 99.0
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 81. 查询自营仓进销存列表(旧)

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询自营仓进销存列表(旧) |
| 请求地址 | `/purchase/inventory/purchaseSaleStorageSelf/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 此接口提供历史数据，新接口财务模块-【查询自营仓进销存】 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| type | string | 否 | 查询维度 [仓库级别: WAREHOUSE; 产品级别: SKU] |
| warehouseIds | array | 否 | 仓库Ids |
| defective | boolean | 否 | 是否不良品 [可用量: false; 不良品: true] |
| dateType | string | 否 | 时间查询维度 [月份: MONTH; 日期: DAY] |
| month | string | 否 | 月份值，yyyy-MM。时间查询维度为MONTH时必传 |
| beginDate | date | 否 | 开始查询日期 [yyyy-MM-dd]。时间查询维度为DAY时必传 |
| endDate | date | 否 | 结束查询日期 [yyyy-MM-dd]。时间查询维度为DAY时必传 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| valueType | string | 否 | 值类型 [数量: QUANTITY; 成本: COST] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "total": 20284,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "skuImageUrl": "",
                "ivOutQuantity": 0,
                "asInQuantity": 0,
                "sku": "00001",
                "lnInQuantity": 0,
                "sumOutQuantity": 0,
                "tfOutQuantity": 0,
                "otherOutQuantity": 0,
                "warehouseId": 1,
                "asOutQuantity": 0,
                "ivInQuantity": 0,
                "endQuantity": 0,
                "warehouseName": "CN_GJ1",
                "skuName": "纯牛奶",
                "saleOutQuantity": 0,
                "beginQuantity": 0,
                "tfInQuantity": 0,
                "otherInQuantity": 0,
                "currencySymbol": "￥",
                "sumInQuantity": 0
            }
        ]
    }
}
```

---

## 82. 查询站点库存分布

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询站点库存分布 |
| 请求地址 | `/purchase/inventory/marketInventory/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| warehouseId | long | 是 | warehouseId |
| sku | string | 是 | sku |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "sku":"GJ ERP_TEST_SKU-501",
    "warehouseId":53
}
```

### 响应示例

```json
{
    "traceId": "open_cc48981cb0524749a51ec977157e1863",
    "code": 200,
    "data": [
        {
            "marketName": "共享",
            "warehouseId": 53,
            "reservedQuantity": 0,
            "badQuantity": 0,
            "marketId": 0,
            "normalQuantity": 1000010
        }
    ],
    "messages": [
        "请求成功"
    ]
}
```

---

## 83. 出入库记录V2

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 出入库记录V2 |
| 请求地址 | `/purchase/inventory/storageInbound/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | long | 是 | 每页条数 [最大100条/页] |
| type | string | 否 | 单据类型 [In-入库，Out-出库] |
| warehouseIds | array<long> | 否 | 仓库ID集合 |
| code | string | 否 | 出入库单号 |
| opType | string | 否 | 操作类型据类型 [init-初始化入库，initial-期初库存，qc_inbound-质检入库，TFInbound-调拨入库，IVInbound-盘盈入库，ASInbound-加工入库，ASSplitInbound-拆分入库，LNInbound-采购入库，assemble_child_inbound-组合产品子件入库，otherIn-其它入库，storage_quality_change_in-库存状态变更入，TFOutbound-调拨出库，RGOutbound-退供出库，IVOutbound-盘亏出库，ASOutbound-加工出库，ASSplitOutbound-拆分出库，ln_outbound-采购出库，assemble_child_outbound-组合产品子件出库，OROutbound-订单出库，otherOut-其它出库，B2BOut-B2B销售出库，storage_quality_change_out-库存状态变更出，AdjustOutbound-调整出库，outSource-委外出库，self_sale_order_return-自发货销售退货，inboundRevoke-入库撤销出库] |
| createStartDate | date | 否 | 创建开始时间 [yyyy-MM-dd] |
| createEndDate | date | 否 | 创建结束时间 [yyyy-MM-dd] |
| remark | string | 否 | 备注 |
| fcode | string | 否 | 关联单据 |
| fcodeList | array<string> | 否 | 关联单据集合 |
| page | long | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "total": 6516,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "purchaseCost": 11616.6,
                "code": "GIB13623020900000018",
                "quantity": -500,
                "opType": "TFOutbound",
                "arriveCost": 0.0,
                "memo": "",
                "supplierCode": "",
                "supplierName": null,
                "type": "Out",
                "warehouseName": "0000:广东洁诺",
                "createdAt": "2023-02-09 16:55:34",
                "priceCost": 11616.6,
                "warehouseId": 136,
                "opTypeName": "调拨出库",
                "creater": "深圳市鸿鹄集",
                "currency": "CNY",
                "id": 6837,
                "stockCountType": "TFOutbound",
                "stockCountTypeName": null,
                "fcode": "TF2302092551",
                "inboundItemVOS": null
            }
        ]
    }
}
```

---

## 84. 出入库明细V2

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 出入库明细V2 |
| 请求地址 | `/purchase/inventory/storageInbound/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 是 | 入库单据编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "code": "GIB13623020900000018"
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "purchaseCost": 11616.6,
        "code": "GIB13623020900000018",
        "quantity": 500,
        "opType": "TFOutbound",
        "arriveCost": 0.0,
        "memo": "",
        "supplierCode": "",
        "type": "Out",
        "warehouseName": "0000:广东洁诺",
        "createdAt": "2023-02-09 16:55:34",
        "priceCost": 11616.6,
        "warehouseId": 136,
        "inboundItemVOS": [
            {
                "fulfillableQuantityBad": 0,
                "nowBadQuantity": 0,
                "outNum": 1675932601,
                "arriveCost": 0.0,
                "warehouseBatchNo": "GWB1362023-02-09000017",
                "fulfillableQuantity": 500,
                "skuName": "白色Q",
                "exchangeRate": 1.0,
                "price": 23.2332,
                "imageUrl": "",
                "basicPurchasePrice": 23.2332,
                "currency": "CNY",
                "sellerSku": "130BK",
                "sku": "BS-Q",
                "quantity": -500,
                "purchaseCostValue": 0,
                "purchaseCostValueName": "实际税率：含税单价",
                "skuType": "Assembly",
                "nowQuantity": 0,
                "unit": "套",
                "marketName": "一号店--有广告数据:US",
                "quantityBad": 0
            }
        ],
        "creater": "深圳市鸿鹄集",
        "currency": "CNY",
        "id": 6837,
        "stockCountType": "TFOutbound",
        "fcode": "TF2302092551"
    }
}
```

---

## 85. 查询FBA库存列表（旧）

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA库存列表（旧） |
| 请求地址 | `/purchase/store/fbaInventory/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| listingLevels | array<string> | 否 | 商品运营级别 [系统-字典管理-商品运营级别] |
| listingStates | array<string> | 否 | 商品运营状态 [系统-字典管理-商品运营状态] |
| state | int | 否 | 状态 [0-异常，1-正常] |
| storageCostAuthority | string | 否 | 成本权限参数 [fifo-先进先出成本，monEndAveWeight-月末加权成本，customizeCost-自定义成本] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| warehouseIds | array<int> | 否 | 仓库id集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20
}
```

### 响应示例

```json
{
    "traceId": "open_95bb87cee8674b4b9e9af1f4edd8e83a",
    "code": 200,
    "data": {
        "total": 1492,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "ps": 0.0,
                "inboundWorking": 0,
                "erpInboundWorking": 0,
                "fbaTurnover": 0.0,
                "stateName": "正常",
                "computePses": "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                "id": 38529,
                "state": 1,
                "brand": "-",
                "reservedFCTransfer": 0,
                "purchaseShippedQuantity": 0,
                "inventoryAge1to2Month": 0,
                "warehouseId": 36,
                "researchingQuantity": 0,
                "computeYesterday9Pses": "0,0,0,0,0,0,0",
                "updateDate": 1668823453567,
                "inventoryQuantity": 0,
                "sellingManagerName": [],
                "warehouseName": "积加测试店铺7:US_FBA",
                "barcodeDescription": "",
                "inventoryAge12MonthUp": 0,
                "goodAvailableQuantity": 0,
                "inventoryAge0to3Month": 0,
                "availableQuantity": 0,
                "unsalableQuantity": 0,
                "warehouseCountry": "US",
                "erpInboundShipped": 0,
                "afnName": "亚马逊配送",
                "updateTime": "2022-11-19 10:04:13",
                "addDate": 1668764721592,
                "countryListingLevels": [
                    {
                        "country": "US"
                    }
                ],
                "goodsTitle": "CHESONA iPad Pro 11 Case with Keyboard, Keyboard for iPad Air 5th Generation - 7 Backlight & Detachable - Pencil Holder - Flip Stand Cover iPad Air 5th/4th 10.9\" iPad Pro 11 inch Keyboard, Blue",
                "inboundReceiving": 0,
                "reservedFutureSupply": 0,
                "erpInbound": true,
                "unsalableAmount": 0,
                "fnsku": "X003IRCZOR",
                "addTime": "2022-11-18 17:45:21",
                "reservedQuantity": 0,
                "goodsTitlePrint": "",
                "futureSupplyBuyable": 0,
                "erpInboundReceiving": 0,
                "lnQuantity": 0,
                "shippedTurnover": 0.0,
                "inventoryAge9to12Month": 0,
                "overseasQuantity": 0,
                "productTypeName": "",
                "defectiveQuantity": 0,
                "countryListingStates": [
                    {
                        "country": "US"
                    }
                ],
                "msku": "S001",
                "inboundQuantity": 0,
                "listingTitle": "CHESONA iPad Pro 11 Case...o 11 inch Keyboard, Blue",
                "totalTurnover": 0.0,
                "sum7ps": 0,
                "fbaInboundQuantity": 0,
                "inventoryAge0to1Month": 0,
                "poQuantity": 0,
                "fbaQuantity": 0,
                "sum30ps": 0,
                "inventoryAge3to6Month": 0,
                "inventoryAge2to3Month": 0,
                "reservedFCProcessing": 0,
                "sum15ps": 0,
                "turnover": 0.0,
                "unsalableRate": 0,
                "plQuantity": 0,
                "reservedCustomerOrders": 0,
                "afn": 1,
                "inboundShipped": 0,
                "inventoryAge6to9Month": 0,
                "asin": "B08FYHZLJG",
                "category": "未分配品类",
                "erpInboundWaitShipped": 0
            }
        ]
    },
    "messages": ["请求成功"]
}
```

---

## 86. 创建其他出库单-已完成状态

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 创建其他出库单-已完成状态 |
| 请求地址 | `/purchase/store/otherOut/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 创建的其他出库单为已完成状态 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| operationType | string | 是 | 子操作类型 [erp系统字典管理-自建仓库存出入库类型] |
| memo | string | 否 | 备注，最大500 |
| outboundRule | string | 是 | 其它出库规则 [FIFO-先进先出(默认)，FIFO-MARKET-先进先出(站点)，SERIAL_BATCH-指定实物批次] |
| fifoItemList | array<object> | 否 | 先进先出产品明细 |
| serialBatchItemList | array<object> | 否 | 指定实物批次产品明细 |
| warehouseId | int | 是 | 仓库id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | string | 是 | 返回数据，出库单号 |
| messages | array<string> | 是 | 提示信息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "warehouseId": 728,
    "operationType": "内部调样",
    "outboundRule": "FIFO",
    "fifoItemList": [{
        "sku": "09-****-SXDI",
        "outboundGoodQuantity": 1,
        "outboundBadQuantity": 0
    }]
}
```

### 响应示例

```json
{
    "traceId": "open_dae988530a54406380d3622c09ecce2e",
    "code": 200,
    "data": "OT2023051200024",
    "messages": [
        "添加成功"
    ]
}
```

---

## 87. 创建其他出库单-草稿状态

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 创建其他出库单-草稿状态 |
| 请求地址 | `/purchase/store/draftOtherOutbound/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 创建的其他出库单为草稿状态 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| operationType | string | 是 | 子操作类型 [erp系统字典管理-自建仓库存出入库类型] |
| memo | string | 否 | 备注，最大50 |
| outboundRule | string | 是 | 其它出库规则 [目前仅支持先进先出：FIFO] |
| fifoItemList | array | 否 | 先进先出产品明细 |
| warehouseId | int | 是 | 仓库id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 服务器响应Status Code |
| data | string | 否 | 返回数据，出库单号 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 链路追踪id |

### 请求示例

```json
{
    "warehouseId": 728,
    "operationType": "内部调样",
    "outboundRule": "FIFO",
    "fifoItemList": [{
        "sku": "09-****-SXDI",
        "outboundGoodQuantity": 1,
        "outboundBadQuantity": 0
    }]
}
```

### 响应示例

```json
{
    "traceId": "open_dae988530a54406380d3622c09ecce2e",
    "code": 200,
    "data": "OT2023051200024",
    "messages": [
        "添加成功"
    ]
}
```

---

## 88. 创建其他入库单-已完成状态

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 创建其他入库单-已完成状态 |
| 请求地址 | `/purchase/store/otherIn/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 创建的其他入库单为已完成状态 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| operationType | string | 是 | 子操作类型 [erp系统字典管理-自建仓库存出入库类型] |
| supplierCode | string | 否 | 供应商编码 |
| bizTime | date | 否 | 业务时间 [yyyy-MM-dd] |
| memo | string | 否 | 备注 |
| itemList | array<object> | 是 | 产品明细 |
| warehouseId | int | 是 | 仓库id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |

### 请求示例

```json
{
    "warehouseId": 64,
    "operationType": "海外仓销售出库",
    "itemList": [
        {
            "sku": "DEB2064",
            "marketId": 38,
            "inboundGoodQuantity": 1,
            "inboundBadQuantity": 0,
            "purchaseCurrency": "CNY",
            "purchaseCost": 0,
            "arriveCurrency": "CNY",
            "arriveCost": 0
        }
    ]
}
```

### 响应示例

```json
{
    "code": 0,
    "data": {},
    "messages": []
}
```

---

## 89. 创建其他入库单-草稿状态

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 创建其他入库单-草稿状态 |
| 请求地址 | `/purchase/store/draftOtherInbound/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 创建的其他入库单为草稿状态 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| operationType | string | 是 | 子操作类型 [erp系统字典管理-自建仓库存出入库类型] |
| bizTime | date | 否 | 业务时间 [yyyy-MM-dd] |
| memo | string | 否 | 备注，最大50 |
| itemList | array<object> | 是 | 产品明细 |
| warehouseId | int | 是 | 仓库id |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| data | string | 否 | 返回数据，入库单号 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 链路追踪id |

### 请求示例

```json
{
    "warehouseId": 728,
    "operationType": "内部调样",
    "itemList": [{
        "marketId": 0,
        "sku": "09-*****-SXDI",
        "inboundGoodQuantity": 1,
        "inboundBadQuantity": 1,
        "purchaseCurrency": "USD",
        "purchaseCost": 0,
        "arriveCurrency": "USD",
        "arriveCost": 0,
        "memo": ""
    }]
}
```

### 响应示例

```json
{
    "traceId": "open_ebfb95951b2f42a4b18cb2a8a3d32cd7",
    "code": 200,
    "data": "OT2023051200018",
    "messages": [
        "添加成功"
    ]
}
```

---

## 90. 查询FBA库存列表V2

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA库存列表V2 |
| 请求地址 | `/purchase/store/fbaInventory/page/V2` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 灰度上线 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| mskuList | array<string> | 否 | MSKU批量查询集合 |
| asinList | array<string> | 否 | ASIN批量查询集合 |
| listingLevelList | array<string> | 否 | 商品运营级别 [系统-字典管理-商品运营级别] |
| listingStateList | array<string> | 否 | 商品运营状态 [系统-字典管理-商品运营状态] |
| state | int | 否 | 状态 [0-异常，1-正常] |
| storageCostAuthority | string | 否 | 成本权限参数 [fifo-先进先出成本，monEndAveWeight-月末加权成本，customizeCost-自定义成本] |
| startCreateTime | datetime | 否 | 开始创建时间 |
| endCreateTime | datetime | 否 | 结束创建时间 |
| startUpdateTime | datetime | 否 | 开始更新时间 |
| endUpdateTime | datetime | 否 | 结束更新时间 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| hideZeroQuantity | boolean | 否 | 隐藏0库存数据，true隐藏，其余为不隐藏 |
| warehouseIdList | array<int> | 否 | 仓库id集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20
}
```

### 响应示例

```json
{}
```

---

## 91. 自发货订单-配货单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 自发货订单-配货单列表 |
| 请求地址 | `/fulfillment/order/foOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页显示多少条[最大100条/页] |
| deliveryTimeAfter | date | 否 | 发货时间起始日期yyyy-MM-dd |
| deliveryTimeBefore | date | 否 | 发货时间截止日期yyyy-MM-dd |
| createdTimeAfter | date | 否 | 创建起始日期yyyy-MM-dd |
| createdTimeBefore | date | 否 | 创建截止日期yyyy-MM-dd |
| updateTimeAfter | date | 否 | 最后更新起始日期yyyy-MM-dd |
| updateTimeBefore | date | 否 | 最后更新截止日期yyyy-MM-dd |
| orderTimeAfter | date | 否 | 订购起始日期yyyy-MM-dd |
| orderTimeBefore | date | 否 | 订购截止日期yyyy-MM-dd |
| fullUpdateTimeAfter | string | 否 | 包裹更新起始时间yyyy-MM-dd HH:mm:ss |
| fullUpdateTimeFullBefore | string | 否 | 包裹更新截止时间yyyy-MM-dd HH:mm:ss |
| sourceChannel | array<string> | 否 | 来源渠道 |
| sourceCode | array<string> | 否 | 来源单号（Goflow、Teapplix、shopify、shopline、OTTO 是流水号【platformOrderNumber】，其他平台用平台单号） |
| marketId | array<int> | 否 | 聚合站点Ids |
| shopId | array<string> | 否 | 店铺Ids |
| shopName | array<string> | 否 | 店铺名称 |
| customerPackageNoList | array<string> | 否 | 客户发货包裹号集合 |
| orderCodeList | array<string> | 否 | OMS配货单号 |
| foOrderStatus | array<string> | 否 | 配货单履约状态 [PENDING-待处理 STAY_CONFIRM-待审核 NOTICE_DISTRIBUTION-通知配货 SHIPPING-发货中 SHIPPED-已出运 CANCELED-取消 CHECKED-已审核 ALREADY_DELIVERY-已发货 DELETE-已作废] |
| shopCountry | array<string> | 否 | 店铺对应的国家 |
| warehouseId | array<string> | 否 | 发货仓库Id |
| orderType | array<string> | 否 | 订单类型(STANDARD-标准订单、PRE_ORDER-预售订单、SUPPLEMENTARY-补录订单、REISSUE-补单发货) |
| thirdWarehouseFlag | string | 否 | 是否三方仓发货:N-否、Y-是 |
| syncDeliveryFlag | array<string> | 否 | 平台标发状态(NEED_NOT-无需标发 AWAIT_SYNC-待同步发货 READY_SYNC-可同步发货 SUCCESS-同步发货成功 FAILED-同步发货失败 SYNC_FLATFORM-已上传平台) |
| deliveryMethod | array<string> | 否 | 订单配送方式:PLATFORM-平台仓发货、FBA-转FBA配送、SELLER-卖家自配送、FBC-转FBC配送、WFS-转WFS配送、CG-转CG配送 |
| accessMode | array<string> | 否 | 接入方式(MANUAL-手工 INTERFACE-接口 IMPORT-导入) |
| bizStatusList | array<string> | 否 | 业务状态(DRAFT 草稿; WAIT_ACCEPT 待接单; WAIT_SHIP_CONFIRM 待发货审核; WAIT_SHIP 待发货; SHIPPED 已发货; SHIP_NEEDLESS 不发货) |
| labelList | array<string> | 否 | 暂支持：OPEN_API_ADD |
| page | int | 是 | 第几页，默认第1页 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 返回提示信息 |
| traceId | string | 否 | 链路追踪ID |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_9d31cb855e264b368a58a2c5ad8dc5da",
    "code": 200,
    "data": {
        "total": 70,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "orderType": "SUPPLEMENTARY",
                "orderTimeMarket": "2023-11-06 16:11:42",
                "foOrderNo": "FO231115151658171007001",
                "sellerShipmentEndTime": null,
                "orderTime": "2023-11-06 16:11:42",
                "soOrderNo": "SO231115151658171007001",
                "foOrderStatus": "ALREADY_DELIVERY",
                "shopId": "10",
                "executionErrorMessage": "",
                "packageCreateTime": null,
                "syncDeliveryFlag": null,
                "timeZone": "Asia/Shanghai",
                "paymentMethodName": "其它",
                "thirdWarehouseFlag": "N",
                "sellerRemark": null,
                "buyerInfo": {
                    "buyerRemark": null,
                    "buyerTaxNo": null,
                    "buyerEmail": null,
                    "id": 72,
                    "buyerName": "卖家姓名",
                    "buyerCode": null
                },
                "platformAssign": {
                    "platformWarehouseName": null,
                    "platformCarrierCode": null,
                    "platformWarehouseId": null
                },
                "warehouseId": 728,
                "paymentMethod": "OTHER",
                "sourceOrderNo": "1699258279004",
                "packageDeliveryTime": null,
                "paymentTimeMarket": null,
                "foOrderLogisticsInfoVO": {
                    "fileName": null,
                    "logisticsChannel": "32131",
                    "filePath": null,
                    "currencySymbol": null,
                    "logisticsCode": null,
                    "logisticsName": "自发货物流商2",
                    "estimatedTimeLimit": null,
                    "trackingNo": null,
                    "estimatedLogisticsExpenses": 0.0,
                    "shipmentId": null,
                    "logisticsNo": "412210",
                    "soOrderCode": "SO231115151658171007001",
                    "faceSheet": null,
                    "orderCode": "FO231115151658171007001",
                    "currency": "USD",
                    "id": 68,
                    "logisticsRealName": null,
                    "logisticsChannelName": "32131",
                    "waybillNo": null
                },
                "isCustomizationOrder": "N",
                "customerPackageNo": null,
                "deliveryTime": null,
                "sourceChannel": "AMAZON",
                "shopName": "******",
                "accessMode": null,
                "warehouseName": "AJ_CN",
                "orderItems": [
                    {
                        "thirdSku": null,
                        "returnedQuantity": null,
                        "sourceLineNo": "6d50d07867e24ddc9ff93a6abb5623bd",
                        "skuDescribe": "3aly导入sku8141",
                        "expectedQuantity": 1,
                        "remark": null,
                        "logisticsAmount": null,
                        "soOrderDetailId": 230,
                        "buyerPayTax": 0.0,
                        "logisticsServiceName": null,
                        "buyerPayShipFee": 0.0,
                        "currency": "USD",
                        "sku": "3alyimport814",
                        "unitPrice": 27.99,
                        "amount": 27.99,
                        "msku": "3alyimport814",
                        "quantity": 1,
                        "actualAmount": 26.69,
                        "customizedText": null,
                        "packageLineNo": 81,
                        "asin": null,
                        "itemPrice": 27.99,
                        "foOrderLineNo": 81,
                        "outOfStockFlag": "N"
                    }
                ],
                "packageNo": null,
                "shopCountry": "MX",
                "buyerPayShipFee": 0.0,
                "countryCode": "US",
                "currency": "USD",
                "paymentTime": null,
                "updateTime": null,
                "orderTypeName": "补录订单",
                "createTime": "2023-11-15 15:16:59",
                "consigneeInfo": {
                    "area": null,
                    "country": "United States of America (USA)",
                    "receivePhone": null,
                    "address": "详细地址",
                    "receivePostalCode": "收件人邮编",
                    "city": "城市",
                    "provinceCode": null,
                    "cityCode": null,
                    "streetCode": null,
                    "receiveEmail": null,
                    "areaCode": null,
                    "receiveName": "收件人姓名",
                    "province": null,
                    "countryCode": "US",
                    "street": null,
                    "id": 72
                }
            }
        ]
    },
    "messages": []
}
```

---

## 92. 查询自配送订单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询自配送订单列表 |
| 请求地址 | `/fulfillment/order/mfnOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| condition | object | 否 | 查询条件 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "total": 431,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "addressPostalcode": "07480-3202",
                "orderType": "StandardOrder",
                "purchaseDate": "2023-02-20 00:00:00",
                "orderId": "111-8298730-3860259",
                "buyerEmail": "gj6832@gerpgo.com",
                "addressCountrycode": "US",
                "lastUpdateDate": "2018-01-25 13:53:39",
                "orderStatus": 3,
                "salesChannel": "Amazon.com",
                "serverId": 1,
                "addressStateorregion": "NJ",
                "marketId": 1,
                "b2b": 0,
                "orderTotalAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$0.00"
                },
                "addressLine1": "test address 1",
                "addressLine2": "test address2",
                "id": 6832,
                "addressLine3": "test address 3",
                "shipmentsMethod": "pending",
                "addressCity": "WEST MILFORD",
                "itemVos": [
                    {
                        "fid": 6832,
                        "quantityOrdered": 1,
                        "productName": "12",
                        "promotionId": "",
                        "sellerSku": "TEST_MSKU_GJ ERP-QWE1193",
                        "sku": "12",
                        "smallImageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                        "listingTitle": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time K765B-BK-self",
                        "asinUrl": "https://www.amazon.com/gp/product/BGJ0000001",
                        "itemId": "",
                        "quantityShipped": 0,
                        "itemPriceAmount": {
                            "currencyAmount": 52.99,
                            "currencySymbol": "$",
                            "currencyCode": "USD",
                            "amountWithSymbol": "$52.99"
                        },
                        "asin": "BGJ0000001",
                        "itemPrice": 52.99,
                        "buyerRequestedCancel": 0,
                        "buyerCancelReason": ""
                    }
                ],
                "vat": 0,
                "buyerName": "gj zhangsan6832",
                "orderTotal": 0.0,
                "addressPhone": "",
                "carrier": "",
                "shipmentsMethodName": "待录入",
                "shipTrack": "",
                "bogusFlag": false,
                "returns": 0,
                "addressName": "gj erp test address",
                "fulfillment": "MFN",
                "shipmentWarehouseId": 1,
                "sellerOrderId": "111-8298730-3860259",
                "refund": 0
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 93. 自发货订单-销售订单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 自发货订单-销售订单列表 |
| 请求地址 | `/fulfillment/order/soOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 历史接口，请参考配货单，因亚马逊隐私政策，API只会返回订购时间在一个月内的买家信息和收货人信息 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| orderTimeAfter | date | 否 | 订购起始日期 [yyyy-MM-dd] |
| orderTimeBefore | date | 否 | 订购截止日期 [yyyy-MM-dd] |
| createTimeAfter | date | 否 | 积加系统创建起始日期 [yyyy-MM-dd] |
| createTimeBefore | date | 否 | 积加系统创建截止日期 [yyyy-MM-dd] |
| lastUpdatedAfter | date | 否 | 积加系统更新开始时间 [yyyy-MM-dd] |
| lastUpdatedBefore | date | 否 | 积加系统更新截止时间 [yyyy-MM-dd] |
| sourceChannel | array | 否 | 来源渠道 [亚马逊: AMAZON; 沃尔玛: WALMART; 自定义: CUSTOM; eBay: EBAY; 虾皮: SHOPEE; lazada: LAZADA; 速卖通: ALIEXPRESS; tikTok: TIKTOK; shopify: SHOPIFY; cdiscount: CDISCOUNT; wish: WISH] |
| shopName | array | 否 | 店铺名称 |
| soOrderNo | array | 否 | 销售订单号 |
| morderTypeList | array<string> | 否 | 配送方式 [PLATFORM(平台仓发货) FBA(转FBA配送) SELLER(卖家自配送)] |
| customizedFlag | string | 否 | 是否定制化订单 [Y-是, N-不是] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回内容分页列表 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_b9b496a4dd4c48e38c1183b4daa66f7f",
    "code": 200,
    "data": {
        "total": 136,
        "pagesize": 0,
        "page": 0,
        "rows": [
            {
                "isCustomizationOrder": "N",
                "discountFee": null,
                "sourceChannel": "AMAZON",
                "shopName": "**",
                "sellerShipmentEndTime": null,
                "orderTime": "2022-06-30 16:10:30",
                "buyerPayTax": null,
                "buyerPayShipFee": null,
                "soOrderNo": "SO220630161239195001",
                "countryCode": "AD",
                "currency": "AED",
                "id": 1,
                "shopId": "7",
                "shopCountryCode": "US",
                "shipmentLevel": null,
                "actualAmount": 0.0,
                "sellerRemark": "",
                "totalAmount": 40.0,
                "buyerInfo": null,
                "soOrderDetails": [
                    {
                        "unitPrice": 6.6667,
                        "amount": 20.0,
                        "msku": null,
                        "actualAmount": 0.0,
                        "skuDescribe": "*******",
                        "expectedQuantity": 3,
                        "customizedText": null,
                        "soOrderLineNo": 80,
                        "validQuantity": 3,
                        "sourceOrderLineNo": "***********",
                        "customizedPics": null,
                        "buyerPayTax": null,
                        "buyerPayShipFee": null,
                        "asin": null,
                        "itemPrice": 20.0,
                        "customizedAttachment": null,
                        "sku": "********"
                    },
                    {
                        "unitPrice": 6.6667,
                        "amount": 20.0,
                        "msku": null,
                        "actualAmount": 0.0,
                        "skuDescribe": "*******",
                        "expectedQuantity": 3,
                        "customizedText": null,
                        "soOrderLineNo": 81,
                        "validQuantity": 3,
                        "sourceOrderLineNo": "**********",
                        "customizedPics": null,
                        "buyerPayTax": null,
                        "buyerPayShipFee": null,
                        "asin": null,
                        "itemPrice": 20.0,
                        "customizedAttachment": null,
                        "sku": "*****"
                    }
                ],
                "platformAssign": {
                    "platformWarehouseName": null,
                    "platformCarrierCode": null,
                    "platformWarehouseId": null
                },
                "discountCode": null,
                "createTime": "2022-06-30 16:12:40",
                "morderType": "SELLER",
                "consigneeInfo": null,
                "sourceOrderNo": "******"
            }
        ]
    },
    "messages": []
}
```

---

## 94. 查询供应商信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询供应商信息 |
| 请求地址 | `/purchase/srm/supplier/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| state | int | 否 | 状态 [0-启用，1-停用] |
| createStartDate | date | 否 | 创建时间开始时间 [yyyy-MM-dd] |
| createEndDate | date | 否 | 创建时间结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| code | string | 否 | 供应商编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_2222e41d6d3243f4b736cc43ba0d83d0",
    "code": 200,
    "data": {
        "total": 73,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "code": "GJ_S1",
                "contractTemplateVOS": [
                    {
                        "templateName": "《系统分仓合同模板》",
                        "templateId": 1
                    },
                    {
                        "templateName": "《系统并仓合同模板》",
                        "templateId": 2
                    },
                    {
                        "templateName": "《111》",
                        "templateId": 4
                    }
                ],
                "description": "积加ERP测试描述",
                "updateAt": "2022-01-07 15:09:13",
                "qqNumber": "523456789",
                "paymentType": 1,
                "phone1": "13812345678",
                "buyerManagerId": 7,
                "createdAt": "2019-02-18 11:34:18",
                "updaterId": 1,
                "paymentRuleCode": "FKTJ202205130001",
                "contact": "积加测试用户1",
                "paymentCycle": 0,
                "state": 0,
                "createrId": 7,
                "addr": "湖南省长沙市岳麓区露谷企业广场",
                "email": "gj@gerpgo.com",
                "paymentDesc": "",
                "supplierWarehouse": true,
                "paymentRate": 100.0,
                "paymentRuleDesc": "FKTJ202205130001-现结-现结",
                "open1688IsMatch": false,
                "receiptInfo": "[{\"name\":\"积加测试用户\",\"bankName\":\"积加银行长沙支行\",\"bankCode\":\"6666 5555 4444 3333 2222 1111\"}]",
                "name": "义乌",
                "creater": "测试用户",
                "faxNumber": "3432-34135",
                "paymentDate": 0,
                "buyerManager": "积加测试用户7"
            }
        ]
    },
    "messages": ["request.success"]
}
```

---

## 95. 录入供应商信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 录入供应商信息 |
| 请求地址 | `/purchase/srm/supplier/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| name | string | 是 | 供应商名称 |
| buyerManager | string | 否 | 采购员名称 |
| buyerManagerId | int | 是 | 采购员id |
| developId | int | 否 | 开发人员ID |
| developer | string | 否 | 开发人员 |
| paymentType | int | 是 | 结算方式 [1-现结，2-月结] |
| paymentDesc | string | 否 | 结算描述 |
| paymentRuleCode | string | 是 | 付款条件编码 |
| state | short | 是 | 状态 [0-启用，1-停用] |
| contact | string | 是 | 供应商联系人 |
| phone1 | string | 是 | 联系人电话 |
| supplierWarehouse | boolean | 是 | 是否作为供应商仓 |
| permissionGroupIds | array<int> | 否 | 权限组ID集合 |
| email | string | 否 | 邮箱 |
| addr | string | 否 | 供应商地址 |
| faxNumber | string | 否 | 传真号 |
| qqNumber | string | 否 | QQ号 |
| description | string | 否 | 备注 |
| receiptInfo | string | 否 | 收款类型 [corporate-公司，individual-个人] |
| attachmentIds | array<int> | 否 | 附件id集合，附件containerType:supplierFile |
| open1688ShopUrl | string | 否 | 供应商1688旺铺地址 |
| code | string | 是 | 供应商编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | string | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "code": "YYSY3",
    "name": "测试专用00013",
    "buyerManagerId": 1,
    "paymentType": 1,
    "paymentDesc": "结算描述{预付比例}",
    "state": 0,
    "contact": "Uzi",
    "phone1": "123456789",
    "supplierWarehouse": false,
    "paymentRuleCode":"结算描述{预付比例}"
}
```

### 响应示例

```json
{
    "traceId": "open_0e9acbd305884d0f8427d13479a43c74",
    "code": 200,
    "data": "true",
    "messages": [
        "添加成功"
    ]
}
```

---

## 96. 修改供应商信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 修改供应商信息 |
| 请求地址 | `/purchase/srm/supplier/update` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| name | string | 是 | 供应商名称 |
| buyerManager | string | 否 | 采购员名称 |
| buyerManagerId | int | 否 | 采购员id |
| developId | int | 否 | 开发人员ID |
| developer | string | 否 | 开发人员 |
| paymentType | int | 是 | 结算方式（1：现结；2：月结；） |
| paymentDesc | string | 否 | 结算描述 |
| paymentRuleCode | string | 是 | 付款条件编码 |
| state | short | 是 | 状态（0：启用；1：停用；） |
| contact | string | 是 | 供应商联系人 |
| phone1 | string | 是 | 联系人电话 |
| supplierWarehouse | boolean | 是 | 是否作为供应商仓 |
| permissionGroupIds | array<long> | 否 | 权限组ID集合 |
| email | string | 否 | 邮箱 |
| addr | string | 否 | 供应商地址 |
| faxNumber | string | 否 | 传真号 |
| qqNumber | string | 否 | QQ号 |
| description | string | 否 | 备注 |
| receiptInfo | string | 否 | 收款信息-收款类型(corporate:公司 individual:个人) |
| attachmentIds | array<string> | 否 | 附件id集合，附件containerType:supplierFile |
| open1688ShopUrl | string | 否 | 供应商1688旺铺地址 |
| open1688ShopName | string | 否 | 供应商1688旺铺名称 |
| open1688IsMatch | boolean | 否 | 供应商1688旺铺是否配对 |
| contactList | array<object> | 否 | 供应商联系人信息集合 |
| buyerManagerAccount | string | 否 | 采购员账号 |
| developAccount | string | 否 | 开发人员账号 |
| receiptInfoList | array<object> | 否 | 收款信息集合 |
| code | string | 是 | 供应商编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "code": "YYSY3",
    "name": "测试专用00013",
    "buyerManagerId": 1,
    "paymentType": 1,
    "paymentDesc": "结算描述{预付比例}",
    "state": 0,
    "contact": "Uzi",
    "phone1": "123456789",
    "supplierWarehouse": false,
    "paymentRuleCode":"FKTJ202205130031"
}
```

### 响应示例

```json
{
    "traceId": "open_2f7289f662d34056824a7e2384637ecf",
    "code": 200,
    "data": null,
    "messages": [
        "request.success"
    ]
}
```

---

## 97. 查询供应商产品列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询供应商产品列表 |
| 请求地址 | `/purchase/srm/supplierSkuQuote/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| createDateEnd | datetime | 否 | 创建结束时间 [yyyy-MM-dd HH:mm:ss] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| productState | int | 否 | 产品状态 [0-正常，1-停用] |
| status | int | 否 | 供应商产品状态 [0-正常，1-停用] |
| supplierStatus | int | 否 | 供应商资料状态 [0-正常，1-停用] |
| productList | array<string> | 否 | sku集合 |
| createDateBegin | datetime | 否 | 创建开始时间 [yyyy-MM-dd HH:mm:ss] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_e71d3aefbca642659da4ab16f9c4499d",
    "code": 200,
    "data": {
        "size": 1,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "auditStatusCode": "review_agree",
                "moq": 0,
                "purchaseUrl": "",
                "createdAt": "2019-02-18 11:49:13",
                "price": 0.2,
                "invoiceType": "not_invoiced",
                "id": 2,
                "auditStatusName": "审核通过",
                "quoteRemark": "",
                "includedTax": 0,
                "supplierWarehouse": 50,
                "invoiceTaxRate": 0.0,
                "taxRebateRate": 0.0,
                "taxRate": 0.0,
                "gradientQuote": 0,
                "creater": "测试用户",
                "includeTaxPrice": 0.2,
                "supplierGradientQuoteJson": "[{\"endQuantity\":9999999,\"includeTaxPrice\":0.2000,\"startQuantity\":1,\"taxRate\":0.00,\"unincludeTaxPrice\":0.2000}]",
                "bucklePackage": 0,
                "status": 1,
                "invoiceTypeName": "不开票",
                "bindOpen1688": false,
                "includeTaxPriceAmount": {
                    "currencyAmount": 0.2,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.2000"
                },
                "supplierNumber": "",
                "supplierCode": "GJ_S2",
                "includePackage": 0,
                "buyerManagerId": "7",
                "attachmentVOList": [],
                "baseInfoRemark": "",
                "defaultSupplier": 0,
                "currency": "CNY",
                "priceAmount": {
                    "currencyAmount": 0.2,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.2000"
                },
                "supplierName": "金华",
                "product": "jp327a manual-us",
                "taxPriceAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.00"
                },
                "supplierGradientQuotes": [
                    {
                        "endQuantity": 9999999,
                        "unincludeTaxPrice": 0.2,
                        "startQuantity": 1,
                        "taxRate": 0.0,
                        "includeTaxPrice": 0.2
                    }
                ],
                "productStateName": "",
                "deliveryDays": 5,
                "taxPrice": 0.0,
                "buyerManager": "积加测试用户7"
            }
        ]
    },
    "messages": []
}
```

---

## 98. 新增供应商产品

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 新增供应商产品 |
| 请求地址 | `/purchase/srm/supplierSkuQuote/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| supplierName | string | 否 | 供应商名称 |
| buyerManager | string | 否 | 采购员 |
| buyerManagerId | string | 否 | 采购员ID |
| defaultSupplier | int | 是 | 是否默认供应商 [0-否，1-是] |
| product | string | 是 | sku |
| productName | string | 否 | 产品名称 |
| productState | int | 否 | 产品状态 |
| productStateName | string | 否 | 产品状态名称 |
| productType | int | 否 | 产品类型 |
| productImageUrl | string | 否 | 产品图片地址 |
| deliveryDays | int | 是 | 采购交期 |
| moq | int | 是 | 最小起订量 |
| supplierNumber | string | 否 | 供应商货号 |
| status | int | 否 | 状态 [0：禁用，1：启用] |
| purchaseUrl | string | 否 | 产品网址 |
| baseInfoRemark | string | 否 | 基本信息备注 |
| includePackage | int | 是 | 是否含包材 |
| currency | string | 是 | 币种 [参考Q&A-通用参数-币种] |
| taxRate | number | 是 | 税率 [%] |
| invoiceType | string | 是 | 发票类型[special_invoice：专票，plain_invoice：普票，not_invoiced：不开票] |
| invoiceTypeName | string | 否 | 发票类型名称 |
| invoiceTaxRate | number | 是 | 票面税率 [%] |
| gradientQuote | int | 是 | 是否梯度报价 |
| bucklePackage | int | 否 | 是否减包材 [0-否，1-是] |
| auditStatusCode | string | 否 | 审批状态Code |
| auditStatusName | string | 否 | 审批状态名称 |
| createdAt | string | 否 | 创建时间 |
| creater | string | 否 | 创建人 |
| editPage | int | 否 | 是否编辑页面 |
| quoteFlag | int | 否 | 是否重新报价（重新报价需要清理审批流） |
| quoteRemark | string | 否 | 报价备注 |
| supplierGradientQuoteJson | string | 否 | 报价Json |
| supplierGradientQuotes | array<object> | 是 | 报价，根据gradientQuote区分是否梯度报价 |
| supplierWarehouse | int | 否 | 是否是供应商仓 |
| syncDeliveryDays | int | 是 | 是否同步采购交期 |
| taxPrice | number | 否 | 含税单价 |
| taxPriceAmount | object | 否 | 含税单价 |
| taxRebateRate | number | 否 | 退税率 |
| open1688ProductVO | object | 否 | 1688供应商产品VO |
| attachmentIds | array<int> | 否 | 附件id集合，附件containerType:supplierQuoteFile |
| supplierCode | string | 是 | 供应商编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | int | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "bucklePackage": 0,
    "currency": "CNY",
    "defaultSupplier": 1,
    "deliveryDays": 30,
    "gradientQuote": 0,
    "includePackage": 0,
    "invoiceTaxRate": 0,
    "invoiceType": "not_invoiced",
    "moq": 1000,
    "product": "sku00001",
    "status": 1,
    "supplierCode": "YYSY3",
    "supplierGradientQuotes": [
        {
            "includeTaxPrice": 49.085,
            "unincludeTaxPrice": 49.085
        }
    ],
    "syncDeliveryDays": 0,
    "taxRate": 0
}
```

### 响应示例

```json
{
    "traceId": "open_bcd29ef7ea394752ba86e537587cbcdc",
    "code": 200,
    "data": 605,
    "messages": [
        "request.success"
    ]
}
```

---

## 99. 修改供应商产品

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 修改供应商产品 |
| 请求地址 | `/purchase/srm/supplierSkuQuote/update` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| auditStatusName | string | 否 | 审批状态名称 |
| baseInfoRemark | string | 否 | 基本信息备注 |
| bucklePackage | int | 是 | 是否扣减包材 |
| buyerManager | string | 否 | 采购员 |
| buyerManagerId | string | 否 | 采购员ID |
| createdAt | string | 否 | 创建时间 |
| creater | string | 否 | 创建人 |
| currency | string | 是 | 币种 |
| defaultSupplier | int | 是 | 默认供应商 |
| deliveryDays | int | 是 | 采购交期 |
| editPage | int | 否 | 是否编辑页面 |
| gradientQuote | int | 是 | 是否梯度报价 |
| id | int | 是 | id |
| includePackage | int | 是 | 是否含包材 |
| invoiceTaxRate | number | 是 | 票面税率 |
| invoiceType | string | 是 | 发票类型 |
| invoiceTypeName | string | 否 | 发票类型名称 |
| moq | int | 是 | 最小起订量 |
| product | string | 是 | sku |
| productImageUrl | string | 否 | 产品图片地址 |
| productName | string | 否 | 产品名称 |
| productState | int | 否 | 产品状态 |
| productStateName | string | 否 | 产品状态名称 |
| productType | int | 否 | 产品类型 |
| purchaseUrl | string | 否 | 网址 |
| quoteFlag | int | 否 | 是否重新报价（重新报价需要清理审批流） |
| quoteRemark | string | 否 | 报价备注 |
| status | int | 是 | 状态 |
| supplierCode | string | 是 | 供应商编码 |
| supplierGradientQuoteJson | string | 否 | 报价Json |
| supplierGradientQuotes | array<object> | 是 | 报价，根据gradientQuote区分是否梯度报价 |
| supplierName | string | 否 | 供应商名称 |
| supplierNumber | string | 否 | 供应商货号 |
| supplierWarehouse | int | 否 | 是否是供应商仓 |
| syncDeliveryDays | int | 是 | 是否同步采购交期 |
| taxPrice | number | 否 | 含税单价 |
| taxPriceAmount | object | 否 | 含税单价 |
| taxRate | number | 是 | 税率 |
| taxRebateRate | number | 否 | 退税率 |
| open1688ProductVO | object | 否 | 1688供应商产品VO |
| attachmentIds | array<int> | 否 | 附件id集合，附件containerType:supplierQuoteFile |
| auditStatusCode | string | 否 | 审批状态Code |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 [成功: 0; 失败:1] |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "bucklePackage": 0,
    "currency": "CNY",
    "defaultSupplier": 1,
    "deliveryDays": 0,
    "gradientQuote": 0,
    "id": 605,
    "includePackage": 0,
    "invoiceTaxRate": 0,
    "invoiceType": "not_invoiced",
    "moq": 0,
    "product": "sku00001",
    "status": 1,
    "supplierCode": "YYSY3",
    "supplierGradientQuotes": [
        {
            "includeTaxPrice": 44.5,
            "unincludeTaxPrice": 44.5
        }
    ],
    "syncDeliveryDays": 0,
    "taxRate": 0
}
```

### 响应示例

```json
{
    "traceId": "open_bcd29ef7ea394752ba86e537587cbcdc",
    "code": 200,
    "data": null,
    "messages": [
        "request.success"
    ]
}
```

---

## 100. 查询采购计划列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询采购计划列表 |
| 请求地址 | `/purchase/srm/plan/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| invoicesStateList | array<int> | 否 | 状态集合 [0-草稿，1-审核驳回，2-审核中，3-待下单，4-已作废，5-下单中，6-已完成] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| createdStartDate | date | 否 | 创建开始时间 [yyyy-MM-dd] |
| createdEndDate | date | 否 | 创建结束时间 [yyyy-MM-dd] |
| beginUpdateTime | datetime | 否 | 更新时间开始 [yyyy-MM-dd HH:mm:ss] |
| endUpdateTime | datetime | 否 | 更新时间结束 [yyyy-MM-dd HH:mm:ss] |
| skuList | array<string> | 否 | sku集合（只有一个模糊匹配） |
| mskuList | array<string> | 否 | msku集合（只有一个模糊匹配） |
| fnskuList | array<string> | 否 | fsku集合（只有一个模糊匹配） |
| codeList | array<string> | 否 | 计划单号集合（只有一个模糊匹配） |
| arrvialWarehouseIdList | array<int> | 否 | 目的仓集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 是 | 提示消息 |
| traceId | string | 是 | 链路id |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "total": 1417,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "code": "PL1902180001",
                "reviewerId": 10,
                "memo": "gj test",
                "uuid": "",
                "baseCurrencySymbol": "￥",
                "totalExpectPrice": 0.0,
                "totalPurchaseCostAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0"
                },
                "createdAt": "2019-02-18 11:42:45",
                "reviewerName": "积加测试用户10",
                "totalQuantity": 100,
                "arrivalMarketName": "共享站点",
                "reviewerTime": "2019-02-18 11:44:02",
                "procurementMethod": 0,
                "id": 1,
                "createrId": 10,
                "arrivalMarketId": 0,
                "invoicesStateName": "已完成",
                "invoicesState": 6,
                "totalPurchaseCost": 0.0,
                "arrivalWarehouseId": 1,
                "updateTime": "2022-11-01 19:20:18",
                "transport": 1,
                "createrName": "测试用户",
                "arrivalWarehouseName": "CN_GJ1",
                "totalNum": 1,
                "totalExpectPriceAmount": {
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                }
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 101. 查询采购计划明细

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询采购计划明细 |
| 请求地址 | `/purchase/srm/plan/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 否 | 二者选其一 |
| id | long | 否 | 二者选其一 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 计划详情 |
| messages | array<string> | 是 | 提示信息 |
| traceId | string | 是 | 链路id |

### 请求示例

```json
{
    "code": "PL2301171401"
}
```

### 响应示例

```json
{
    "traceId": "open_e2d6d322c69d4218a9f7e0214d8a77a3",
    "code": 200,
    "data": {
        "transportName": null,
        "code": "PL2301171401",
        "reviewerId": null,
        "transferMarketName": null,
        "processState": null,
        "planItemVoList": [
            {
                "fid": 1401,
                "targetStorageQuantity": null,
                "threePs": 0.0,
                "itemVolume": 0.0,
                "ninetyReturns": null,
                "baseRule": null,
                "inQuantity": 0,
                "rtReservedFcProcessing": null,
                "state": 1,
                "invoicesStateName": null,
                "distributionAccountId": null,
                "brand": "-",
                "invoicesState": null,
                "sixtyPs": 0.0,
                "rtAdjustQuantity": null,
                "thirtyReturns": null,
                "yesterdayReturnPs": null,
                "fourteenPs": 0.0,
                "viewPlanQuantity": 10000,
                "createName": null,
                "rtReservedQuantity": null,
                "sixtyReturnPs": 0,
                "preassemblyQuantity": null,
                "listingLevel": null,
                "yesterdayReturns": null,
                "totalExpectPrice": 0.0,
                "transferQuantity": null,
                "viewShippedTurnover": null,
                "itemTotalVolume": 0.0,
                "selfWarehouses": null,
                "invAge3To6Month": null,
                "fourteenRemove": null,
                "arrivalMarketName": null,
                "assembly": 1,
                "arrivalMarketId": null,
                "viewLotNoQuantity": 0,
                "availableQuantity": null,
                "threeReturns": null,
                "transferWarehouseName": null,
                "realPsRuleGroupName": null,
                "purchaseCost": 2.022,
                "replenishmentQuantity": null,
                "purchaseAccountId": null,
                "viewDeliveryDay": 1,
                "rtUnsellableQuantity": null,
                "expectPrice": 2.022,
                "sixtyReturns": null,
                "inboundReceiving": null,
                "inboundWaitShipped": null,
                "fourteenReturns": null,
                "rtAvailableQuantity": null,
                "rtTransferQuantity": null,
                "alreadyTransferQuantity": null,
                "fnsku": "",
                "sevenPs": 0.0,
                "viewPs28": null,
                "viewAvailableQuantity": 2012,
                "fourteenTs": null,
                "createdAt": null,
                "ps7": null,
                "realPsGroupRule": null,
                "productTypeName": "组合产品",
                "arrvialWarehouseIdList": null,
                "purchaseDeliveryPeriod": 1,
                "viewUnsalableQuantityRate": null,
                "arrivalWarehouseId": 136,
                "fbaProcurementMethod": null,
                "realPsRuleGroupPs": null,
                "flShippedQuantity": null,
                "sixtyTs": null,
                "adjustQuantity": null,
                "poQuantity": 0,
                "viewPs7": null,
                "totalCost": 0.0,
                "assemblySupplierCode": null,
                "thirtyPs": 0.0,
                "invAge0To3Month": null,
                "assemblyJson": null,
                "qualityTime": null,
                "marketId": null,
                "imageUrl": "",
                "productManagerAccountName": "system",
                "sellerSku": null,
                "turnoverR": null,
                "turnover": null,
                "targetStorageTime": null,
                "plQuantity": 10000,
                "turnoverP": null,
                "warehouses": null,
                "rtInQuantity": null,
                "viewPs14": null,
                "viewPurchaseShippedQuantity": null,
                "asin": null,
                "threeTs": null,
                "viewUnsalableQuantity": 0,
                "productManagerAccountId": null,
                "productDeliveryDays": 1,
                "inboundWorking": null,
                "singleQuantity": null,
                "rtInboundReceiving": null,
                "productManagerAccount": "",
                "distributionQuantity": null,
                "memo": null,
                "invAge9To12Month": null,
                "productName": "ANK-A",
                "moq": null,
                "rtPoQuantity": null,
                "stateName": "已分单",
                "sevenTs": null,
                "id": 2969,
                "sku": "ANK-A",
                "ninetyRemove": null,
                "requirementFrom": null,
                "sevenReturns": null,
                "purchaseShippedQuantity": 10000,
                "manualAdjustmentPs": null,
                "distributionTime": null,
                "packageQtyType": null,
                "viewPurchaseQuantity": 0,
                "inIntervalPeriod": 0.0,
                "sixtyRemove": null,
                "transferWarehouseId": null,
                "warehouseId": null,
                "assemblyWarehouseName": null,
                "thirtyTs": null,
                "warehouseType": null,
                "ninetyTs": null,
                "overseasShippedQuantity": null,
                "unsellableQuantity": 0.0,
                "yesterdayTs": null,
                "sevenRemove": null,
                "viewWarehouseTurnover": null,
                "arriveCost": 0.0,
                "usePs": null,
                "rtPlQuantity": null,
                "urgent": 0,
                "planMemo": null,
                "transportTypeDesc": "-",
                "product": null,
                "rtInboundShipped": null,
                "reservedFcProcessing": null,
                "invAge6To9Month": null,
                "arrivalWarehouseName": "0000:广东洁诺",
                "reservedFcTransfer": null,
                "totalExpectPriceAmount": null,
                "realPsGroupRules": null,
                "rtPurchaseShippedQuantity": null,
                "assemblyWarehouseId": null,
                "transportName": "陆运01",
                "rtReservedFcTransfer": null,
                "reservedQuantity": null,
                "invAge12MonthUp": null,
                "repIntervalPeriod": null,
                "thirtyRemove": null,
                "rtFulfillableQuantity": null,
                "shippedTurnover": null,
                "threeRemove": null,
                "repWorkTime": 0.0,
                "viewOverseaQuantity": null,
                "viewTotalTurnover": null,
                "rtFlShippedQuantity": null,
                "packageQuantity": 0.0,
                "msku": "ANK-A",
                "expectDeliveryDate": "2023-01-18",
                "yesterdayRemove": null,
                "totalTurnover": null,
                "viewProductManagerAccountId": 0,
                "ninetyPs": 0.0,
                "unit": "ANK",
                "manualAdjustmentQuantity": null,
                "expectPriceAmount": {
                    "currencyAmount": 2.022,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥2.0220"
                },
                "realPsRuleGroupId": null,
                "yesterdayPs": 0.0,
                "code": null,
                "transportId": 2,
                "requirementFromType": null,
                "thirtyReturnPs": 0,
                "sevenReturnPs": 0,
                "fulfillableQuantity": 2012,
                "assemblyStr": "ANK-A-02{*}1{+}ANK-A-01{*}1",
                "baseCurrencySymbol": "￥",
                "fourteenReturnPs": 0,
                "poCode": "",
                "forecastPs": null,
                "urgentName": "No",
                "viewCnQuantity": null,
                "productMemo": null,
                "productType": 2,
                "viewProductManagerAccount": null,
                "arrIntervalPeriod": null,
                "safeStorageTime": 0.0,
                "quantity": 0,
                "transportDay": null,
                "transport": null,
                "inboundShipped": null,
                "ninetyReturnPs": 0,
                "purchaseCostAmount": null,
                "sellerSkus": null,
                "threeReturnPs": 0,
                "warehousesToSku": null,
                "category": "001-纯牛奶",
                "listingState": null,
                "transportTypeId": null
            },
            {
                "fid": 1401,
                "targetStorageQuantity": null,
                "threePs": 0.0,
                "itemVolume": 0.0,
                "ninetyReturns": null,
                "baseRule": null,
                "inQuantity": 0,
                "rtReservedFcProcessing": null,
                "state": 0,
                "invoicesStateName": null,
                "distributionAccountId": null,
                "brand": "-",
                "invoicesState": null,
                "sixtyPs": 0.0,
                "rtAdjustQuantity": null,
                "thirtyReturns": null,
                "yesterdayReturnPs": null,
                "fourteenPs": 0.0,
                "viewPlanQuantity": 10000,
                "createName": null,
                "rtReservedQuantity": null,
                "sixtyReturnPs": 0,
                "preassemblyQuantity": null,
                "listingLevel": null,
                "yesterdayReturns": null,
                "totalExpectPrice": 36366.3,
                "transferQuantity": null,
                "viewShippedTurnover": null,
                "itemTotalVolume": 0.0,
                "selfWarehouses": null,
                "invAge3To6Month": null,
                "fourteenRemove": null,
                "arrivalMarketName": null,
                "assembly": 1,
                "arrivalMarketId": null,
                "viewLotNoQuantity": 0,
                "availableQuantity": null,
                "threeReturns": null,
                "transferWarehouseName": null,
                "realPsRuleGroupName": null,
                "purchaseCost": 12.1221,
                "replenishmentQuantity": null,
                "purchaseAccountId": null,
                "viewDeliveryDay": 11,
                "rtUnsellableQuantity": null,
                "expectPrice": 12.1221,
                "sixtyReturns": null,
                "inboundReceiving": null,
                "inboundWaitShipped": null,
                "fourteenReturns": null,
                "rtAvailableQuantity": null,
                "rtTransferQuantity": null,
                "alreadyTransferQuantity": null,
                "fnsku": "",
                "sevenPs": 0.0,
                "viewPs28": null,
                "viewAvailableQuantity": 1000,
                "fourteenTs": null,
                "createdAt": null,
                "ps7": null,
                "realPsGroupRule": null,
                "productTypeName": "组合产品",
                "arrvialWarehouseIdList": null,
                "purchaseDeliveryPeriod": 11,
                "viewUnsalableQuantityRate": null,
                "arrivalWarehouseId": 136,
                "fbaProcurementMethod": null,
                "realPsRuleGroupPs": null,
                "flShippedQuantity": null,
                "sixtyTs": null,
                "adjustQuantity": null,
                "poQuantity": 0,
                "viewPs7": null,
                "totalCost": 36366.3,
                "assemblySupplierCode": null,
                "thirtyPs": 0.0,
                "invAge0To3Month": null,
                "assemblyJson": null,
                "qualityTime": null,
                "marketId": null,
                "imageUrl": "",
                "productManagerAccountName": "system",
                "sellerSku": null,
                "turnoverR": null,
                "turnover": null,
                "targetStorageTime": null,
                "plQuantity": 10000,
                "turnoverP": null,
                "warehouses": null,
                "rtInQuantity": null,
                "viewPs14": null,
                "viewPurchaseShippedQuantity": null,
                "asin": null,
                "threeTs": null,
                "viewUnsalableQuantity": 0,
                "productManagerAccountId": null,
                "productDeliveryDays": 11,
                "inboundWorking": null,
                "singleQuantity": null,
                "rtInboundReceiving": null,
                "productManagerAccount": "",
                "distributionQuantity": null,
                "memo": null,
                "invAge9To12Month": null,
                "productName": "ANK-B",
                "moq": null,
                "rtPoQuantity": null,
                "stateName": "未分单",
                "sevenTs": null,
                "id": 2970,
                "sku": "ANK-B",
                "ninetyRemove": null,
                "requirementFrom": null,
                "sevenReturns": null,
                "purchaseShippedQuantity": 10000,
                "manualAdjustmentPs": null,
                "distributionTime": null,
                "packageQtyType": null,
                "viewPurchaseQuantity": 0,
                "inIntervalPeriod": 0.0,
                "sixtyRemove": null,
                "transferWarehouseId": null,
                "warehouseId": null,
                "assemblyWarehouseName": null,
                "thirtyTs": null,
                "warehouseType": null,
                "ninetyTs": null,
                "overseasShippedQuantity": null,
                "unsellableQuantity": 0.0,
                "yesterdayTs": null,
                "sevenRemove": null,
                "viewWarehouseTurnover": null,
                "arriveCost": 0.0,
                "usePs": null,
                "rtPlQuantity": null,
                "urgent": 0,
                "planMemo": null,
                "transportTypeDesc": "-",
                "product": null,
                "rtInboundShipped": null,
                "reservedFcProcessing": null,
                "invAge6To9Month": null,
                "arrivalWarehouseName": "0000:广东洁诺",
                "reservedFcTransfer": null,
                "totalExpectPriceAmount": null,
                "realPsGroupRules": null,
                "rtPurchaseShippedQuantity": null,
                "assemblyWarehouseId": null,
                "transportName": "陆运01",
                "rtReservedFcTransfer": null,
                "reservedQuantity": null,
                "invAge12MonthUp": null,
                "repIntervalPeriod": null,
                "thirtyRemove": null,
                "rtFulfillableQuantity": null,
                "shippedTurnover": null,
                "threeRemove": null,
                "repWorkTime": 0.0,
                "viewOverseaQuantity": null,
                "viewTotalTurnover": null,
                "rtFlShippedQuantity": null,
                "packageQuantity": 0.0,
                "msku": "ANK-B",
                "expectDeliveryDate": "2023-01-28",
                "yesterdayRemove": null,
                "totalTurnover": null,
                "viewProductManagerAccountId": 0,
                "ninetyPs": 0.0,
                "unit": "ANK",
                "manualAdjustmentQuantity": null,
                "expectPriceAmount": {
                    "currencyAmount": 12.1221,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥12.1221"
                },
                "realPsRuleGroupId": null,
                "yesterdayPs": 0.0,
                "code": null,
                "transportId": 2,
                "requirementFromType": null,
                "thirtyReturnPs": 0,
                "sevenReturnPs": 0,
                "fulfillableQuantity": 1000,
                "assemblyStr": "ANK-B-01{*}1{+}ANK-A-02{*}1",
                "baseCurrencySymbol": "￥",
                "fourteenReturnPs": 0,
                "poCode": "",
                "forecastPs": null,
                "urgentName": "No",
                "viewCnQuantity": null,
                "productMemo": null,
                "productType": 2,
                "viewProductManagerAccount": null,
                "arrIntervalPeriod": null,
                "safeStorageTime": 0.0,
                "quantity": 3000,
                "transportDay": null,
                "transport": null,
                "inboundShipped": null,
                "ninetyReturnPs": 0,
                "purchaseCostAmount": null,
                "sellerSkus": null,
                "threeReturnPs": 0,
                "warehousesToSku": null,
                "category": "01-地垫",
                "listingState": null,
                "transportTypeId": null
            }
        ],
        "memo": "",
        "processStateName": null,
        "uuid": "",
        "baseCurrencySymbol": null,
        "totalExpectPrice": null,
        "shippedTurnover": null,
        "createdAt": "2023-01-17 17:20:52",
        "reviewerName": "",
        "attachmentVOList": [],
        "totalQuantity": 3000,
        "purchaseOrderCode": null,
        "arrivalMarketName": "共享站点",
        "reviewerTime": null,
        "fbaWarehouse": false,
        "procurementMethod": 0,
        "id": 1401,
        "createrId": 11371,
        "arrivalMarketId": 0,
        "invoicesStateName": "下单中",
        "turnover": null,
        "invoicesState": 5,
        "totalPurchaseCost": null,
        "transferWarehouseName": null,
        "procurementMethodName": null,
        "arrivalWarehouseId": 136,
        "totalTurnover": null,
        "transport": null,
        "createrName": "广州艾诺科",
        "arrivalWarehouseName": "0000:广东洁诺",
        "transferWarehouseId": null,
        "totalNum": null,
        "attachmentIds": null
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 102. 创建采购订单-草稿状态

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 创建采购订单-草稿状态 |
| 请求地址 | `/purchase/srm/order/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 创建的草稿状态的采购订单 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| customCode | string | 否 | 自定义采购单号 |
| memo | string | 否 | 备注 |
| poItems | array<object> | 是 | 采购订单明细创建API入参 |
| purchaseSubjectId | int | 否 | 采购主体ID |
| supplierCode | string | 是 | 供应商编码 |
| paymentTerms | string | 否 | 付款条件 |
| outerNo | string | 是 | 幂等key [外部唯一标识。不同的采购订单传值需不同。如果传入的值已存在，则返回标识对应的采购订单] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | messages |
| array<string> | 否 | 否 | traceId |
| string | 否 | 否 | int |

### 请求示例

```json
{
    "outerNo": "jijiatest01",
    "customCode": "jijiatest01",
    "supplierCode": "test032801",
    "purchaseSubjectId": 3,
    "poItems": [{
        "arrivalMarketId": 0,
        "arrivalWarehouseId": 1,
        "expectDeliveryDate": "2023-06-16",
        "product": "BM0102025AN026",
        "sellerSku": "BM0102025AN026",
        "orderQuantity": 31,
        "giftQuantity": 0,
        "excludeTaxPrice": 10,
        "actualPrice": 11.3,
        "taxRate": 13,
        "invoiceTaxRate": 13,
        "taxRebateRate": 2,
        "invoiceType": "special_invoice",
        "transportName": "海运",
        "memo": "这个是明细备注",
        "requirementFrom": "积加接口测试"  
    }]
}
```

### 响应示例

```json
{
    "traceId": "open_e77a75b210044c9fbb28cd944396f1cc",
    "code": 200,
    "data": [
        {
            "code": "PO2305190069"
        }
    ],
    "messages": []
}
```

---

## 103. 采购订单-确认待交货

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 采购订单-确认待交货 |
| 请求地址 | `/purchase/srm/order/confirm` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| poCodeList | array<string> | 是 | 草稿状态的采购订单号集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回信息 |
| messages | array<string> | 否 | 接口提示信息 |
| traceId | string | 否 | 链路追踪id |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "poCodeList": ["PO2306010103"]
}
```

### 响应示例

```json
{
    "traceId": "open_2feabbcad499418fb18991b915727de8",
    "code": 200,
    "data": {
        "poCodeList": [
            "PO2306010103"
        ]
    },
    "messages": [
        "确认成功"
    ]
}
```

---

## 104. 查询采购订单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询采购订单列表 |
| 请求地址 | `/purchase/srm/procure/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| codeList | array<string> | 否 | 采购单号 |
| customCode | string | 否 | 自定义单号 |
| customCodeList | array<string> | 否 | 自定义单号集合 |
| supplierCodeList | array<string> | 否 | 供应商code |
| skuList | array<string> | 否 | sku集合 |
| invoicesStatusList | array<int> | 否 | 单据状态 [0-草稿，1-审核驳回，2-审核中，3-待交货，4-已作废，5-变更中，6-交货中，7-全部交货，8-已完成，99-进行中] |
| applyStatus | string | 否 | 请款池申请状态 [un_apply-未申请，partial_apply-部分申请，full_apply-全部申请] |
| createStartDate | datetime | 否 | 创建开始时间 [yyyy-MM-dd HH:mm:ss] |
| createEndDate | datetime | 否 | 创建结束时间 [yyyy-MM-dd HH:mm:ss] |
| beginUpdateTime | datetime | 否 | 更新开始 [yyyy-MM-dd HH:mm:ss] |
| endUpdateTime | datetime | 否 | 更新结束 [yyyy-MM-dd HH:mm:ss] |
| reviewer | string | 否 | 审核人 |
| reviewStartDate | datetime | 否 | 审单时间开始时间 [yyyy-MM-dd HH:mm:ss] |
| reviewEndDate | datetime | 否 | 审单结束开始时间 [yyyy-MM-dd HH:mm:ss] |
| pageInfo | object | 是 | 分页对象 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 提示消息 |
| traceId | string | 否 | 接口返回traceId |

### 请求示例

```json
{
    "pageInfo": {
        "page": 1,
        "pagesize": 10
    }
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "total": 1543,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "parentTotalQuantity": 0,
                "memo": "",
                "childInboundQuantity": 0,
                "totalQuantity": 123,
                "purchaseOtherFee": 0,
                "id": 1905,
                "invoicesStatusName": "草稿",
                "invoicesStatus": 0,
                "paymentRate": 20.0,
                "supervisorId": 10611,
                "paymentStatusStr": "未支付",
                "childTotalQuantity": 123,
                "applyStatusStr": "未申请",
                "supplierCode": "QIXI",
                "paymentType": 1,
                "businessOrderStatusName": "",
                "paymentCycle": 0,
                "currency": "CNY",
                "purchasePlanCode": "PL2302191417",
                "skuSpecies": 1,
                "creator": "周务实",
                "updateTime": "2023-02-19 18:08:41",
                "appliedAmount": 0.0,
                "reviewer": "",
                "childActualQuantity": 0,
                "mergedFlag": 0,
                "totalTaxRebateAmount": 74.53069306930693,
                "createdAt": "2023-02-19 18:08:42",
                "actualQuantity": 0,
                "paymentRuleCode": "FKTJ202205130031",
                "paymentDesc": "",
                "inboundQuantity": 0,
                "financeStatusName": "未请款",
                "applyStatus": "un_apply",
                "supervisor": "上海嘉劭",
                "financeStatus": "un_request",
                "paymentRuleExpireDateType": "order_confirmation_date",
                "code": "PO2302191905",
                "purchaseType": 0,
                "paymentRuleVersion": "V.20220513.0001",
                "paymentStatus": "un_payment",
                "supplierName": "七喜测试",
                "parentActualQuantity": 0,
                "assembleSkuOrder": false,
                "plCreator": "周务实",
                "purchaseTypeName": "普通订单",
                "paymentTypeName": "现结",
                "totalAfterTaxRebateAmount": 3689.269306930693,
                "purchaseAmount": 3763.8,
                "parentInboundQuantity": 0,
                "paymentDate": 0
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 105. 查询采购订单详情

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询采购订单详情 |
| 请求地址 | `/purchase/srm/procure/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| poCode | string | 是 | poCode |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回扩展对象 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "poCode": "PO2302191905"
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "procureItemVos": [
            {
                "packageWeight": 0.2,
                "balanceQuantity": 123,
                "volumeWeight": 0.0,
                "productName": "蓝色游泳圈",
                "orderQuantity": 123,
                "brand": "pp001-四衡",
                "unInboundQuantity": 123,
                "packages": 0.0,
                "isFbaWarehouse": false,
                "totalActualAmount": 0.0,
                "arrivalMarketName": "warehouse.arrival.market.0",
                "currency": "CNY",
                "arrivalMarketId": 0,
                "product": "sku00001",
                "planQuantity": 123,
                "excludeTaxPrice": 30.0,
                "actualQuantity": 0,
                "isDelayDelivery": false,
                "productTypeName": "成品",
                "invoiceType": "special_invoice",
                "productImageUrl": "",
                "arrivalWarehouseId": 139,
                "expectDeliveryDate": "2023-03-13",
                "inboundQuantity": 0,
                "totalExcludeTaxAmount": 3690.0,
                "totalAmount": 3763.8,
                "unit": "个",
                "planExpectDeliveryDate": "2023-03-16",
                "assemblyJson": "",
                "productType": 0,
                "specification": "蓝色",
                "delayExpectDeliveryDate": "2023-03-13",
                "totalExcludeTax": 3690.0,
                "category": "pl0001-日用品",
                "totalPackageWeight": "24.6"
            }
        ],
        "attachmentVOList": [],
        "warehouseProcureItemVos": [
            {
                "procureItemVos": [
                    {
                        "fid": 1905,
                        "packageWeight": 0.2,
                        "balanceQuantity": 123,
                        "volumeWeight": 0.0,
                        "productName": "蓝色游泳圈",
                        "orderQuantity": 123,
                        "purchaseUrl": "",
                        "reduceQuantity": 0,
                        "id": 4267,
                        "state": 0,
                        "brand": "pp001-四衡",
                        "planSources": [
                            {
                                "plCode": "PL2302191417",
                                "plCreater": "周务实"
                            }
                        ],
                        "unInboundQuantity": 123,
                        "giftFlag": 0,
                        "includePackageName": "是",
                        "plCreater": "周务实",
                        "packages": 0.0,
                        "invoiceTypeName": "专票",
                        "planIds": "PL2302191417",
                        "isFbaWarehouse": false,
                        "productNamePrint": "",
                        "actualPrice": 30.6,
                        "supplierNumber": "",
                        "listingLevel": "",
                        "supplierCode": "QIXI",
                        "arrivalMarketName": "共享站点",
                        "assembly": 0,
                        "currency": "CNY",
                        "arrivalMarketId": 0,
                        "urgent": 0,
                        "product": "sku00001",
                        "drawbackTaxPrice": 29.9941,
                        "assemblySite": "",
                        "planQuantity": 123,
                        "arrivalWarehouseName": "QIXICANG",
                        "transportName": "陆运01",
                        "excludeTaxPrice": 30.0,
                        "fnsku": "",
                        "actualQuantity": 0,
                        "isDelayDelivery": false,
                        "productTypeName": "成品",
                        "invoiceType": "special_invoice",
                        "productImageUrl": "",
                        "arrivalWarehouseId": 139,
                        "expectDeliveryDate": "2023-03-13",
                        "deliveryWarehouseId": 139,
                        "inboundQuantity": 0,
                        "invoiceTaxRate": 1.0,
                        "taxRebateRate": 2.0,
                        "deliveryWarehouseName": "QIXICANG",
                        "totalAmount": 3763.8,
                        "taxRate": 2.0,
                        "unit": "个",
                        "planExpectDeliveryDate": "2023-03-16",
                        "childSources": "-",
                        "planMarketId": 0,
                        "code": "PO2302191905",
                        "includePackage": 1,
                        "increaseQuantity": 0,
                        "sellerSku": "sku00001",
                        "productType": 0,
                        "supplierName": "七喜测试",
                        "assembleRule": "",
                        "packagePrice": 0.0,
                        "transport": 2,
                        "delayExpectDeliveryDate": "2023-03-13",
                        "invoiceExcludetaxPrice": 30.297,
                        "taxPrice": 0.6,
                        "totalExcludeTax": 3690.0,
                        "asin": "",
                        "category": "pl0001-日用品",
                        "listingState": ""
                    }
                ],
                "warehouseId": 139,
                "deliveryWarehouseId": 139,
                "warehouseType": "NotFBA",
                "arrivalMarketId": 0,
                "warehouseName": "QIXICANG",
                "deliveryWarehouseName": "QIXICANG"
            }
        ]
    }
}
```

---

## 106. 采购订单快捷入库-查询待入库列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 采购订单快捷入库-查询待入库列表 |
| 请求地址 | `/purchase/srm/quickInbound/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<string> | 否 | 采购单号集合，最外层为数组[最大100条]，传参请参考请求示例 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | array<object> | 是 | 接口返回数据 |
| messages | array<double> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
[
    "PO2303211965"
]
```

### 响应示例

```json
{
    "traceId": "open_b17d724d3b0d45f999f9aecbfa34648f",
    "code": 200,
    "data": [
        {
            "supplierName": "广州X公司",
            "arrivalWarehouseId": 95,
            "deliveryWarehouseId": 95,
            "supplierCode": "SC599",
            "quickInboundListItemVOS": [
                {
                    "product": "BX001",
                    "brandName": "-",
                    "quickInboundLocationVO": null,
                    "returnQuantity": null,
                    "fnsku": "",
                    "giftFlag": 0,
                    "productSmallImageUrl": "",
                    "inboundQuantity": null,
                    "categoryName": "HSL02-采购件",
                    "productName": "1号彩盒",
                    "orderQuantity": 2,
                    "poItemId": 4339,
                    "productTypeName": "包材",
                    "asin": "",
                    "sellerSku": "BX001",
                    "alreadyDeliveryQuantity": 0,
                    "category": "HSL02",
                    "alreadyInboundQuantity": 0,
                    "urgent": 0,
                    "brand": "",
                    "productType": 1
                }
            ],
            "poId": 1965,
            "deliveryWarehouseName": "CHC_CN",
            "mergedFlag": 0,
            "arrivalWarehouseName": "CHC_CN",
            "arrivalMarketName": "共享",
            "poCode": "PO2303211965",
            "warehouseType": "CN",
            "arrivalMarketId": 0
        }
    ],
    "messages": []
}
```

---

## 107. 采购订单快捷入库-确认入库

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 采购订单快捷入库-确认入库 |
| 请求地址 | `/purchase/srm/quickInbound/confirm` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 最外层为数组，传参请参考请求示例 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
[
    {
        "deliveryWarehouseId": 728,
        "deliveryWarehouseName": "AJ_CN",
        "arrivalMarketId": 0,
        "arrivalMarketName": "共享",
        "poId": 9968,
        "poCode": "PO2*****68",
        "arrivalWarehouseId": 728,
        "arrivalWarehouseName": "AJ_CN",
        "supplierCode": "test01001",
        "supplierName": "测试用供应商001",
        "warehouseType": "CN",
        "quickInboundListItemVOS": [
            {
                "alreadyInboundQuantity": 220,
                "asin": "",
                "brand": "",
                "brandName": "-",
                "category": "*****",
                "categoryName": "*****",
                "fnsku": "",
                "inboundQuantity": 1,
                "orderQuantity": 999,
                "poItemId": 19612,
                "product": "BG-RSH-0033-US",
                "productName": "热************in",
                "productType": 0,
                "productTypeName": "成品",
                "returnQuantity": 1,
                "quickInboundLocationVO": null,
                "productSmallImageUrl": null,
                "quickInboundLocations": null,
                "sellerSku": "B**********-US"
            }
        ]
    }
]
```

### 响应示例

```json
{
    "traceId": "open_ae2b22e3a1a644329d0594dd356e8dab",
    "code": 200,
    "data": null,
    "messages": [
        "快捷入库成功！"
    ]
}
```

---

## 108. 采购订单快捷入库-确认入库V2

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 采购订单快捷入库-确认入库V2 |
| 请求地址 | `/purchase/srm/quickInbound/confirm/V2` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | 自动完成采购-交货-发货-入库流程 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 最外层结构为：array<object>，传参请参考示例 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | array<object> | 否 | 接口返回数据 |
| messages | string | 否 | 提示信息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
[
    {
        "poCode": "PO2312045048",
        "memo": "",
        "overMemo": "入库量超收时，必填备注，新增采购变更单记录",
        "inboundItemDTOList": [
            {
                "poItemId": 31173,
                "inboundQuantity": 1,
                "returnQuantity": 0,
                "inboundLocationDTOList": [
                    {
                        "locationId": 0,
                        "quantity": 2
                    }
                ]
            }
        ]
    }
]
```

### 响应示例

```json
{}
```

---

## 109. 采购订单变更单新增+自动审核

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 采购订单变更单新增+自动审核 |
| 请求地址 | `/purchase/srm/procureChange/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| memo | string | 是 | 备注 |
| procureChangeItems | array<object> | 是 | 变更单详情集合 |
| poCode | string | 是 | 采购订单号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | number | 是 | 接口返回响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示信息 |
| traceId | string | 否 | 接口返回traceId |

### 请求示例

```json
{
  "poCode": "PO******16",
  "memo": "**********",
  "procureChangeItems": [
    {
      "arrivalWarehouseId": 60,
      "newExcludeTaxPrice": 13.72,
      "sku": "S******S"
    }
  ]
}
```

### 响应示例

```json
{
  "traceId": "open_ae2b22e3a1a644329d0594dd356e8dab",
  "code": 200,
  "data": {
    "creator": "manager",
    "code": "POC****0176",
    "customRelevanceCode": null,
    "reviewerId": null,
    "creatorId": 2,
    "updateAt": "2023-03-23 17:45:16",
    "memo": "******更",
    "relevanceCode": "PO****16",
    "supplierCode": "default-supplier",
    "reviewer": null,
    "procureChangeItems": [
      {
        "fid": 176,
        "relevanceItemId": 54,
        "newActualPrice": 15.93,
        "excludeTaxPrice": 1,
        "fnsku": "",
        "actualPrice": 1,
        "overReceiveLotNoItemId": null,
        "memo": "接口变更",
        "orderQuantity": 160,
        "newOrderQuantity": 160,
        "overReceiveFlag": null,
        "actualQuantity": 0,
        "newTaxRebateRate": 0,
        "invoiceType": "not_invoiced",
        "id": 211,
        "sku": "S******US",
        "newInvoiceType": "not_invoiced",
        "productType": 0,
        "newInvoiceTaxRate": 0,
        "arrivalWarehouseId": 60,
        "msku": "SG*****S",
        "newInvoiceExcludetaxPrice": 15.93,
        "drawbackTaxPrice": 15.93,
        "planQuantity": 160,
        "newTaxRate": 0,
        "changeType": 0,
        "newExcludeTaxPrice": 15.93,
        "invoiceTaxRate": 0,
        "taxRebateRate": 0,
        "taxRate": 0,
        "invoiceExcludetaxPrice": 1,
        "asin": ""
      }
    ],
    "createdAt": "2023-03-23 17:45:16",
    "currency": "CNY",
    "id": 176,
    "reviewTime": null,
    "status": "under_review"
  },
  "messages": []
}
```

---

## 110. 查询关联采购订单信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询关联采购订单信息 |
| 请求地址 | `/purchase/srm/relevancePoInfo/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 是 | 采购计划单号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| messages | array<string> | 是 | 接口返回提示消息 |
| data | array<object> | 是 | 接口返回数据 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
	"code": "PL2302211424"
}
```

### 响应示例

```json
{
    "traceId": "open_29d9236471444b21bad77e75f88174f8",
    "code": 200,
    "data": [
        {
            "msku": "GJ ERP_TEST_SKU-4",
            "fnsku": "",
            "plQuantity": 111,
            "skuName": "积加ERP测试产品821515577",
            "poActualQuantity": 0,
            "poCode": "PO2302211917",
            "poQuantity": 111,
            "sku": "GJ ERP_TEST_SKU-4"
        }
    ],
    "message": ""
}
```

---

## 111. 创建采购交货单

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 创建采购交货单 |
| 请求地址 | `/purchase/srm/lotNo/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| arrivalMarketId | int | 是 | 目的站点 |
| consumePackageFlag | int | 否 | 装配出库是否扣减包材 [0-不扣减，1-扣减；委外交货单使用] |
| createLotNoViewItemVos | array | 是 | deliveryDate |
| string | 是 | 否 | deliveryWarehouseId |
| int | 是 | 否 | expectQcDate |
| string | 否 | 否 | fid |
| int | 是 | 否 | isDelivery |
| boolean | 是 | 否 | isQc |
| int | 是 | 否 | memo |
| string | 否 | 否 | overMemo |
| string | 否 | 否 | qcType |
| int | 否 | 否 | quickInboundCreateFlag |
| boolean | 否 | 否 | shipmentDate |
| string | 否 | 否 | supplierWarehousingFlag |
| int | 否 | 否 | trackings |
| string | 否 | 否 | warehouseType |
| string | 否 | 否 | deliveryWarehouseName |
| string | 否 | 否 | supplierCode |
| string | 否 | 否 | supplierName |
| string | 否 | 否 | supplierAsWarehouseFlag |
| int | 否 | 否 | supplierWarehouseIdBySupplierCode |
| int | 否 | 否 | supervisor |
| string | 否 | 否 | deliveryWarehouseMarket |
| string | 否 | 否 | packages |
| int | 否 | 否 | allocateFlag |
| int | 否 | 否 |  |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 提示信息 |
| traceId | string | 是 | 日志跟踪号 |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "allocateFlag": 0,
    "arrivalMarketId": 0,
    "consumePackageFlag": 0,
    "createLotNoViewItemVos": [{
        "actualQuantity": 1,
        "arrivalWarehouseId": 310,
        "arrivalWarehouseName": "CN01",
        "asin": "",
        "balanceQuantity": 122,
        "category": "00",
        "categoryName": "00-凉鞋",
        "estimateBox": 0,
        "fnsku": "",
        "giftFlag": 0,
        "memo": null,
        "orderQuantity": 123,
        "packageWeight": 0.5,
        "planMarketId": 0,
        "product": "131313",
        "productImageUrl": null,
        "productName": "子件11",
        "productType": 3,
        "productTypeName": "半成品",
        "quantity": 1,
        "sellerSku": "131313",
        "singleQuantity": 0,
        "urgent": 0,
        "volumeWeight": 1.3333,
    }],
    "deliveryDate": "2023-04-04",
    "deliveryWarehouseId": 310,
    "expectQcDate": "",
    "fid": 11078,
    "isDelivery": false,
    "isQc": 0,
    "logisticsCode": null,
    "memo": null,
    "overMemo": "",
    "packages": null,
    "qcType": 0,
    "quickInboundCreateFlag": false,
    "shipmentDate": "2023-04-04",
    "srmWorkflowDTO": {
        "nextNodeUserId": 0
    },
    "supplierWarehousingFlag": 0,
    "trackings": null,
    "warehouseType": "CN",
    "deliveryWarehouseName": "CN01",
    "supplierCode": null,
    "supplierName": "电子商务有限公司",
    "supplierAsWarehouseFlag": null,
    "supplierWarehouseIdBySupplierCode": 45,
    "supervisor": null,
    "deliveryWarehouseMarket": "310_0"
}
```

### 响应示例

```json
{
    "code": 0,
    "data": {
        "code": "LN2304037671"
    },
    "messages": ["请求成功"],
    "traceId": "abc-def-123"
}
```

---

## 112. 查询交货单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询交货单列表 |
| 请求地址 | `/purchase/srm/lotno/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| code | string | 否 | 交货单号 |
| codeList | array<string> | 否 | 交货单号集合，一次建议不要超过50 |
| skuList | array<string> | 否 | sku集合 |
| deliveryWarehouseId | long | 否 | 交货仓ID |
| lotNoStateList | array<int> | 否 | 单据状态 [0-待质检，1-质检中，2-待发货，3-已发货，4-已完成，5-已作废，6-入库中，99-进行中] |
| beginCreatedAt | date | 否 | 创建开始时间 [yyyy-MM-dd] |
| endCreatedAt | date | 否 | 创建结束时间 [yyyy-MM-dd] |
| beginUpdateTime | datetime | 否 | 更新开始时间 [yyyy-MM-dd HH:mm:ss] |
| endUpdateTime | datetime | 否 | 更新结束时间 [yyyy-MM-dd HH:mm:ss] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "total": 3206,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "qcType": 1,
                "memo": "SELF;",
                "domesticLogisticsCostAmountObj": {
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "warehousingAmountObj": {
                    "currencyAmount": 6949.8,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥6949.8"
                },
                "createdAt": "2019-02-18 11:56:32",
                "deliveryAmountObj": {
                    "currencyAmount": 6949.8,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥6949.8"
                },
                "warehousingDate": "2019-02-18",
                "id": 1,
                "auditStatusName": "审核通过",
                "warehousingQuantity": 99,
                "deliveryWarehouseId": 1,
                "totalValueAmountObj": {
                    "currencyAmount": 0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0"
                },
                "totalValueWarehousingAmount": 0,
                "packages": 5,
                "deliveryWarehouseName": "CN_GJ1",
                "lotNoState": 4,
                "creater": "测试用户",
                "warehouseType": "CN",
                "needQc": true,
                "code": "LN1902180001",
                "totalValueWarehousingAmountObj": {
                    "currencyAmount": 0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0"
                },
                "deliveryAmount": 6949.8,
                "supplierCode": "GJ_S1",
                "paymentType": 1,
                "poCode": "PO1902180001",
                "deliveryQuantity": 99,
                "currency": "CNY",
                "arrivalMarketId": 0,
                "deliveryDate": "2019-02-19",
                "skuSpecies": 1,
                "supplierName": "义乌",
                "dlCodes": [
                    "DL2002210651"
                ],
                "quantity": 99,
                "paymentTypeName": "现结",
                "updateTime": "2022-11-01 19:20:18",
                "lotNoStateName": "已完成",
                "reviewer": "",
                "totalVolumeWeight": 0.0,
                "warehousingAmount": 6949.8,
                "totalValueAmount": 0,
                "auditStatus": 2,
                "totalPackageWeight": 0.0,
                "qcTypeName": "工厂",
                "customPoCode": ""
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 113. 查询交货单明细

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询交货单明细 |
| 请求地址 | `/purchase/srm/lotNo/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 是 | 交货单号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "code": "LN1902180001"
}
```

### 响应示例

```json
{
    "code": 200,
    "data": {
        "memo": "SELF;",
        "domesticLogisticsCostAmountObj": {
            "currencySymbol": "￥",
            "currencyCode": "CNY"
        },
        "warehousingAmountObj": {
            "currencyAmount": 6949.8,
            "currencySymbol": "￥",
            "currencyCode": "CNY",
            "amountWithSymbol": "￥6949.8000"
        },
        "createdAt": "2019-02-18 11:56:32",
        "deliveryAmountObj": {
            "currencyAmount": 6949.8,
            "currencySymbol": "￥",
            "currencyCode": "CNY",
            "amountWithSymbol": "￥6949.8000"
        },
        "lotnoItemVOList": [
            {
                "fid": 1,
                "excludeTaxPrice": 0.0,
                "fnsku": "FNGJX0000382",
                "qcStatus": "",
                "packageWeight": 0.0,
                "volumeWeight": 0.0,
                "poItemId": 3,
                "actualTotalPriceAmount": {
                    "currencyAmount": 6949.8,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥6949.8"
                },
                "invoiceType": "",
                "warehousingDate": "2019-02-18 12:06:31",
                "id": 1,
                "brand": "-",
                "deliveryFlag": -1,
                "receiveMemo": "",
                "taxFlag": 0,
                "arrivalWarehouseId": 1,
                "warehousingQuantity": 99,
                "giftFlag": 0,
                "expectDeliveryDate": "2019-03-05",
                "poBalanceQuantity": 0,
                "deliveryWarehouseId": 1,
                "actualTotalPrice": 6949.8,
                "invoiceTaxRate": 0.0,
                "taxRebateRate": 0.0,
                "taxRate": 0.0,
                "warehousingPriceAmount": {
                    "currencyAmount": 6949.8,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥6949.8"
                },
                "listingLevel": "",
                "categoryName": "-",
                "qcReturnQuantity": 0,
                "poCode": "PO1902180001",
                "deliveryQuantity": 99,
                "currency": "CNY",
                "sellerSku": "jp327a",
                "warehousingPrice": 6949.8,
                "arrivalMarketId": 0,
                "product": "jp327a",
                "quantity": 99,
                "drawbackTaxPrice": 0.0,
                "packagePrice": 0.0,
                "arrivePriceAmount": {
                    "currencyAmount": 70.2,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥70.2"
                },
                "deliveryMemo": "数量少1",
                "planCode": "PL1902180001",
                "arrivalWarehouseName": "CN_GJ1",
                "arrivePrice": 70.2,
                "invoiceExcludetaxPrice": 0.0,
                "asin": "",
                "category": "-",
                "listingState": ""
            }
        ],
        "warehousingDate": "2019-02-18",
        "id": 1,
        "auditStatusName": "审核通过",
        "warehousingQuantity": 99,
        "deliveryWarehouseId": 1,
        "totalValueAmountObj": {
            "currencySymbol": "￥",
            "currencyCode": "CNY"
        },
        "packages": 5,
        "deliveryWarehouseName": "CN_GJ1",
        "lotNoState": 4,
        "creater": "测试用户",
        "warehouseType": "CN",
        "needQc": true,
        "code": "LN1902180001",
        "totalValueWarehousingAmountObj": {
            "currencySymbol": "￥",
            "currencyCode": "CNY"
        },
        "deliveryAmount": 6949.8,
        "supplierCode": "GJ_S1",
        "deliveryDetailsVoList": [
            {
                "product": "jp327a",
                "dlCode": "DL2002210651",
                "quantity": 99,
                "fnsku": "FNGJX0000382",
                "giftFlag": 0,
                "receiptQuantity": 99,
                "balanceQuantity": 0,
                "categoryName": "-",
                "asin": "",
                "sellerSku": "jp327a"
            }
        ],
        "paymentType": 1,
        "attachmentVOList": [],
        "poCode": "PO1902180001",
        "deliveryQuantity": 99,
        "currency": "CNY",
        "arrivalMarketId": 0,
        "deliveryDate": "2019-02-19",
        "skuSpecies": 1,
        "supplierName": "义乌",
        "inboundDetailsVoList": [
            {
                "product": "jp327a",
                "fnsku": "FNGJX0000382",
                "giftFlag": 0,
                "inboundDate": "2019-02-18",
                "inboundQuantity": 99,
                "categoryName": "-",
                "ibCode": "IB1902180001",
                "inboundCreator": "测试用户",
                "asin": "",
                "sellerSku": "jp327a"
            }
        ],
        "quantity": 99,
        "logsList": [
            {
                "fid": 1,
                "op": "InboundPart",
                "content": "积加ERP日志",
                "recordDate": "2019-02-18 12:06:31",
                "account": "测试用户"
            },
            {
                "fid": 1,
                "op": "InboundPart",
                "content": "积加ERP日志",
                "recordDate": "2019-02-18 12:06:31",
                "account": "测试用户"
            }
        ],
        "paymentTypeName": "现结",
        "lotNoStateName": "已完成",
        "totalVolumeWeight": 0.0,
        "warehousingAmount": 6949.8,
        "auditStatus": 2,
        "totalPackageWeight": 0.0,
        "customPoCode": ""
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 114. 交货单（待发货状态）快捷入库

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 交货单（待发货状态）快捷入库 |
| 请求地址 | `/purchase/srm/quickInboundByCode/confirm` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 是 | 交货单号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | int | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "code": "*******"
}
```

### 响应示例

```json
{
    "traceId": "open_21afd1e6d43**********7e9c3ae",
    "code": 200,
    "data": null,
    "messages": [
        "交货单-快捷入库成功"
    ]
}
```

---

## 115. 查询采购退货单列表V2

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询采购退货单列表V2 |
| 请求地址 | `/fulfillment/store/storageReturn/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大500条/页] |
| createTimeStart | date | 否 | 创建开始时间 [yyyy-MM-dd] |
| createTimeEnd | date | 否 | 创建结束时间 [yyyy-MM-dd] |
| processTimeStart | date | 否 | 处理时间开始 [yyyy-MM-dd] |
| processTimeEnd | date | 否 | 处理时间结束 [yyyy-MM-dd] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| data | object | 是 | 返回数据 |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page":1,
    "pagesize":10
}
```

### 响应示例

```json
{
    "traceId": "open_327d9c2410e248aeb6f71891bc108374",
    "code": 200,
    "data": {
        "total": 55,
        "rows": [
            {
                "purchaseCode": "",
                "code": "RG2305040117",
                "purchaseSubjectName": null,
                "refundStatus": "progressRefund",
                "memo": null,
                "warehouseName": "ANNKE_01",
                "statusName": "已处理",
                "refundCurrency": "CNY",
                "id": 117,
                "fcode": "",
                "deliveryCode": "",
                "supplierName": "安科采购",
                "refundableAmount": 121.0,
                "creator": "深圳市鸿鹄集",
                "completedRefundAmount": 0.0,
                "remainingRefundAmount": 120.0,
                "returnTypeName": "库存退货",
                "initiatedRefundAmount": 1.0,
                "warehouseId": 166,
                "returnNum": 11,
                "createTime": "2023-05-04 19:04:38",
                "lnCode": "",
                "refundCurrencySymbol": "￥",
                "progressRefundAmount": 1.0,
                "refundStatusName": "退款中",
                "items": [
                    {
                        "purchaseCode": "",
                        "msku": "AA-DW81KD000-V4-OP",
                        "fnsku": "",
                        "outNum": "0",
                        "memo": "",
                        "storageStatus": "normal",
                        "supplementQuantity": 0,
                        "purchasePrice": {
                            "currencySymbol": "￥"
                        },
                        "returnPrice": {
                            "currencySymbol": "￥"
                        },
                        "productName": "录像机 5MP-N 5合1 澳规 PAL",
                        "returnNum": 11,
                        "lnCode": "",
                        "asin": "",
                        "sku": "AA-DW81KD000-V4-OP",
                        "returnAmount": {
                            "currencySymbol": "￥"
                        },
                        "interceptQuantity": 0,
                        "deliveryCode": ""
                    }
                ],
                "returnType": "inventory_return",
                "status": "processed"
            }
        ]
    },
    "messages": []
}
```

---

## 116. 查询采购主体

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询采购主体 |
| 请求地址 | `/purchase/srm/purchaseSubject/list` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 返回数据 |
| messages | array<string> | 否 | 提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{}
```

---

## 117. 查询自定义物流商列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询自定义物流商列表 |
| 请求地址 | `/fulfillment/ship/customSupplier/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| startUpdateTime | date | 否 | 开始修改时间 [yyyy-MM-dd] |
| endUpdateTime | date | 否 | 结束修改时间 [yyyy-MM-dd] |
| status | int | 否 | 物流商状态 [0-禁用，1-启用] |
| supplierCode | string | 否 | 物流商编码 |
| supplierType | string | 否 | 物流商类型 [supplier_first-头程物流，supplier_self-自发货物流] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "page": 1,
  "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_e24d0ac8bc9d447aa3238db87fb5159c",
    "code": 200,
    "data": {
        "total": 32,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "receiptList": null,
                "remark": "",
                "createUserName": "积加测试用户1",
                "supplierCode": "A0001",
                "uuid": "supplier_self1",
                "paymentType": null,
                "buyerManagerId": 2,
                "supplierApiType": null,
                "feeSubjectId": null,
                "paymentRuleCode": null,
                "id": 1,
                "supplierName": "九方",
                "supplierAddress": null,
                "thirdWarehouse": null,
                "logisticsTimelinessName": "标准型",
                "logisticsTimeliness": 1,
                "paymentTypeName": null,
                "feeSubjectName": null,
                "updateTime": "2022-11-20 21:17:56",
                "paymentRuleName": null,
                "supplierTypeName": "自发货物流",
                "contactList": null,
                "createUser": 1,
                "supplierType": "supplier_self",
                "buyerManager": "积加测试用户2",
                "status": 1
            }
        ]
    },
    "messages": [
        "操作成功"
    ]
}
```

---

## 118. 查询API物流商列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询API物流商列表 |
| 请求地址 | `/fulfillment/ship/apiSupplier/list` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| customizeNameList | array<string> | 否 | 自定义名称集合 |
| status | int | 否 | 物流商状态 [0-停用，1-启用] |
| supplierApiTypeList | array<string> | 否 | Api物流商类型 [supplier_first-头程物流，supplier_self-自发货物流] |
| supplierCodeList | array<string> | 否 | 物流商编号集合 |
| supplierNameList | array<string> | 否 | 物流商名称集合 |
| authorizeStatus | string | 否 | 授权状态 [authorizer-已授权，un_authorizer-未授权] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<string> | 是 | 接口返回数据 |
| messages | array<string> | 是 | 提示信息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{
    "traceId": "open_e12a3088e64f4f0aa8fdd25b1dd9ec79",
    "code": 200,
    "data": [
        {
            "authorizeTime": "2022-07-07 07:26:54",
            "remark": "",
            "supplierCode": "YT-1",
            "customizeName": "云途",
            "supplierApiType": "supplier_self",
            "id": 3,
            "supplierName": "云途",
            "supplierAddress": "",
            "authorizeStatus": "authorizer",
            "updateTime": "2022-07-07 15:26:54",
            "supplierTypeName": null,
            "supplierType": "supplier_api",
            "status": 1
        }
    ],
    "messages": []
}
```

---

## 119. 物流-查看费用

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 物流-查看费用 |
| 请求地址 | `/fulfillment/ship/deliveryCost/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| codeCreateTimeStart | datetime | 否 | 单据创建时间起始 [若通过codeCreateTime来查询则codes字段为必填，不传不会返回数据] [yyyy-MM-dd HH:mm:ss] |
| codes | array | 否 | 发货单集合 |
| createTimeEnd | datetime | 否 | 费用创建时间结束 [yyyy-MM-dd HH:mm:ss] |
| createTimeStart | datetime | 否 | 费用创建时间起始 [yyyy-MM-dd HH:mm:ss] |
| feeTypes | array | 否 | 费用类型 [estimate-预估，actual-实际] |
| orderStatus | array | 否 | 单据状态 [draft-草稿，in_delivery-提货中，shipped-已出运，receiving-入库中，finished-已完成，cancelled-已作废] |
| page | string | 是 | 页码 [分页查询必须带一个条件，只传分页参数不会返回数据] |
| pagesize | string | 是 | 每页条数 [最大100条/页] |
| codeCreateTimeEnd | datetime | 否 | 单据创建时间结束 [若通过codeCreateTime来查询则codes字段为必填，不传不会返回数据] [yyyy-MM-dd HH:mm:ss] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | traceId |
| string | 否 | 否 | code |
| int | 否 | 否 |  |

### 请求示例

```json
{
    "createTimeEnd":"2023-07-01 00:00:00",
    "createTimeStart":"2023-01-01 00:00:00"
}
```

### 响应示例

```json
{}
```

---

## 120. 查询发货单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询发货单列表 |
| 请求地址 | `/fulfillment/ship/delivery/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| country | string | 否 | 目的国家 |
| createdTimeBegin | date | 否 | 单据创建开始时间 [yyyy-MM-dd] |
| createdTimeEnd | date | 否 | 单据创建结束时间 [yyyy-MM-dd] |
| diffStatus | string | 否 | 收发差异状态 [有差异: YES; 无差异: NO] |
| statusList | array<string> | 否 | 状态集合 [进行中: processing; 草稿: draft; 提货中: in_delivery; 已出运: shipped; 入库中: receiving; 已完成: finished; 已作废: cancelled] |
| updateTimeEnd | datetime | 否 | 更新时间结束 [yyyy-MM-dd HH:mm:ss] |
| updateTimeStart | datetime | 否 | 更新时间开始 [yyyy-MM-dd HH:mm:ss] |
| warehouseIdList | array<int> | 否 | 目的仓库集合 |
| shipmentIds | array<string> | 否 | 货件号 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| confirmShipmentDateBegin | date | 否 | 实际发货日期开始时间 [yyyy-MM-dd] |
| confirmShipmentDateEnd | date | 否 | 实际发货日期结束时间 [yyyy-MM-dd] |
| codeList | array<string> | 否 | 发货单集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_b69ca2b67af845d2b02f7365304cc9c2",
    "code": 200,
    "data": {
        "total": 5123,
        "rows": [
            {
                "country": "CN",
                "estimatedCurrencyCode": "",
                "transportName": "陆运01",
                "confirmShipmentDate": "2023-02-21",
                "isDealDiffQty": false,
                "payer": "self",
                "createdAt": "2023-02-21 19:12:36",
                "ifBop": false,
                "ifPurchaseSplit": false,
                "relevanceCodeList": [
                    {
                        "relevanceQuantity": 120,
                        "code": "LN2302213323",
                        "quantity": 120,
                        "shippedQuantity": 0,
                        "type": "LN",
                        "warehouseName": "QIXICANG"
                    }
                ],
                "createdTime": "2023-02-21 19:12:36",
                "actualCurrencyCode": "",
                "id": 5208,
                "chargeUnitPriceUnit": "",
                "importCompanyName": "",
                "etaRedFlag": true,
                "arrivalWarehouseId": 139,
                "receiptDate": "2023-02-21 11:20:36",
                "cancelActualFee": true,
                "importCompany": "",
                "transportMode": "",
                "warehouseType": "domestic",
                "flagLogisticsFee": 0,
                "estimatedAmount": 0.0,
                "receiveRnQuantity": 0,
                "status": "receiving",
                "chargeWeight": 0.0,
                "code": "DL2302215208",
                "receiptQuantity": 0,
                "box": 0,
                "diffQuantity": 0,
                "expectArrivalDate": "2023-02-21",
                "expectShipmentDate": "2023-02-21",
                "customsClearance": "",
                "receivingAt": "2023-02-21",
                "statusName": "入库中",
                "shipmentDate": "2023-02-21",
                "channelId": 0,
                "isDealReceiptFinished": true,
                "creator": "上海嘉劭",
                "aliOrderNo": "",
                "quantity": 120,
                "chargeUnitPriceUnitSymbol": "",
                "containerType": "",
                "actualAmount": 0.0,
                "chargeWeightUnit": "",
                "fromWarehouseType": "",
                "updateTime": "2023-02-21 19:20:37",
                "transport": "2",
                "receiptRnQuantity": 0,
                "receiveQuantity": 120,
                "flagSecondCostHedge": 0,
                "handleDiffQuantity": 0,
                "fromWarehouseNames": [],
                "warehouseNames": [
                    "QIXICANG"
                ],
                "chargeUnitPrice": 0.0,
                "ifDiffApprove": false
            }
        ]
    },
    "messages": []
}
```

---

## 121. 查询发货单明细

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询发货单明细 |
| 请求地址 | `/fulfillment/ship/delivery/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| needItem | boolean | 否 | 是否需要明细数据 |
| relevanceCodes | array<string> | 否 | 关联单号 |
| shipmentIds | array<string> | 否 | 货件号 |
| statusList | array<string> | 否 | 状态集合 [进行中: processing; 草稿: draft; 提货中: in_delivery; 已出运: shipped; 入库中: receiving; 已完成: finished; 已作废: cancelled] |
| deliveryCodes | array<string> | 否 | 发货单号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
  "needItem": true,
  "deliveryCodes": ["D****72"],
  "statusList": [],
  "shipmentIds": [],
  "relevanceCodes": []
}
```

### 响应示例

```json
{
    "traceId": "open_512381109a3b494b84cc46cae60d0ce5",
    "code": 200,
    "data": [
        {
            "country": "CN",
            "confirmShipmentDate": "2023-02-21",
            "payer": "self",
            "createdAt": "2023-02-21 19:12:36",
            "payment": 0,
            "id": 5208,
            "state": 0,
            "createrId": 10611,
            "deliveryCode": "D****72",
            "receiptMemo": "",
            "importCompanyName": "",
            "arrivalWarehouseId": 139,
            "rnType": 0,
            "receiptDate": "2023-02-21",
            "weight": 0.0,
            "importCompany": "",
            "creater": "****",
            "transportMode": "",
            "flagLogisticsFee": 0,
            "status": "receiving",
            "code": "D******",
            "forecastLogisticsCurrency": "",
            "box": 0,
            "countryId": 0,
            "expectArrivalDate": "2023-02-21",
            "expectShipmentDate": "2023-02-21",
            "customsClearance": "",
            "shipmentDate": "2023-02-21",
            "channelId": 0,
            "aliOrderNo": "",
            "containerType": "",
            "updateTime": "2023-02-21 19:20:37",
            "transport": "2",
            "overReceiptReason": "",
            "flagSecondCostHedge": 0,
            "forecastLogisticsCost": 0.0
        }
    ],
    "messages": []
}
```

---

## 122. 查询FBA货件列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA货件列表 |
| 请求地址 | `/fulfillment/ship/shipment/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| statusList | array<string> | 否 | 单据状态 [卖家已创建货件，但未发货: WORKING; 准备发货: READY_TO_SHIP; 承运人已取件: SHIPPED; 承运人已通知亚马逊运营中心其已知晓货件的存在: IN_TRANSIT; 承运人已将货件配送至亚马逊运营中心: DELIVERED; 货件已在亚马逊运营中心的收货装卸地点登记: CHECKED_IN; 货件已到达亚马逊运营中心，但有部分商品尚未标记为已收到: RECEIVING; 货件已到达亚马逊运营中心，且所有商品已经标记为已收到: CLOSED; 卖家在货件发亚马逊运营中心后取消了货件: CANCELLED; 卖家在将货件发送到亚马逊运营中心之前取消了货件: DELETED; 货件出错，但不是由亚马逊处理的: ERROR] |
| shipmentIdList | array<string> | 否 | 货件号集合 |
| warehouseIds | array<int> | 否 | 目的仓库ID |
| referenceIdList | array<string> | 否 | Reference单号集合 |
| relevanceCode | string | 否 | 关联单号 |
| recordStartDate | date | 否 | 创建日期(开始) [yyyy-MM-dd] |
| recordEndDate | date | 否 | 创建日期(结束) [yyyy-MM-dd] |
| updatedStartDate | date | 否 | 更新日期(开始) [yyyy-MM-dd] |
| updatedEndDate | date | 否 | 更新日期(结束) [yyyy-MM-dd] |
| receivingStartDate | date | 否 | 收货日期(开始) [yyyy-MM-dd] |
| receivingEndDate | date | 否 | 收货日期(结束) [yyyy-MM-dd] |
| typeList | array<string> | 否 | 货件类型：FBA，WFS，AWD |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_6c64f41008c0477cb88a6810703dec20",
    "code": 200,
    "data": {
        "total": 5704,
        "rows": [
            {
                "fbaPackage": 0,
                "type": "FBA",
                "totalBoxes": 0,
                "relevanceCodeQtyByItem": 0,
                "toAddress": "   ,  ( 51F6)",
                "numberOfPackages": 0,
                "labelPrepType": "SELLER_LABEL",
                "quantityDelivered": 0,
                "totalGrossWeight": 0,
                "shipmentDetailVos": [
                    {
                        "fid": 6411,
                        "fnsku": "FNGJX0000010",
                        "labelPrepType": "",
                        "quantityDelivered": 0,
                        "id": 115994,
                        "sku": "TEST_MSKU_GJ ERP-QWE1010",
                        "quantityReceived": 0,
                        "msku": "TEST_MSKU_GJ ERP-QWE1010",
                        "listingTitle": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time K766-BK",
                        "upc": "",
                        "quantityShipped": 100,
                        "warehouseId": 3,
                        "shipToCountryCode": "CA",
                        "reportQuantityReceived": 0,
                        "relevanceCodes": [
                            null
                        ],
                        "quantityDelivery": 0,
                        "receiveShipDiff": 0,
                        "declareReceiveDiff": 0,
                        "declareShipDiff": 100,
                        "gtin": "",
                        "quantityCanDelivered": 100,
                        "areCasesRequired": false,
                        "dlCodeList": [],
                        "asin": "",
                        "quantityPacked": 0
                    }
                ],
                "waitDeliveryQuantity": 100,
                "handleStatus": 0,
                "id": 6411,
                "quantityReceived": 0,
                "updatedAt": "2023-02-22 15:00:42",
                "areCasesRequiredName": "原厂包装",
                "oldFbaPackage": 0,
                "createAccount": "石金电子",
                "deliveryTrackingList": [],
                "quantityShipped": 100,
                "shipFromAddress": "{\"DistrictOrCounty\":\"\",\"AddressLine1\":\"gj erp ship address line 1\",\"PostalCode\":\"75081\",\"City\":\"Richardson\",\"CountryCode\":\"US\",\"StateOrProvinceCode\":\"TX\",\"Name\":\"GJ ERP ship39974\"}",
                "warehouseId": 3,
                "shipToCountryCode": "CA",
                "name": "FBA(2023-02-22 14:42:26) - ",
                "recordAt": "2023-02-22 14:42:35",
                "totalVol": 0,
                "reportQuantityReceived": 0,
                "totalNetWeight": 0,
                "status": "DELETED",
                "relevanceCodeQuantity": 0,
                "receiveShipDiff": 0,
                "labelPrepTypeName": "卖家",
                "decideShip": "YES",
                "fromAddressDTO": {
                    "country": "US",
                    "city": "Richardson",
                    "district": "",
                    "postalCode": "75081",
                    "name": "GJ ERP ship39974",
                    "addressLine1": "gj erp ship address line 1",
                    "addressLine2": "",
                    "state": "TX"
                },
                "declareReceiveDiff": 0,
                "warehouseName": "一号店:CA_FBA",
                "toAddressDTO": {
                    "country": "",
                    "city": "",
                    "postalCode": "",
                    "name": "",
                    "addressLine1": "",
                    "addressLine2": "",
                    "state": ""
                },
                "referenceId": "",
                "marketId": 0,
                "fbaTransport": 0,
                "deliveryQuantity": 0,
                "fromAddress": "GJ ERP ship39974--US TX Richardson  gj erp ship address line 1  75081",
                "centerId": "51F6",
                "carrierType": "",
                "canShip": false,
                "updateTime": "2023-02-22 15:00:41",
                "sellerSkuCount": 1,
                "inboundOrderId": "",
                "marketName": "一号店:CA",
                "createTime": "2023-02-22 14:42:35",
                "shipmentId": "FBA5EA751F60",
                "deliveryCountry": "CA",
                "dlCodeList": [],
                "areCasesRequired": "true",
                "quantityPacked": 0
            }
        ]
    },
    "messages": []
}
```

---

## 123. 查询FBA货件看板

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA货件看板 |
| 请求地址 | `/fulfillment/ship/shipmentData/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页大小(最大100条/每页) |
| shipmentId | string | 否 | 货件ID |
| receivingDateBegin | date | 否 | 开始日期，为收货日期 [yyyy-MM-dd] |
| receivingDateEnd | date | 否 | 结束日期，为收货日期 [yyyy-MM-dd] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_b1659b6aea05462f9c44a89c53ffb206",
    "code": 200,
    "data": {
        "total": 8448,
        "rows": [
            {
                "centerId": "51F6",
                "product": "TEST_MSKU_GJ ERP-QWE1010",
                "fnsku": "FNGJX0000010",
                "diffValue": 100,
                "warehouseName": "一号店:CA_FBA",
                "numberOfPackages": 0,
                "skuName": "",
                "quantityShipped": 100,
                "warehouseId": 3,
                "shipmentId": "FBA5EA751F60",
                "shipToCountryCode": "CA",
                "recordAt": "2023-02-22 14:42:35",
                "sellerSku": "TEST_MSKU_GJ ERP-QWE1010",
                "shipmentName": "FBA(2023-02-22 14:42:26) - ",
                "quantityReceived": 0,
                "status": "DELETED",
                "updatedAt": "2023-02-22 15:00:42"
            }
        ]
    },
    "messages":[]
}
```

---

## 124. 发货单-查看实际费用

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 发货单-查看实际费用 |
| 请求地址 | `/fulfillment/ship/deliveryActualFee/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 是 | code |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "code":"DL2302075193"
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "ifBop": false,
        "costList": [
            {
                "includedcost": "0",
                "billAmountRemain": 3000.0,
                "updateAt": "2023-02-15 09:52:46",
                "dlBusinessName": "丽君跨国货代",
                "businessTime": "2023-02-07 09:52:42",
                "expenseTypekey": "FYX202209220004",
                "paymentAmount": 0.0,
                "expenseShareWaykey": "weight",
                "createdAt": "2023-02-15 09:52:46",
                "billAmount": 0.0,
                "feeSubjectId": 1,
                "paymentRuleCode": "FKTJ202205130040",
                "billStatus": "un_payment",
                "dlBusinessType": "GJ_S9 - 丽君跨国货代",
                "currency": "CNY",
                "id": 5334,
                "accountUsageName": "计入成本并请款",
                "paymentAmountRemain": 3000.0,
                "paymentStatus": "un_apply",
                "expenseType": "其他费用项",
                "amount": 3000.0,
                "dlCode": "DL2302075193",
                "customsBrokerName": "丽君跨国货代",
                "customsBroker": "GJ_S9",
                "currencySymbol": "￥",
                "feeSubjectName": "GJ_TEST_1",
                "feeType": "actual",
                "paymentVersion": "V.20220513.0001",
                "expenseShareWay": "实重(KG)",
                "requestFunds": "0",
                "accountUsage": "cost_payment",
                "defaultcost": "0",
                "creater": "汇深贸易商行",
                "paymentStatusName": "未申请",
                "costSourse": 1,
                "remarks": ""
            }
        ],
        "purchaseDeliveryExpenseitemVoList": [
            {
                "includedcost": "0",
                "billAmountRemain": 3000.0,
                "updateAt": "2023-02-15 01:52:46",
                "dlBusinessName": "丽君跨国货代",
                "paymentAmount": 0.0,
                "billAmount": 0.0,
                "feeSubjectId": 1,
                "paymentRuleCode": "FKTJ202205130040",
                "billStatus": "un_payment",
                "dlBusinessType": "GJ_S9-丽君跨国货代",
                "currency": "CNY",
                "id": 5334,
                "paymentAmountRemain": 3000.0,
                "paymentStatus": "un_apply",
                "expenseType": "其他费用项",
                "amount": 3000.0,
                "dlCode": "DL2302075193",
                "customsBrokerName": "丽君跨国货代",
                "customsBroker": "GJ_S9",
                "feeSubjectName": "GJ_TEST_1",
                "feeType": "actual",
                "expenseTypeKey": "FYX202209220004",
                "expenseShareWayKey": "weight",
                "paymentVersion": "V.20220513.0001",
                "expenseShareWay": "实重(KG)",
                "requestFunds": "未申请",
                "accountUsage": "cost_payment",
                "defaultcost": "0",
                "creater": "汇深贸易商行",
                "remarks": ""
            }
        ]
    }
}
```

---

## 125. 发货单-查看分摊费用

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 发货单-查看分摊费用 |
| 请求地址 | `/fulfillment/ship/deliveryCostShareFee/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 是 | code |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "code":"DL2302075193"
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "logisticsCostShareVO": [
            {
                "fnsku": "",
                "createUserName": "汇深贸易商行",
                "purchasePrice": 30.0,
                "sourceCode": "DL2302075193",
                "shippedquantity": 0,
                "singleVolume": 8.0E-4,
                "rowNum": 0,
                "productTypeName": "半成品",
                "platformSourceCode": "",
                "sku": "20220615",
                "dutyPrice": 0.0,
                "msku": "20220615",
                "relevanceCode": "TF2302072546",
                "feeExpenseType": "FYX202209220004",
                "feeType": "actual",
                "expenseShareWay": "weight",
                "warehouseId": 151,
                "dutyCurrency": "CNY",
                "shopid": 0,
                "feeExpenseName": "其他费用项",
                "shopName": "",
                "purchaseCurrency": "CNY",
                "warehouseName": "USCA2-J1",
                "customExpenseItem": "DL",
                "productCategory": "001-纯牛奶",
                "skuName": "子件B",
                "lastSkuFlag": "N",
                "dlBusinessType": "GJ_S9",
                "currency": "CNY",
                "singleWeight": 0.011,
                "productType": 3,
                "storageSizeL": 10.0,
                "feePrice": 52.1327,
                "quantity": 3,
                "currencySymbol": "￥",
                "updateTime": "2023-02-15 09:52:46",
                "singleVolumeWeight": 0.125,
                "storageSizeW": 15.0,
                "picture": "",
                "feeAmount": 156.3981,
                "createTime": "2023-02-15 09:52:46",
                "asin": "",
                "createUser": 2551,
                "storageSizeH": 5.0
            },
            {
                "fnsku": "",
                "createUserName": "汇深贸易商行",
                "purchasePrice": 27.0,
                "sourceCode": "DL2302075193",
                "shippedquantity": 0,
                "singleVolume": 1.0E-4,
                "rowNum": 1,
                "productTypeName": "成品",
                "platformSourceCode": "",
                "sku": "11113",
                "dutyPrice": 0.0,
                "msku": "11113",
                "relevanceCode": "TF2302072546",
                "feeExpenseType": "FYX202209220004",
                "feeType": "actual",
                "expenseShareWay": "weight",
                "warehouseId": 151,
                "dutyCurrency": "CNY",
                "shopid": 0,
                "feeExpenseName": "其他费用项",
                "shopName": "",
                "purchaseCurrency": "CNY",
                "warehouseName": "USCA2-J1",
                "customExpenseItem": "DL",
                "productCategory": "01-地垫",
                "skuName": "测试产品0624",
                "lastSkuFlag": "N",
                "dlBusinessType": "GJ_S9",
                "currency": "CNY",
                "singleWeight": 0.2,
                "productType": 0,
                "storageSizeL": 8.0,
                "feePrice": 947.8673,
                "quantity": 3,
                "currencySymbol": "￥",
                "updateTime": "2023-02-15 09:52:46",
                "singleVolumeWeight": 0.0133,
                "storageSizeW": 2.0,
                "picture": "",
                "feeAmount": 2843.6019,
                "createTime": "2023-02-15 09:52:46",
                "asin": "",
                "createUser": 2551,
                "storageSizeH": 5.0
            }
        ],
        "logisticsCostShareViewVO": [
            {
                "fnsku": "",
                "createUserName": "汇深贸易商行",
                "purchasePrice": 30.0,
                "sourceCode": "DL2302075193",
                "shippedquantity": 0,
                "singleVolume": 8.0E-4,
                "rowNum": 0,
                "productTypeName": "半成品",
                "platformSourceCode": "",
                "id": 12804,
                "shopId": "0",
                "sku": "20220615",
                "dutyPrice": 0.0,
                "msku": "20220615",
                "relevanceCode": "TF2302072546",
                "feeType": "actual",
                "warehouseId": 151,
                "dutyCurrency": "CNY",
                "shopName": "",
                "purchaseCurrency": "CNY",
                "warehouseName": "USCA2-J1",
                "customExpenseItem": "DL",
                "productCategory": "001-纯牛奶",
                "unitCostShareItems": [
                    {
                        "feeExpenseName": "其他费用项",
                        "feePrice": 52.1327,
                        "expenseShareWay": "weight",
                        "lastSkuFlag": "N",
                        "feeAmount": 156.3981,
                        "currencySymbol": "￥",
                        "currency": "CNY",
                        "feeExpenseType": "FYX202209220004"
                    }
                ],
                "skuName": "子件B",
                "dlBusinessType": "GJ_S9",
                "singleWeight": 0.011,
                "productType": 3,
                "storageSizeL": 10.0,
                "quantity": 3,
                "updateTime": "2023-02-15 09:52:46",
                "singleVolumeWeight": 0.125,
                "storageSizeW": 15.0,
                "picture": "",
                "createTime": "2023-02-15 09:52:46",
                "asin": "",
                "createUser": 2551,
                "storageSizeH": 5.0
            },
            {
                "fnsku": "",
                "createUserName": "汇深贸易商行",
                "purchasePrice": 27.0,
                "sourceCode": "DL2302075193",
                "shippedquantity": 0,
                "singleVolume": 1.0E-4,
                "rowNum": 1,
                "productTypeName": "成品",
                "platformSourceCode": "",
                "id": 12805,
                "shopId": "0",
                "sku": "11113",
                "dutyPrice": 0.0,
                "msku": "11113",
                "relevanceCode": "TF2302072546",
                "feeType": "actual",
                "warehouseId": 151,
                "dutyCurrency": "CNY",
                "shopName": "",
                "purchaseCurrency": "CNY",
                "warehouseName": "USCA2-J1",
                "customExpenseItem": "DL",
                "productCategory": "01-地垫",
                "unitCostShareItems": [
                    {
                        "feeExpenseName": "其他费用项",
                        "feePrice": 947.8673,
                        "expenseShareWay": "weight",
                        "lastSkuFlag": "N",
                        "feeAmount": 2843.6019,
                        "currencySymbol": "￥",
                        "currency": "CNY",
                        "feeExpenseType": "FYX202209220004"
                    }
                ],
                "skuName": "测试产品0624",
                "dlBusinessType": "GJ_S9",
                "singleWeight": 0.2,
                "productType": 0,
                "storageSizeL": 8.0,
                "quantity": 3,
                "updateTime": "2023-02-15 09:52:46",
                "singleVolumeWeight": 0.0133,
                "storageSizeW": 2.0,
                "picture": "",
                "createTime": "2023-02-15 09:52:46",
                "asin": "",
                "createUser": 2551,
                "storageSizeH": 5.0
            }
        ]
    }
}
```

---

## 126. 发货单-查看预估费用

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 发货单-查看预估费用 |
| 请求地址 | `/fulfillment/ship/deliveryFee/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | string | 是 | code |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "code":"DL2212055165"
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "ifBop": false,
        "costList": [
            {
                "includedcost": "0",
                "billAmountRemain": 2000.0,
                "updateAt": "2022-12-05 17:52:34",
                "dlBusinessName": "丽君跨国货代",
                "businessTime": "2022-12-05 17:52:34",
                "expenseTypekey": "FYX202209220001",
                "paymentAmount": 0.0,
                "expenseShareWaykey": "volumeWeight",
                "createdAt": "2022-12-05 17:52:34",
                "billAmount": 0.0,
                "paymentRuleCode": "FKTJ202205130040",
                "billStatus": "un_payment",
                "dlBusinessType": "GJ_S9 - 丽君跨国货代",
                "currency": "CNY",
                "id": 5326,
                "accountUsageName": "计入成本并请款",
                "paymentAmountRemain": 2000.0,
                "paymentStatus": "un_apply",
                "expenseType": "运杂费",
                "amount": 2000.0,
                "dlCode": "DL2212055165",
                "customsBrokerName": "丽君跨国货代",
                "customsBroker": "GJ_S9",
                "currencySymbol": "￥",
                "feeType": "estimate",
                "expenseShareWay": "体积(CBM)",
                "requestFunds": "0",
                "accountUsage": "cost_payment",
                "defaultcost": "0",
                "creater": "汇深贸易商行",
                "paymentStatusName": "未申请",
                "costSourse": 1
            }
        ]
    }
}
```

---

## 127. 查询物流费用金额明细

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询物流费用金额明细 |
| 请求地址 | `/fulfillment/ship/cost/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 发货单集合、时间必传一项 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 |  |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| feeTypes | array<string> | 否 | 费用类型 [estimate：预估， actual：实际] |
| expenseTypes | array<string> | 否 | 费用项code |
| updateTimeStart | datetime | 否 | 费用更新时间起始 [yyyy-MM-dd HH:mm:ss] |
| updateTimeEnd | datetime | 否 | 费用更新时间结束 [yyyy-MM-dd HH:mm:ss] |
| createTimeStart | datetime | 否 | 费用创建时间起始 [yyyy-MM-dd HH:mm:ss] |
| createTimeEnd | datetime | 否 | 费用创建时间结束 [yyyy-MM-dd HH:mm:ss] |
| page | int | 否 | 当前第几页 |
| pagesize | int | 否 | 每页条数 [最大100条/页] |
| codes | array<string> | 否 | 发货单号集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | messages |
| array<string> | 否 | 否 | traceId |
| string | 否 | 否 | int |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "createTimeStart": "2023-06-01 00:00:00",
    "createTimeEnd": "2023-06-30 00:00:00"
}
```

### 响应示例

```json
{
    "traceId": "open_4a30ff89689240a2bc782f0aca15ef6e",
    "code": 200,
    "data": {
        "total": 14,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "includedcost": "0",
                "billAmountRemain": 1.23,
                "updateAt": "2023-06-02 18:08:03",
                "dlBusinessName": "云途",
                "feeRate": null,
                "paymentAmount": 0.0,
                "createdAt": "2023-06-02 18:08:03",
                "billAmount": 0.0,
                "feeSubjectId": 3,
                "paymentRuleCode": "FKTJ202205120796",
                "billStatus": "un_payment",
                "dlBusinessType": "YT-1 - 云途",
                "currency": "CAD",
                "paymentAmountRemain": 1.23,
                "paymentStatus": "un_apply",
                "expenseType": "关税",
                "amount": 1.23,
                "dlCode": "LP2207292044145001",
                "customsBrokerName": "云途",
                "customsBroker": "YT-1",
                "currencySymbol": "CA$",
                "dictId": null,
                "feeType": "actual",
                "expenseTypeKey": "FYX0004",
                "expenseShareWayKey": "quantity",
                "paymentVersion": null,
                "expenseShareWay": "按数量",
                "requestFunds": "0",
                "accountUsage": "expense",
                "defaultcost": "0",
                "creater": "admin",
                "remarks": null
            }
        ]
    },
    "messages": []
}
```

---

## 128. 查询物流费用分摊明细

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询物流费用分摊明细 |
| 请求地址 | `/fulfillment/ship/costShare/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 发货单集合、时间必传一项 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 |  |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| feeTypes | array<string> | 否 | 费用类型 [estimate：预估， actual：实际] |
| expenseTypes | array<string> | 否 | 费用项code |
| updateTimeStart | datetime | 否 | 费用更新时间起始 [yyyy-MM-dd HH:mm:ss] |
| updateTimeEnd | datetime | 否 | 费用更新时间结束 [yyyy-MM-dd HH:mm:ss] |
| createTimeStart | datetime | 否 | 费用创建时间起始 [yyyy-MM-dd HH:mm:ss] |
| createTimeEnd | datetime | 否 | 费用创建时间结束 [yyyy-MM-dd HH:mm:ss] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| codes | array<string> | 否 | 发货单号集合 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | messages |
| array<string> | 否 | 否 | traceId |
| string | 否 | 否 | int |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "createTimeStart": "2023-06-01 00:00:00",
    "createTimeEnd": "2023-06-30 00:00:00"
}
```

### 响应示例

```json
{
    "traceId": "open_1906816ce579499bb33b9d0b715d3a4a",
    "code": 200,
    "data": {
        "total": 32,
        "footer": null,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "serialOutCurrency": null,
                "volumeWeightCoefficient": null,
                "fnsku": "",
                "packUnit": null,
                "feeCurrency": "CAD",
                "purchasePrice": 33.5,
                "packLength": null,
                "sourceCode": "LP2207292044145001",
                "price": null,
                "rowNum": 0,
                "cartonNum": null,
                "id": 78864,
                "shopId": "7",
                "sku": "WSQ-01R",
                "productDutyCurrency": null,
                "dutyPrice": null,
                "deliveryCode": "LP2207292044145001",
                "packingCartonQuantity": null,
                "dutyCostWay": null,
                "singleProductSizeH": 11.5,
                "msku": "",
                "serialEstimateTime": null,
                "singleProductSizeL": 24.5,
                "relevanceCode": "FO2207292043375001",
                "feeExpenseType": "FYX0004",
                "feeType": "actual",
                "singleProductSizeW": 12.0,
                "productDutyPrice": null,
                "cartonUnit": null,
                "volume": 0.0034,
                "customFinanceTypeDTOS": null,
                "warehouseId": 1,
                "dutyCurrency": "CNY",
                "cartonHeight": null,
                "cartonGrossWeight": null,
                "hidden": null,
                "businessTime": null,
                "purchaseCurrency": "CNY",
                "feeRate": null,
                "cartonWidth": null,
                "feeVatPrice": null,
                "marketId": 7,
                "productCategory": "未分配品类",
                "feeDutyPrice": null,
                "cartonLength": null,
                "dlBusinessType": "YT-1",
                "currency": "CNY",
                "singleWeight": 0.27,
                "packHeight": null,
                "productType": 0,
                "feePrice": 33.5,
                "customPrice": null,
                "storageSizeL": 24.5,
                "quantity": 1,
                "feeTransportPrice": null,
                "updateTime": "2023-06-02 18:08:03",
                "singleVolumeWeight": 0.6762,
                "storageSizeW": 12.0,
                "serialOutQuantity": null,
                "serialActualTime": null,
                "packWidth": null,
                "createTime": "2023-06-02 18:08:03",
                "transportCostWay": null,
                "singleCustomPriceJson": null,
                "asin": "",
                "serialOutArriveCost": null,
                "createUser": 1,
                "storageSizeH": 11.5
            }
        ]
    },
    "messages": []
}
```

---

## 129. 查询发货单详情-装箱清单

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询发货单详情-装箱清单 |
| 请求地址 | `/fulfillment/ship/deliveryCarton/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| relateCode | string | 是 | 关联单号 [单号和类型不匹配会报错] |
| itemType | int | 是 | 单据明细类型 [1-交货单，2-调拨单，3-发货单] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 链路追送id |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "itemType": 3,
    "relateCode": "DL2308085455"
}
```

### 响应示例

```json
{
    "traceId": "open_a3e8a85a658a48a69ef6846557992297",
    "code": 200,
    "data": {
        "totalVolume": "0.1980",
        "totalcartonNum": 3,
        "code": "DL2305308222",
        "totalRoughWeight": 39.0,
        "totalLnQuantity": 44,
        "totalLength": 150.0,
        "totalWide": 90.0,
        "totalVolumeWeight": 33.0,
        "encaseType": 2,
        "countryCode": "CN",
        "totalHigh": 132.0,
        "totalWeight": 39.0,
        "totalCartonQuantity": 44,
        "itemCartonVOList": [
            {
                "cartonQuantity": 13,
                "fnsku": "",
                "productCategoryName": "alyt9-三级品类_开放平台父品类传参",
                "lnQuantity": 13,
                "productName": "**********",
                "productCategory": "alyt9",
                "sumSingleNetWeight": 0.0,
                "cartonNum": 1,
                "productTypeName": "成品",
                "sku": "***********",
                "dutyPrice": null,
                "productType": 0,
                "itemCartonViewVoList": [
                    {
                        "itemType": 3,
                        "wide": 30.0,
                        "length": 50.0,
                        "itemId": 34077,
                        "high": 44.0,
                        "boxNo": 1,
                        "boxNum": 13,
                        "relateCode": "DL2305308222",
                        "id": 1077779,
                        "roughWeight": 13.0
                    }
                ],
                "image": "",
                "msku": "**********",
                "arrivalWarehouseId": 728,
                "productId": 8732,
                "isInspectionName": "否",
                "sumSingleGrossWeight": 13.0,
                "isInspection": 0,
                "nquantity": 1,
                "dutyCurrencySymbol": null,
                "singleGrossWeight": 450,
                "itemId": 34077,
                "mquantity": 0,
                "material": "",
                "transferGroup": null,
                "shipmentId": "",
                "englishCustomsName": "",
                "dutyCurrency": "",
                "asin": "",
                "sumVolume": 0.066
            },
            {
                "cartonQuantity": 31,
                "fnsku": "",
                "productCategoryName": "alyt9-三级品类_开放平台父品类传参",
                "lnQuantity": 31,
                "productName": "**********",
                "productCategory": "alyt9",
                "sumSingleNetWeight": 0.0,
                "cartonNum": 2,
                "productTypeName": "成品",
                "sku": "************",
                "dutyPrice": null,
                "productType": 0,
                "itemCartonViewVoList": [
                    {
                        "itemType": 3,
                        "wide": 30.0,
                        "length": 50.0,
                        "itemId": 34078,
                        "high": 44.0,
                        "boxNo": 2,
                        "boxNum": 28,
                        "relateCode": "DL2305308222",
                        "id": 1077780,
                        "roughWeight": 13.0
                    },
                    {
                        "itemType": 3,
                        "wide": 30.0,
                        "length": 50.0,
                        "itemId": 34078,
                        "high": 44.0,
                        "boxNo": 3,
                        "boxNum": 3,
                        "relateCode": "DL2305308222",
                        "id": 1077781,
                        "roughWeight": 13.0
                    }
                ],
                "image": "",
                "msku": "************",
                "arrivalWarehouseId": 728,
                "productId": 8733,
                "isInspectionName": "否",
                "sumSingleGrossWeight": 26.0,
                "isInspection": 0,
                "nquantity": 2,
                "dutyCurrencySymbol": null,
                "singleGrossWeight": 450,
                "itemId": 34078,
                "mquantity": 0,
                "material": "",
                "transferGroup": null,
                "shipmentId": "",
                "englishCustomsName": "",
                "dutyCurrency": "",
                "asin": "",
                "sumVolume": 0.132
            }
        ]
    },
    "messages": []
}
```

---

## 130. 查询FBA货件装箱清单

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA货件装箱清单 |
| 请求地址 | `/fulfillment/ship/shipmentAttachment/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 3次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| shipmentItemQueryDTOS | array<object> | 是 | 批量查询明细 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 返回码 |
| data | array<object> | 是 | 数据 |
| messages | array | 是 | 提示信息 |
| traceId | string | 是 | 请求id |

### 请求示例

```json
{
    "shipmentItemQueryDTOS": [
        {
            "shipmentId": "FBA123456"
        }
    ]
}
```

### 响应示例

```json
{
    "traceId": "open_1ded32c498a04fcfadc3fd5771984d71",
    "code": 200,
    "data": [
        {
            "centerId": "33E8",
            "shipmentId": "FBA123456",
            "name": "FBA(2022-12-13 15:39:21) - ",
            "id": 23519,
            "attachmentId": 123
        }
    ],
    "messages": []
}
```

---

## 131. 批量新增发货单物流轨迹

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 批量新增发货单物流轨迹 |
| 请求地址 | `/fulfillment/ship/deliveryTrack/create` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 最外层为数组，传参请参考请求示例 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | string | 是 | 返回数据 |
| messages | array<string> | 是 | 提示信息 |
| traceId | string | 是 | 链路追踪id |
| code | int | 是 | 响应码 |

### 请求示例

```json
[
    {
        "deliveryInfo": {
            "code": "DL2308177653"
        },
        "deliveryTrackInfoDTOs": [
            {
                "remark": "",
                "relatedCode": "DL2308177653",
                "itemDTOList": [
                    {
                        "ptrackNodeCode": 100000,
                        "trackNodeCode": 100100,
                        "trackTime": "2023-08-28 14:39:13",
                        "trackContent": "下单",
                        "place": "",
                        "city": "",
                        "country": "",
                        "supplierCode": "",
                        "countryName": "",
                        "supplierName": ""
                    }
                ]
            }
        ]
    }
]
```

### 响应示例

```json
{
    "traceId": "open_81d1b59dc24e4ecbb19fc46b0c77317a",
    "code": 200,
    "data": "操作成功",
    "messages": []
}
```

---

## 132. 查询物流方式列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询物流方式列表 |
| 请求地址 | `/fulfillment/ship/transport/list` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| status | string | 否 | 状态：enable、disable |
| shipperCountry | string | 否 | 发货国家 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页大小(最大100条/每页) |
| name | string | 否 | 物流方式 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_979a1935b3c646b9b06bf87c34f2e9a9",
    "code": 200,
    "data": {
        "total": 31,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "volumeWeightCoefficient": 6000,
                "chargeTypeName": "计费重(KG)",
                "shipperCountry": "CN",
                "name": "海运",
                "id": 1,
                "status": "disable"
            }
        ]
    },
    "messages": []
}
```

---

## 133. 发货单编辑

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 发货单编辑 |
| 请求地址 | `/fulfillment/ship/delivery/update` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| shipmentDate | string | 否 | 提货日期 yyyy-MM-dd |
| expectShipmentDate | string | 否 | 预计发货日期 yyyy-MM-dd |
| sailDate | string | 否 | 开船日期 yyyy-MM-dd |
| estimateArrivePortDate | string | 否 | 预计到港日期 yyyy-MM-dd |
| actualArrivePortDate | string | 否 | 实际到港日期 yyyy-MM-dd |
| expectArrivalDate | string | 否 | 预计到仓日期 yyyy-MM-dd |
| actualArrivalDate | string | 否 | 实际到仓日期 yyyy-MM-dd |
| confirmShipmentDate | string | 否 | 实际发货日期 yyyy-MM-dd |
| transport | string | 否 | 物流方式ID（数字） |
| customsClearance | string | 否 | 清关地 |
| trackings | string | 否 | 物流跟踪号 |
| memo | string | 否 | 备注 |
| dlCode | string | 是 | 发货单号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | boolean | 否 | 是否成功 |
| messages | array<string> | 否 | 提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{}
```

---

## 134. 批量查询包裹单详情及费用

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 批量查询包裹单详情及费用 |
| 请求地址 | `/fulfillment/ship/units/detail` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| unitCodeList | array<string> | 否 | 包裹单号集合（建议不超过20个），单号必传一类 |
| foOrderCodeList | array<string> | 否 | 系统单号集合（建议不超过20个），单号必传一类 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 否 | 接口返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{}
```

---

## 135. 查询仓库-FBA仓

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询仓库-FBA仓 |
| 请求地址 | `/purchase/inventory/fbaWarehouse/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| status | string | 否 | 仓库状态[enable-启用，disable-停用] |
| marketName | string | 否 | 店铺名称 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| name | string | 否 | 仓库名称 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_6f72e59e82c1428994598554167e881b",
    "code": 200,
    "data": {
        "total": 27,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "country": "US",
                "closeNaWarehouse": false,
                "transferWarehouseName": "ZJ_HWC",
                "grayUnbundleFlag": false,
                "fbaProcurementMethod": 1,
                "typeName": "FBA",
                "type": "FBA",
                "serverId": 1,
                "fbaProcurementMethodName": "中转",
                "marketName": "一号店--有广告数据",
                "openNaWarehouse": false,
                "sellerId": "gqzezsttdzdunt",
                "transferWarehouseId": 84,
                "name": "US_FBA",
                "statusName": "启用",
                "id": 2,
                "panEurFlag": false,
                "others": "[{\"groupName\":\"Params\",\"name\":\"EndInventorySerialDate\",\"val\":\"2021-12-15\"},{\"groupName\":\"Params\",\"name\":\"MarketId\",\"val\":\"1\"},{\"name\":\"InitStartDate\",\"val\":\"2019-09-16\"},{\"groupName\":\"Params\",\"name\":\"BeginInventorySerialDate\",\"val\":\"2020-05-15\"},{\"name\":\"LastUpdatedAfter\",\"val\":\"2021-12-18T12:05:38Z\"},{\"name\":\"InitFlag\",\"val\":\"NO\"},{\"groupName\":\"Params\",\"name\":\"SerialInitDate\",\"val\":\"2020-02-28\"},{\"name\":\"InitEndDate\",\"val\":\"2020-09-16\"}]",
                "status": "enable"
            }
        ]
    },
    "messages": ["request.success"]
}
```

---

## 136. 查询仓库-自营仓

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询仓库-自营仓 |
| 请求地址 | `/purchase/inventory/selfWarehouse/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| status | string | 否 | 仓库状态[enable-启用，disable-停用] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| name | string | 否 | 仓库名称 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_72cd47f0a5fe48378be360692c93f645",
    "code": 200,
    "data": {
        "total": 56,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "country": "CN",
                "zipCode": "",
                "addressRemark": "",
                "gipAddressVO": {
                    "country": "1",
                    "zipCode": "213456",
                    "city": "2181",
                    "mobile": "123456789000",
                    "phone": "0769276190987",
                    "street": "东莞凤岗的一个好地方",
                    "district": "2202",
                    "company": "我的公司",
                    "state": "2052",
                    "contacts": "啊哈哈"
                },
                "city": "",
                "typeName": "自营",
                "productTransferSubpac": false,
                "type": "SELF",
                "street": "",
                "statusName": "启用",
                "company": "",
                "id": 1,
                "state": "",
                "street2": "",
                "others": "[{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_COUNTRY\",\"val\":\"1\"},{\"groupName\":\"Params\",\"name\":\"EndInventorySerialDate\",\"val\":\"2020-05-15\"},{\"groupName\":\"Params\",\"name\":\"BeginInventorySerialDate\",\"val\":\"2020-05-15\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_COMPANY\",\"val\":\"我的公司\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_STREET\",\"val\":\"东莞凤岗的一个好地方\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_CITY\",\"val\":\"2181\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_STATE\",\"val\":\"2052\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_EMAIL\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_ZIPCODE\",\"val\":\"213456\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_QQ\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_MOBILE\",\"val\":\"123456789000\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_DISTRICT\",\"val\":\"2202\"},{\"groupName\":\"Params\",\"name\":\"SerialInitDate\",\"val\":\"2020-02-28\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_PHONE\",\"val\":\"0769276190987\"},{\"groupName\":\"AddressKey\",\"name\":\"ADDRESS_CONTACTS\",\"val\":\"啊哈哈\"}]",
                "email": "",
                "qq": "",
                "mobile": "",
                "assembleTransferSubpac": false,
                "stateStr": "广东省",
                "phone": "",
                "district": "",
                "name": "CN_GJ1",
                "contacts": "",
                "status": "enable"
            }
        ]
    },
    "messages": ["request.success"]
}
```

---

## 137. 查询仓库-供应商仓

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询仓库-供应商仓 |
| 请求地址 | `/purchase/inventory/supplierWarehouse/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| status | string | 否 | 仓库状态[enable-启用，disable-停用] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| name | string | 否 | 仓库名称 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_04538b7dfcf2423bbf2039558278276d",
    "code": 200,
    "data": {
        "total": 48,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "country": "CN",
                "gipAddressVO": {},
                "name": "GJ_S5:服装鞋帽加工",
                "statusName": "启用",
                "typeName": "供应商",
                "id": 34,
                "type": "SUPPLIER",
                "others": "[{\"groupName\":\"Params\",\"name\":\"EndInventorySerialDate\",\"val\":\"2020-05-15\"},{\"groupName\":\"Params\",\"name\":\"BeginInventorySerialDate\",\"val\":\"2020-05-15\"},{\"groupName\":\"Params\",\"name\":\"SerialInitDate\",\"val\":\"2020-02-28\"}]",
                "status": "enable",
                "createDate": "2020-03-13 21:44:48"
            }
        ]
    },
    "messages": ["request.success"]
}
```

---

## 138. 查询仓库信息列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询仓库信息列表 |
| 请求地址 | `/purchase/store/multiTypeWarehouse/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| model | object | 是 | 查询参数 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 响应码 |
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |

### 请求示例

```json
{
    "model":{},
    "page": 1,
    "pagesize": 20
}
```

### 响应示例

```json
{
    "traceId": "open_67e364ad594c48b7ad49c48b95a12fad",
    "code": 200,
    "data": {
        "total": 140,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "country": "US",
                "zipCode": null,
                "addressRemark": "",
                "city": null,
                "type": "WFS",
                "assembleTransferSubPac": null,
                "street": null,
                "company": null,
                "id": 163,
                "state": "",
                "street2": null,
                "email": null,
                "createDate": "2023-03-15 16:56:02",
                "qq": null,
                "fbaProcurementMethod": null,
                "productTransferSubPac": null,
                "mobile": null,
                "multiMarketId": 14,
                "stateStr": "",
                "transferWarehouseId": null,
                "phone": null,
                "district": null,
                "name": "US_WFS",
                "contacts": null,
                "status": "enable"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 139. 查询库位信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询库位信息 |
| 请求地址 | `/fulfillment/store/location/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大500条/页] |
| status | string | 否 | 状态 [启用: enable; 停用: disable] |
| code | string | 否 | 库位编码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "total": 271,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "code": "01-01",
                "shelfId": 13,
                "creatorId": 10611,
                "warehouseName": "QIXICANG",
                "enabled": "Y",
                "maxContainerSize": 1,
                "reservoirType": "存货区",
                "enabledContainerNumber": "N",
                "id": 151,
                "floor": 1,
                "skuSpecies": 1,
                "warehouseShelfId": 13,
                "whichLayer": "01",
                "shelfCode": "0002",
                "quantity": 54,
                "updateTime": "2022-12-20 20:27:41",
                "maxSkuSize": 99,
                "warehouseAreaId": 6,
                "areaCode": "00002",
                "areaId": 6,
                "createTime": "2022-12-20 20:27:41",
                "warehouseId": 139,
                "lattice": 1,
                "enabledFull": "N",
                "location": "01",
                "locationFullCode": "00002-0002-01-01",
                "status": "enable"
            }
        ]
    }
}
```

---

## 140. 查询入库单列表V2

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询入库单列表V2 |
| 请求地址 | `/fulfillment/store/selfInboundListAndDetail/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| billCodes | array | 否 | 单据号 |
| dateType | string | 否 | 时间类型1-预计到仓 2-收货 3-入库 4 - 创建 |
| startDate | date | 否 | 开始日期 [yyyy-MM-dd]，需传dateType |
| endDate | date | 否 | 结束日期 [yyyy-MM-dd]，需传dateType |
| receiveStatusList | array | 否 | 收货状态 ：WAIT_RECEIVE-待收货；PART_RECEIVE-部分收货；ALL_RECEIVED-全部收货 |
| orderStatusList | array | 否 | 入库状态：WAIT_INBOUND-待入库 PART_INBOUND-部分入库 COMPLETED-已完结 CANCELLED-已取消 |
| arrivalWarehouseIdList | array | 否 | 入库仓集合 |
| rnType | string | 是 | 目的仓类型 0-国内仓 1-海外仓 3-供应商仓 4 - 三方仓 |
| orderType | string | 否 | purchase - 采购入库；transfer - 调拨入库；return - 退货入库 |
| page | int | 是 | 当前第几页 默认0 |
| pagesize | int | 是 | 每页条数 [最大500条/页] |
| billType | string | 否 | billType 1-入库单 2-发货单；3-关联单据（调拨单/交货单）； 4-物流跟踪号 5-采购单号 6 - 质检单 7 - 三方仓单号 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| messages | array<string> | 是 | 提示信息 |
| data | object | 是 | 返回数据 |
| code | int | 是 | 响应码 |
| traceId | string | 是 | 链路ID |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "rnType": 4
}
```

### 响应示例

```json
{
    "traceId": "open_a3c01e2ad22445d6b0c5b19c86ad3cbe",
    "code": 200,
    "data": {
        "total": 5,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "orderType": "purchase",
                "qcType": "NOT_QC",
                "purchaseCode": "PO2302071895",
                "orderItemResultList": [
                    {
                        "returnedNum": 0,
                        "fnsku": "",
                        "orderId": 3061,
                        "sourceItemId": 9200,
                        "categoryName": "ZC-早春系列",
                        "releatedItemId": 4632,
                        "productName": "太平鸟羽绒服",
                        "marketId": 0,
                        "imageUrl": "https://img.app.gerpgo.com/demo%2F2022%2F08%2Fattachments%2Fdemo%2F1660703536294a49cb857de5a40f9a193138bd80c8a75_origin_img_v2_393eebf0-88dc-46ab-9844-a8fded06555g.png",
                        "externalSku": "testinout",
                        "id": 4611,
                        "receiveNum": 0,
                        "sku": "YURONGFU",
                        "brand": "",
                        "productType": "成品",
                        "overReceiveReason": "",
                        "msku": "YURONGFU",
                        "maxReceiveNum": 105,
                        "marketName": "共享",
                        "exceptionNum": 0,
                        "asin": "",
                        "arriveNum": 100,
                        "onShelfNum": 0
                    }
                ],
                "externalExtendData": {
                    "externalOrderNo": "RVC004-20230612-0003",
                    "orderNo": "WV20230505003061",
                    "orderId": 3061,
                    "externalOrderFailMsg": "-",
                    "externalOrderStatusName": "新建",
                    "platformName": "仓搜搜",
                    "externalOrderStatus": "C",
                    "platformCode": "CANGSOSO"
                },
                "orderStatus": "WAIT_INBOUND",
                "remark": "",
                "supplierCode": "001",
                "warehouseName": "USCA2-J1",
                "purchaseCustomCode": "",
                "trackings": "",
                "onShelfOrderList": [],
                "id": 3061,
                "supplierName": "南南服装供应商",
                "sourceRemark": "",
                "orderNo": "WV20230505003061",
                "expectArriveTime": "2023-05-15 00:00:00",
                "receiveTime": null,
                "onShelfTime": null,
                "exceptionNum": 0,
                "warehouseId": 151,
                "createTime": "2023-05-05 10:08:33",
                "qcCode": "",
                "createUser": "云熙科技",
                "releatedCode": "LN2302073310",
                "warehouseType": "THIRD",
                "packageCount": 1,
                "sourceOrderNo": "DL2305055318"
            }
        ]
    },
    "messages": []
}
```

---

## 141. 查询仓库进销存

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询仓库进销存 |
| 请求地址 | `/finance/asset/selfPsi/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| endDate | date | 否 | 结束日期 [yyyy-MM-dd] dateType为DAY时必填 |
| dateType | string | 是 | 日期类型: MONTH、DAY |
| defective | boolean | 是 | 是否是不良品: false/ture |
| month | string | 否 | 月份 [yyyy-MM] dateType为MONTH时必填 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| type | string | 是 | 查询类型：维度 WAREHOUSE, SKU |
| warehouseType | string | 否 | 仓库类型，SELF-自营仓（默认），SUPPLIER-供应商仓，THIRD-三方仓 |
| warehouseIds | array<long> | 否 | 仓库ID集 |
| zeroNotDisplay | boolean | 是 | 余额为0且无发生额不显示 : false/true |
| beginDate | date | 否 | 开始日期 [yyyy-MM-dd] dateType为DAY时必填 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |
| code | number | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20
}
```

### 响应示例

```json
{}
```

---

## 142. FBA进销存-成本

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | FBA进销存-成本 |
| 请求地址 | `/finance/asset/fbaPsi/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| month | string | 是 | 月份 [yyyy-MM] |
| warehouseIds | array<long> | 否 | 仓库ID |
| mskuList | array<string> | 否 | MSKU |
| skuList | array<string> | 否 | SKU |
| warehouseType | string | 否 | 仓库类型：默认EXACT |
| productStatus | string | 否 | 产品状态 |
| type | string | 否 | 查询类型：默认MSKU |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20,
    "month": "2023-02"
}
```

### 响应示例

```json
{
    "traceId": "open_e057f3f9336947f5a48dfa1697488605",
    "code": 200,
    "data": {
        "total": 16661,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "unknownEventsArriveCost": 0.0,
                "beginBookCost": 0.0,
                "customerShipmentsGapPurchaseCost": 0.0,
                "unknownEventsCost": 0.0,
                "endPurchaseCost": 0.0,
                "diffArriveCost": 0.0,
                "beginCost": 0.0,
                "adjustmentsDisposalQuantity": 0,
                "customerReturnPurchaseCost": 0.0,
                "dealDiffPurchaseCost": null,
                "beginQuantityGapCost": 0.0,
                "smAccountName": "",
                "sku": null,
                "customerOrderCost": 0.0,
                "shipmentsDateRangeQuantityGap": null,
                "customerReturnsArriveCost": 0.0,
                "adjustmentsDisposalPurchaseCost": 0.0,
                "bookDiffPurchaseCost": 0.0,
                "adjustmentsDamagedCost": 0.0,
                "customerReturnQuantity": 0,
                "removalReturnArriveCost": 0.0,
                "endBookArriveCost": 0.0,
                "warehouseTransferInOutPurchaseCost": 0.0,
                "adjustmentsFoundArriveCost": 0.0,
                "beginQuantityGapArriveCost": 0.0,
                "inventoryReceiptsArriveCost": 0.0,
                "tbShippedArriveCost": 0.0,
                "adjustmentsLostQuantity": 0,
                "endBookPurchaseCost": 0.0,
                "warehouseId": 2,
                "tbShippedQuantity": 0,
                "adjustmentsOtherQuantity": 0,
                "removalReturnPurchaseCost": 0.0,
                "customerReturnsQuantity": 0,
                "customerShipmentsArriveCost": 0.0,
                "adjustmentsDamagedPurchaseCost": 0.0,
                "beginPurchaseCost": 0.0,
                "endQuantity": 0,
                "endArriveCost": 0.0,
                "fbaShippedCost": 0.0,
                "adjustmentsDisposalArriveCost": 0.0,
                "unknownEventsPurchaseCost": 0.0,
                "unknownEventsQuantity": 0,
                "warehouseName": "Zingtto:US_FBA",
                "beginQuantityGapPurchaseCost": 0.0,
                "fbaShippedPurchaseCost": 0.0,
                "erpShippedArriveCost": 0.0,
                "warehouseTransferInOutCost": 0.0,
                "transitBetweenWarehousePurchaseCost": 0.0,
                "beginQuantity": 0,
                "diffCost": 0.0,
                "removalReturnCost": 0.0,
                "inventoryReceiptsQuantity": 0,
                "unionAlias": "Zingtto:NA_FBA",
                "endCost": 0.0,
                "smAccountId": null,
                "adjustmentsDamagedQuantity": 0,
                "inventoryReceiptsCost": 0.0,
                "customerOrderQuantityGap": null,
                "adjustmentsLostPurchaseCost": 0.0,
                "customerReturnQuantityGap": 0,
                "endAccountQuantity": 0,
                "marketName": "Zingtto:US",
                "pmAccountId": null,
                "adjustmentsDamagedArriveCost": 0.0,
                "diffPurchaseCost": 0.0,
                "erpTransitQuantity": 0,
                "endAccountPurchaseCost": 0.0,
                "transitBetweenWarehouseArriveCost": 0.0,
                "endBookCost": 0.0,
                "fnsku": "X000W1NHE9",
                "receiptsArriveCost": 0.0,
                "productStatusValue": "可售",
                "erpShippedCost": 0.0,
                "beginBookPurchaseCost": 0.0,
                "beginQuantityGap": 0,
                "receiptsCost": 0.0,
                "bookDiffArriveCost": 0.0,
                "warehouseTransferInOutQuantity": 0,
                "bookDiffQuantity": null,
                "adjustmentsOtherCost": 0.0,
                "adjustmentsOtherArriveCost": 0.0,
                "customerShipmentsPurchaseCost": 0.0,
                "adjustmentsOtherPurchaseCost": 0.0,
                "dealDiffQuantity": null,
                "adjustmentsLostArriveCost": 0.0,
                "beginBookArriveCost": 0.0,
                "msku": "EyelinerStampNew0630",
                "dealDiffCost": null,
                "fbaShippedArriveCost": 0.0,
                "adjustmentsFoundCost": 0.0,
                "customerShipmentsQuantityGap": 0,
                "month": "2023-02",
                "transitBetweenWarehouseQuantity": 0,
                "customerOrderArriveCost": 0.0,
                "endBookQuantity": 0,
                "inventoryReceiptsPurchaseCost": 0.0,
                "customerReturnCost": 0.0,
                "adjustmentsFoundQuantity": 0,
                "receiptsQuantity": 0,
                "customerReturnGapCost": 0.0,
                "customerOrderQuantity": 0,
                "erpShippedPurchaseCost": 0.0,
                "marketId": 1,
                "fbaTransitQuantity": 0,
                "tbShippedCost": 0.0,
                "tbShippedPurchaseCost": 0.0,
                "customerShipmentsGapArriveCost": 0.0,
                "productType": null,
                "customerReturnsCost": 0.0,
                "customerShipmentsGapCost": 0.0,
                "adjustmentsLostCost": 0.0,
                "customerReturnGapArriveCost": 0.0,
                "pmAccountName": "",
                "endAccountArriveCost": 0.0,
                "quantityId": 1236444,
                "productStatus": "normal",
                "adjustmentsDisposalCost": 0.0,
                "customerOrderPurchaseCost": 0.0,
                "warehouseTransferInOutArriveCost": 0.0,
                "transitBetweenWarehouseCost": 0.0,
                "customerReturnArriveCost": 0.0,
                "beginQuantityTransport": 0,
                "customerShipmentsQuantity": 0,
                "removalQuantity": 0,
                "customerReturnGapPurchaseCost": 0.0,
                "customerShipmentsCost": 0.0,
                "dealDiffArriveCost": null,
                "fasin": null,
                "receiptsPurchaseCost": 0.0,
                "customerReturnsPurchaseCost": 0.0,
                "beginArriveCost": 0.0,
                "asin": "B017GZNFW6",
                "adjustmentsFoundPurchaseCost": 0.0,
                "dateRangeReportOrderQuantity": 0
            }
        ]
    },
    "messages": []
}
```

---

## 143. FBA进销存-数量

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | FBA进销存-数量 |
| 请求地址 | `/finance/asset/fbaPsiQuantity/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| month | string | 是 | 月份 [yyyy-MM] |
| warehouseIds | array<long> | 否 | 仓库ID |
| mskuList | array<string> | 否 | MSKU |
| skuList | array<string> | 否 | SKU |
| warehouseType | string | 否 | 仓库类型：默认EXACT |
| productStatus | string | 否 | 产品状态 |
| type | string | 否 | 查询类型：默认MSKU |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "month": "2023-02"
}
```

### 响应示例

```json
{
    "traceId": "open_a4ac6dbbe60c4345b680d87b15b9e6b7",
    "code": 200,
    "data": {
        "total": 16661,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "fnsku": "X000W1NHE9",
                "productStatusValue": "可售",
                "beginQuantityGap": 0,
                "sellerId": "",
                "adjustmentsDisposalQuantity": 0,
                "warehouseTransferInOutQuantity": 0,
                "bookDiffQuantity": null,
                "smAccountName": "",
                "id": 1236444,
                "sku": null,
                "shipmentsDateRangeQuantityGap": 0,
                "dealDiffQuantity": null,
                "msku": "EyelinerStampNew0630",
                "customerReturnQuantity": 0,
                "turnoverRatioAvg": null,
                "adjustmentsLostQuantity": 0,
                "month": "2023-02",
                "customerShipmentsQuantityGap": 0,
                "warehouseId": 2,
                "exactFlag": false,
                "transitBetweenWarehouseQuantity": 0,
                "endBookQuantity": 0,
                "tbShippedQuantity": 0,
                "adjustmentsOtherQuantity": 0,
                "customerReturnsQuantity": 0,
                "turnoverRatio": null,
                "endQuantity": 0,
                "adjustmentsFoundQuantity": 0,
                "receiptsQuantity": 0,
                "unknownEventsQuantity": 0,
                "customerOrderQuantity": 0,
                "warehouseName": "Zingtto:US_FBA",
                "marketId": 1,
                "fbaTransitQuantity": 0,
                "beginQuantity": 0,
                "productType": null,
                "itsRatio": null,
                "inventoryReceiptsQuantity": 0,
                "unionAlias": "Zingtto:NA_FBA",
                "smAccountId": null,
                "adjustmentsDamagedQuantity": 0,
                "pmAccountName": "",
                "productStatus": "normal",
                "turnoverDays": null,
                "customerOrderQuantityGap": null,
                "updateTime": "2023-08-23 09:58:25",
                "beginQuantityTransport": 0,
                "customerShipmentsQuantity": 0,
                "removalQuantity": 0,
                "endAccountQuantity": 0,
                "marketName": "Zingtto:US",
                "pmAccountId": null,
                "createTime": "2023-08-23 09:58:25",
                "fasin": null,
                "erpTransitQuantity": 0,
                "asin": "B017GZNFW6",
                "dateRangeReportOrderQuantity": 0
            }
        ]
    },
    "messages": []
}
```

---

## 144. 查询长期仓储费

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询长期仓储费 |
| 请求地址 | `/finance/asset/storageLongFee/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| purchaseStartDate | date | 否 | 开始时间 [yyyy-MM-dd] |
| purchaseEndDate | date | 否 | 结束时间 [yyyy-MM-dd] |
| marketIds | array<long> | 否 | 站点集合 |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
	"page": 1,
	"pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_b02a03ae911145a3bae683e7fa94d6a9",
    "code": 200,
    "data": {
        "total": 488,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "country": "JP",
                "fnsku": "FNGJX0000370",
                "quantity6More": "0",
                "year": "2020",
                "volumeUnit": "cubic_meters",
                "storageFee12More": 164.0,
                "enrolledSmallAndLight": "N",
                "title": "",
                "serverId": 1,
                "productName": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time",
                "storageFee6More": 0.0,
                "marketId": 12,
                "currency": "JPY",
                "sku": "",
                "brand": "",
                "snapshotDate": "2020-03-14T23:00:00+08:00",
                "beijingTime": false,
                "msku": "TEST_MSKU_GJ ERP-QWE1142",
                "smallImageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                "asinUrl": "https://www.amazon.co.jp/gp/product/BGJ0000286",
                "condition": "New",
                "perUnitVolume": "8.0E-4",
                "quantity12More": "11",
                "normalImageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                "month": "3",
                "asin": "BGJ0000286",
                "category": "NO"
            }
        ]
    },
    "messages": ["request.success"]
}
```

---

## 145. 查询月度仓储费

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询月度仓储费 |
| 请求地址 | `/finance/asset/storageFee/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| year | string | 否 | 年份 [yyyy] |
| month | string | 否 | 月份 [M] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_8b2378179b674ec0a934a5e8bff52614",
    "code": 200,
    "data": {
        "total": 203728,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "itemVolume": "0",
                "storageFee": 0.2252,
                "fnsku": "FNGJX0000015",
                "year": "2018",
                "marketIds": [],
                "title": "",
                "serverId": 1,
                "productName": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time",
                "marketId": 1,
                "storageRate": "0.69",
                "estimatedTotalItemVolume": "0.3255",
                "monthOfCharge": "2018-05",
                "countryCode": "US",
                "weightUnits": "",
                "currency": "USD",
                "id": 1,
                "sku": "",
                "measurementUnits": "",
                "brand": "null",
                "smallImageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                "medianSide": "0",
                "averageQuantityOnHand": "7.03",
                "weight": "0",
                "productSizeTier": "",
                "asinUrl": "https://www.amazon.com/gp/product/BGJ0000003",
                "shortestSide": "0",
                "fulfillmentCenter": "LEX1",
                "averageQuantityPendingRemoval": "1.55",
                "longestSide": "0",
                "normalImageUrl": "https://gateway.apist.gerpgo.com/common/file?id=1529&origin=demo",
                "month": "5",
                "estimatedMonthlyStorageFee": "0.2252",
                "volumeUnits": "",
                "asin": "BGJ0000003",
                "category": "NO"
            }
        ]
    },
    "messages": ["request.success"]
}
```

---

## 146. 查询赔偿列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询赔偿列表 |
| 请求地址 | `/operation/asset/compensateInfo/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| purchaseStartDate | date | 否 | 开始时间 [yyyy-MM-dd] |
| purchaseEndDate | date | 否 | 结束时间 [yyyy-MM-dd] |
| amazonOrderId | string | 否 | 订单号 |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketIds | array<long> | 否 | 站点 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | number | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | null | 是 | 接口返回traceId |

### 请求示例

```json
{
	"page": 1,
	"pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_4a5ffd038ecf4c3ba9a17b0790a3d743",
    "code": 200,
    "data": {
        "total": 19540,
        "pagesize": 1,  
        "page": 1,       
        "rows": [
            {
                "reason": "CustomerReturn",
                "originalReimbursementId": null,
                "approvalDate": "2020-04-27T06:53:24-07:00",
                "fnsku": "FNGJX0001774",
                "amountPerUnit": 49.01,
                "quantityReimbursedTotal": 1,
                "amazonOrderId": "113-7096054-0194615",
                "quantityReimbursedInventory": 0,
                "productName": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time",
                "marketId": 8,
                "originalReimbursementType": null,
                "condition": "NewItem",
                "caseId": "",
                "asin": "BGJ0000435",
                "amountTotal": 49.01,
                "id": 36243,
                "sku": "TEST_MSKU_GJ ERP-QWE1072",
                "reimbursementId": "5032515621",
                "currencyUnit": "USD",
                "quantityReimbursedCash": 1,
                "createDate": "2020-11-03T22:07:09.000+00:00"
            }
        ]
       
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 147. 查询退款单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询退款单列表 |
| 请求地址 | `/finance/asset/paymentRefund/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| endDate | date | 否 | 退款结束日期 [yyyy-MM-dd] |
| businessType | string | 否 | 单据类型 [付款退款单: payment_refund; 退货退款单: return_refund] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| realRefdundBeginDate | date | 否 | 实际退款开始日期 [yyyy-MM-dd] |
| realRefdundEndDate | date | 否 | 实际退款结束日期 [yyyy-MM-dd] |
| refundCode | array<string> | 否 | 单据编号 |
| refundStatus | array<string> | 否 | 单据状态 [待退款: pending; 已退款: refunded; 已作废: cancelled] |
| sourceItemCode | array | 否 | 源单明细编号 |
| supplierCodeList | array | 否 | 应收对象标识 [供应商: Supplier; 物流商: Logistics; 推广资源: Service; 个人: Personal] |
| updateTimeStart | datetime | 否 | 更新时间-开始时间 [yyyy-MM-dd HH:mm:ss] |
| updateTimeEnd | datetime | 否 | 更新时间-结束时间 [yyyy-MM-dd HH:mm:ss] |
| beginDate | date | 否 | 开始退款日期 [yyyy-MM-dd] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "total": 13,
        "size": 0,
        "footer": [],
        "pagesize": 0,
        "from": 0,
        "page": 0,
        "rows": [
            {
                "attachmentDtos": [],
                "realRefundDate": "2022-08-02 01:50:27",
                "urgencyLevel": {
                    "name": "正常",
                    "value": "general"
                },
                "payBank": "",
                "receiveUserId": "",
                "exchangeRealAmountSum": {
                    "kilobitsAmount": "￥20.0000",
                    "currencyAmount": 20.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥20.0000"
                },
                "refundRemainAmountSum": {
                    "kilobitsAmount": "￥100.0000",
                    "currencyAmount": 100.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥100.0000"
                },
                "payNews": "",
                "id": 7,
                "transCode": "",
                "urgencyReason": "",
                "sourceRemainAmountSum": {
                    "kilobitsAmount": "￥100.0000",
                    "currencyAmount": 100.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥100.0000"
                },
                "exchangeSourceRemainAmountSum": {
                    "kilobitsAmount": "￥100.0000",
                    "currencyAmount": 100.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥100.0000"
                },
                "purchaseDeptName": "",
                "sourceItemCode": [
                    "FK0F2208020003"
                ],
                "actualRefundAmountSum": {
                    "kilobitsAmount": "￥20.0000",
                    "currencyAmount": 20.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥20.0000"
                },
                "refundMode": "银行转账",
                "supplierType": {
                    "name": "供应商",
                    "value": "supply"
                },
                "payCode": "",
                "exchangeRefundRemainAmountSum": {
                    "kilobitsAmount": "￥100.0000",
                    "currencyAmount": 100.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥100.0000"
                },
                "refundDate": "2022-07-31",
                "payDrawee": "",
                "exchangeServiceChargeSum": {
                    "kilobitsAmount": "￥0.0000",
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "purchaseSubjectName": "-",
                "exchangeActualRefundAmountSum": {
                    "kilobitsAmount": "￥20.0000",
                    "currencyAmount": 20.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥20.0000"
                },
                "realAmountSum": {
                    "kilobitsAmount": "￥20.0000",
                    "currencyAmount": 20.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥20.0000"
                },
                "billSource": "system",
                "serviceChargeSum": {
                    "kilobitsAmount": "￥0.0000",
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "refundStatus": {
                    "name": "已退款",
                    "value": "refunded"
                },
                "remark": "",
                "supplierCode": "GJ_S2",
                "receiveNews": "-",
                "refundType": {
                    "name": "付款",
                    "value": "PaymentRequest"
                },
                "updateBy": 5931,
                "purchaseUserName": "",
                "purchaseUserId": "0",
                "itemOutDtos": [
                    {
                        "originCodeType": {
                            "name": "采购订单",
                            "value": "PURCHASE_ORDER"
                        },
                        "codeType": {
                            "name": "采购订单",
                            "value": "PURCHASE_ORDER"
                        },
                        "exchangeRefundRemainAmount": {
                            "kilobitsAmount": "￥100.0000",
                            "currencyAmount": 100.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥100.0000"
                        },
                        "exchangeRealAmount": {
                            "kilobitsAmount": "￥20.0000",
                            "currencyAmount": 20.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥20.0000"
                        },
                        "exchangeSourceRemainAmount": {
                            "kilobitsAmount": "￥100.0000",
                            "currencyAmount": 100.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥100.0000"
                        },
                        "sourceCurrency": "CNY",
                        "remark": "",
                        "exchangePayAmount": {
                            "kilobitsAmount": "￥20.0000",
                            "currencyAmount": 20.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥20.0000"
                        },
                        "exchangeServiceCharge": {
                            "kilobitsAmount": "￥0.0000",
                            "currencyAmount": 0.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥0.0000"
                        },
                        "payRealAmount": {
                            "kilobitsAmount": "￥20.0000",
                            "currencyAmount": 20.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥20.0000"
                        },
                        "customCode": "PO2208021592",
                        "marketId": "",
                        "sourceDate": "2022-07-30",
                        "realAmount": {
                            "kilobitsAmount": "￥20.0000",
                            "currencyAmount": 20.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥20.0000"
                        },
                        "refundItemId": "TKITEM0F2208020002",
                        "serviceCharge": {
                            "kilobitsAmount": "￥0.0000",
                            "currencyAmount": 0.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥0.0000"
                        },
                        "payAmount": {
                            "kilobitsAmount": "￥100.0000",
                            "currencyAmount": 100.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥100.0000"
                        },
                        "id": 7,
                        "sourceRemainAmount": {
                            "kilobitsAmount": "￥100.0000",
                            "currencyAmount": 100.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥100.0000"
                        },
                        "payRemainAmount": {
                            "kilobitsAmount": "￥100.0000",
                            "currencyAmount": 100.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥100.0000"
                        },
                        "fcode": "PO2208021592",
                        "refundAmount": {
                            "kilobitsAmount": "￥100.0000",
                            "currencyAmount": 100.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥100.0000"
                        },
                        "exchangeActualRefundAmount": {
                            "kilobitsAmount": "￥20.0000",
                            "currencyAmount": 20.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥20.0000"
                        },
                        "sourceRate": 1.0,
                        "refundRemainAmount": {
                            "kilobitsAmount": "￥100.0000",
                            "currencyAmount": 100.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥100.0000"
                        },
                        "payRate": 1.0,
                        "billItemCode": "FKMX0F2208020003",
                        "relevantBillCode": "CG0F2208020003",
                        "originType": {
                            "billCodeEnum": "CG",
                            "name": "采购费用",
                            "value": "purchase_fee"
                        },
                        "sourceRealAmount": {
                            "kilobitsAmount": "￥20.0000",
                            "currencyAmount": 20.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥20.0000"
                        },
                        "purchaseOrder": "PO2208021592",
                        "realPayDate": "2022-07-31 23:46:43",
                        "sourceItemCode": "FK0F2208020003",
                        "payCurrency": {
                            "symbol": "￥",
                            "name": "人民币",
                            "value": "CNY"
                        },
                        "actualRefundAmount": {
                            "kilobitsAmount": "￥20.0000",
                            "currencyAmount": 20.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY",
                            "amountWithSymbol": "￥20.0000"
                        },
                        "refundCode": "TK0F2208020002"
                    }
                ],
                "billType": {
                    "name": "付款退款单",
                    "value": "payment_refund"
                },
                "updateTime": "2022-08-02 01:50:41",
                "purchaseDept": "0",
                "payAccount": "",
                "relevantBillCode": [
                    "CG0F2208020003"
                ],
                "purchaseSubject": "",
                "supplierCodeName": "金华",
                "createBy": 5931,
                "expectedRefundDate": "2022-07-31",
                "createTime": "2022-08-02 01:49:57",
                "refundRate": "1.0000",
                "refundCode": "TK0F2208020002"
            }
        ]
    }
}
```

---

## 148. 查询销售回款分析

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询销售回款分析 |
| 请求地址 | `/finance/asset/financialEventGroup/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| processingStatus | string | 否 | 付款状态 [未结算: Open; 已经结算: Closed] |
| fundTransferStatus | string | 否 | 转账状态 [Failed 失败； Processing --处理中 ；Succeeded --成功；Unknown 未知 ；NoFundsDisbursed 未付款] |
| dateType | string | 否 | 查询时间类型 [付款时间: fundTransferDate; 结算周期: financialEventGroupEnd; 更新时间: updateDate] |
| purchaseStartDate | date | 否 | 开始时间 [yyyy-MM-dd] |
| purchaseEndDate | date | 否 | 截止时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| marketIds | array<long> | 否 | 国家id |
| currency | string | 否 | 币种 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 返回提示信息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize":1
}
```

### 响应示例

```json
{
    "traceId": "open_d0fdaedbcb5e471889ef97098446f619",
    "code": 200,
    "data": {
        "total": 1232,
        "footer": [],
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "financialEventGroupEnd": "2023-05-07T06:06:57Z",
                "financialEventGroupDateInterval": "2023-04-21T06:06:57Z~2023-05-07T06:06:57Z",
                "transferStandardDate": "2019-03-06 19:18:22",
                "country": "US",
                "convertedAmount": 289.41,
                "financialEventGroupId": "ysYeL4YCDKzUnfx8uafawN1POcE830gi-VfWHRFDoaQ",
                "fundTransferStatus": "Succeeded",
                "memo": "",
                "accountLevelReserveCode": "",
                "settlementId": "11549125631",
                "accountLevelReserveObj": {
                    "amount": null,
                    "currencySymbol": "",
                    "currency": ""
                },
                "amountCashed": 20.0,
                "marketId": 4,
                "amountCashedCode": "CNY",
                "settledAmountObj": null,
                "alias": "积加测试店铺2",
                "id": 1,
                "traceId": "GJ ERP Trace id 1",
                "settledStandardDateInterval": "2023-04-21 06:06:57~2023-05-07 06:06:57",
                "originalAmountObj": {
                    "amount": 289.41,
                    "currencySymbol": "$",
                    "currency": "USD"
                },
                "convertedAmountObj": {
                    "amount": 289.41,
                    "currencySymbol": "$",
                    "currency": "USD"
                },
                "updateTime": "2023-05-05T22:06:57.000+00:00",
                "countryCanEdit": 0,
                "accountLevelReserve": null,
                "processingStatus": "Closed",
                "amountCashedObj": {
                    "amount": 20.0,
                    "currencySymbol": "￥",
                    "currency": "CNY"
                },
                "originalAmount": 289.41,
                "financialEventGroupStart": "2023-04-21T06:06:57Z",
                "originalCode": "USD",
                "convertedCode": "USD",
                "accountTail": "304",
                "fundTransferDate": "2019-03-06T19:18:22.756Z"
            }
        ]
    },
    "messages": []
}
```

---

## 149. 查询月结算

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询月结算 |
| 请求地址 | `/finance/asset/monthlyStatementAmount/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| showCurrencyType | string | 否 | 展示币种 [YUAN,CNY,USD] |
| typeCode | int | 是 | 类型编码，0：销量，1：收入-订单，2：收入-赔偿，3：费用-订单，4：费用-服务费，5：费用-广告，6：费用-押金，7：费用-成本，8：费用-站外，9：税-销售税，10：其他 |
| viewType | string | 否 | 数据查询类型 [按天: day; 按周: week; 按月: month; 按年: year] |
| beginDate | date | 是 | 开始日期 [yyyy-MM-dd] |
| endDate | date | 是 | 结束日期 [yyyy-MM-dd] |
| marketIds | array<long> | 否 | 站点 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | array<object> | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "typeCode": 1,
    "beginDate": "2023-10-01",
    "endDate": "2023-10-07"
}
```

### 响应示例

```json
{
    "code": 200,
    "data": [
        {
            "totalAmount": {
                "amount": "",
                "quantity": "",
                "currencySymbol": ""
            },
            "marketName": "",
            "amountTypeName": "亚马逊配送订单销售总额",
            "amountMap": {
                "2024-01-01": {
                    "quantity": "1",
                    "currencySymbol": "",
                    "amount": "",
                    "baseCurrencySymbol": "",
                    "baseCurrencyAmount": ""
                },
                "2024-01-02": {
                    "quantity": "1",
                    "currencySymbol": "",
                    "amount": "",
                    "baseCurrencySymbol": "",
                    "baseCurrencyAmount": ""
                }
            },
            "amountTypeCode": 5
        }
    ],
    "messages": [
        "request.success"
    ]
}
```

---

## 150. 查询日期范围报告

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询日期范围报告 |
| 请求地址 | `/finance/asset/dateRangeReports/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| purchaseStartDate | date | 否 | 开始时间 [yyyy-MM-dd] |
| purchaseEndDate | date | 否 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [建议100条/页] |
| orderType | int | 否 | 报表类型 [标准订单: 0; 发票订单: 1] |
| marketIds | array<int> | 否 | 店铺ID集合，如果数据较多，建议按店铺单独分开同步效率更高 |
| feeTypes | array<string> | 否 | 费用类型 [mergerFee: 并仓费; removeFee: 移除处置费; returnFee: 退货处理费; dealFee: Deal; couponFee: Coupon; compensation: 赔偿费用; order: 订单费用; refund: 退款费用; other: 未归类费用; transfer: 转账; storage: 月度仓储费; longStorage: 长期仓储费; adCost: 广告花费; chargeBackRefund: 退款费; amazonLogistics: 亚马逊物流承运人费; atozComplaint: AtoZ投诉费; subscribe: 订阅费; excessStorage: 超量仓储费; earlyReviewer: 早期评论人计划费; returnCardTransfer: 转出失败; cardTransfer: 信用卡转入; disbursementCorrect: 付款更正; addTax: 增值税收; otherStorage: 其他仓储费; managerFee: 账号经理费; liquidation: 清算费用; adjustmentFee: 费用调整; intFreight: 国际运输费; intFreightAdjustment: 国际运输费调整; intFreightTax: 国际货运税费; liquidationAdjust: 清算调整; trialOrder: 试用订单; trialShipment: 试用运费; orderRetroCharge: 订单退税费; refundRetroCharge: 订单退税调整费; unplannedServiceFee: 计划外服务费; shippingServiceFee: 航运服务费; adjustment: 调整费用; preProcessingFee:预处理费, gradeAndResellFee:二次转售费, vineEvaluationFee:VINE测评费, deliveryServices:送货服务, compensationAdjust:赔偿调整, withholdingIncomeTax:预扣所得税, fbaTransportFee: FBA运输费, shippingServices: 便捷送货费, fulfilmentRefund:履约费退款] |
| orderId | string | 否 | 订单id |
| queryDateType | int | 否 | 时间类型 [市场时间: 0; 零时区时间: 1] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 提示消息 |
| traceId | string | 是 | 返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_772429a63414435c996ab6692d1a2f03",
    "code": 200,
    "data": {
        "total": 628967,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "orderType": 0,
                "orderId": "",
                "regulatoryFeeTax": 0.0,
                "otherTransactionFees": 0.0,
                "type": "Debt",
                "standardDate": "2020-04-06 15:54:25",
                "orderState": "",
                "pointsGranted": 0.0,
                "testOrderName": "",
                "marketDate": "2023-05-07 06:00:32",
                "productSales": 0.0,
                "testOrder": false,
                "saleOrderType": "",
                "id": 1,
                "promotionalRebates": 0.0,
                "sku": "",
                "originSku": "",
                "fbaFees": 0.0,
                "sellingFees": 0.0,
                "zeroDate": "2020-04-06 22:54:25",
                "taxCollectionModel": "",
                "regulatoryFee": 0.0,
                "marketplace": "",
                "tcsigst": 0.0,
                "feeType": "",
                "promotionalRebatesTax": 0.0,
                "productSalesTax": 0.0,
                "other": 173.15,
                "updateDate": "2020-04-22 15:16:18",
                "shippingCreditsTax": 0.0,
                "description": "amzn1.cam.v1.sgid.12733098381",
                "settlementId": "12794775751",
                "marketId": 2,
                "giftWrapCreditsTax": 0.0,
                "total": 173.15,
                "tcssgst": 0.0,
                "currency": "",
                "shippingCredits": 0.0,
                "marketplaceWithheldTax": 0.0,
                "createDate": "2020-04-06 7:54:25 AM PDT",
                "product": "",
                "quantity": 0,
                "currencySymbol": "",
                "tcscgst": 0.0,
                "marketName": "一号店:CA",
                "orderPostal": "",
                "orderCity": "",
                "giftWrapCredits": 0.0,
                "fulfillment": "",
                "countryCode": "CA",
                "countryName": "加拿大"
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 151. 查询付款单列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询付款单列表 |
| 请求地址 | `/finance/asset/paymentbill/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| currency | string | 否 | 查询币种 |
| payStatusList | array<string> | 否 | 支付状态 [待支付: pending_payment; 已支付: already_payment; 已作废: cancelled] |
| refundStatusList | array<string> | 否 | 退款状态 [无需退款: no_need_refund; 未退款: un_refund; 部分退款: partial_refund; 全部退款: full_refund] |
| billCodeList | array<string> | 否 | 付款单据编号 |
| applyCodeList | array<string> | 否 | 申请单据编号 |
| payableTargetCodeList | array<string> | 否 | 应付对象code |
| purchaseUserIds | array<string> | 否 | 业务员ids |
| purchaseDeptIds | array<string> | 否 | 部门ids |
| realPayUserIds | array<string> | 否 | 支付人id |
| payCurrency | string | 否 | 支付币种 |
| applyCurrency | string | 否 | 申请币种 |
| fcodeList | array<string> | 否 | 关联单据集合 |
| expectedPaymentDateStart | date | 否 | 期望付款时间-开始 [yyyy-MM-dd] |
| expectedPaymentDateEnd | date | 否 | 期望付款时间-结束 [yyyy-MM-dd] |
| realPayTimeStart | date | 否 | 支付时间-开始 [yyyy-MM-dd] |
| realPayTimeEnd | date | 否 | 支付时间-结束 [yyyy-MM-dd] |
| createTimeStart | date | 否 | 单据时间-开始 [yyyy-MM-dd] |
| createTimeEnd | date | 否 | 单据时间-结束 [yyyy-MM-dd] |
| updateTimeStart | date | 否 | 更新时间-开始时间 [yyyy-MM-dd] |
| updateTimeEnd | date | 否 | 更新时间-结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_09a0cfdd569e43ef8d3c06a68971877c",
    "code": 200,
    "data": {
        "total": 536,
        "pagesize": 0,
        "page": 0,
        "rows": [
            {
                "reason": "",
                "inRefundAmount": {
                    "kilobitsAmount": "￥0.0000",
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "urgencyLevel": {
                    "name": "正常",
                    "value": "general"
                },
                "payBank": "",
                "serviceCharge": {
                    "kilobitsAmount": "￥0.0000",
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "payAmount": {
                    "kilobitsAmount": "￥250.0000",
                    "currencyAmount": 250.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "payNews": "工商银行-1234567890",
                "remainAmount": {
                    "kilobitsAmount": "￥0.0000",
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "billItemResps": [
                    {
                        "applyType": {
                            "name": "采购费用",
                            "value": "purchase_fee"
                        },
                        "codeType": {
                            "name": "入库单",
                            "value": "GRN"
                        },
                        "expectedPaymentDate": "2023-01-29",
                        "attachmentDtos": [],
                        "cashDiscountYuan": 0.0,
                        "inRefundAmount": 0.0,
                        "serviceCharge": {
                            "kilobitsAmount": "￥0.0000",
                            "currencyAmount": 0.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "receiveName": "",
                        "payAmount": {
                            "kilobitsAmount": "￥250.0000",
                            "currencyAmount": 250.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "remainAmount": {
                            "kilobitsAmount": "￥0.0000",
                            "currencyAmount": 0.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "trackings": "",
                        "originCode": "CG0F2301310128",
                        "id": 2318,
                        "receiveType": {
                            "name": "付款",
                            "value": "PaymentRequest"
                        },
                        "fcode": "GIB06423013100000046",
                        "shipmentCodes": [],
                        "msku": "",
                        "payRate": 1.0,
                        "receiveBank": "",
                        "applyRate": 1.0,
                        "payAmountYuan": 250.0,
                        "applyAttachmentDtos": [],
                        "applyUserName": "上海嘉劭",
                        "applyRemark": "",
                        "payCurrency": "CNY",
                        "receiveAccount": "",
                        "applyCode": "FKSQ0F2301310049",
                        "applyPayAmount": {
                            "kilobitsAmount": "￥250.0000",
                            "currencyAmount": 250.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "refundedAmount": 0.0,
                        "paymentBillRemark": "",
                        "remainPayAmount": {
                            "kilobitsAmount": "￥250.0000",
                            "currencyAmount": 250.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "originCurrency": "CNY",
                        "remark": "",
                        "receiveNews": "",
                        "title": "",
                        "categoryName": "",
                        "applyUserId": 10611,
                        "customCode": "PO2301311893",
                        "realAmount": {
                            "kilobitsAmount": "￥250.0000",
                            "currencyAmount": 250.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "updateBy": "10611",
                        "realAmountYuan": {
                            "kilobitsAmount": "￥250.0000",
                            "currencyAmount": 250.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "currency": "",
                        "cashDiscount": {
                            "kilobitsAmount": "￥0.0000",
                            "currencyAmount": 0.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "serviceChargeYuan": 0.0,
                        "payMode": "银行转账",
                        "receiveCode": "",
                        "billCode": "FK0F2301310003",
                        "updateTime": "2023-02-12 21:10:37",
                        "billItemCode": "FKMX0F2301310003",
                        "applyItemCode": "SQMX0F2301310003",
                        "asinUrl": "",
                        "planCode": "PP0F2301310001",
                        "remainPayAmountYuan": {
                            "kilobitsAmount": "￥250.0000",
                            "currencyAmount": 250.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "remainAmountYuan": {
                            "kilobitsAmount": "￥0.0000",
                            "currencyAmount": 0.0,
                            "currencySymbol": "￥",
                            "currencyCode": "CNY"
                        },
                        "createBy": "10611",
                        "marketName": "",
                        "createTime": "2023-01-31",
                        "purchaseOrder": "PO2301311893",
                        "asin": "",
                        "warehouseNames": [
                            "CN_007"
                        ],
                        "payStatus": {
                            "name": "待支付",
                            "value": "pending_payment"
                        }
                    }
                ],
                "id": 577,
                "transCode": "",
                "realPayUser": 0,
                "urgencyReason": "",
                "realPayUserName": "",
                "payRate": 1.0,
                "payAmountYuan": {
                    "kilobitsAmount": "￥0.0000",
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥0.0000"
                },
                "purchaseDeptName": "",
                "payCurrency": "CNY",
                "refundedAmount": {
                    "kilobitsAmount": "￥0.0000",
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "remainPayAmount": {
                    "kilobitsAmount": "￥250.0000",
                    "currencyAmount": 250.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "originCurrency": "CNY",
                "refundStatus": {
                    "name": "未退款",
                    "value": "un_refund"
                },
                "payableTarget": {
                    "settlementType": {
                        "name": "月结",
                        "type": 2
                    },
                    "code": "JG001",
                    "receiptInfo": "[{\"name\":\"\",\"bankName\":\"\",\"bankCode\":\"\"}]",
                    "name": "龙珠加工",
                    "typeName": "供应商",
                    "type": {
                        "name": "供应商",
                        "value": "supply"
                    }
                },
                "remark": "",
                "realAmount": {
                    "kilobitsAmount": "￥250.0000",
                    "currencyAmount": 250.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "payAccountCode": "1234567890",
                "updateBy": "10611",
                "purchaseUserName": "上海嘉劭",
                "cashDiscount": {
                    "kilobitsAmount": "￥0.0000",
                    "currencyAmount": 0.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY"
                },
                "payName": "工商银行",
                "purchaseUserId": 10611,
                "payMode": "银行转账",
                "billType": {
                    "name": "付款单",
                    "value": "payment"
                },
                "purchase": {
                    "purchaseSubject": 0,
                    "purchaseSubjectName": "",
                    "purchaseDeptName": "",
                    "purchaseUserName": ""
                },
                "billCode": "FK0F2301310003",
                "updateTime": "2023-02-12 21:10:37",
                "payAccount": "",
                "remainPayAmountYuan": {
                    "kilobitsAmount": "￥250.0000",
                    "currencyAmount": 250.0,
                    "currencySymbol": "￥",
                    "currencyCode": "CNY",
                    "amountWithSymbol": "￥250.0000"
                },
                "purchaseSubject": 0,
                "createBy": "10611",
                "createTime": "2023-01-31",
                "payStatus": {
                    "name": "待支付",
                    "value": "pending_payment"
                }
            }
        ]
    },
    "messages": []
}
```

---

## 152. 广告发票历史记录

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 广告发票历史记录 |
| 请求地址 | `/finance/asset/adsInvoice/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| invoiceId | string | 否 | 发票id |
| dateType | int | 否 | 日期类型 [发票开具日期: 1; 开始日期: 2; 到期日期: 3] |
| startDate | date | 否 | 开始时间 [yyyy-MM-dd] |
| endDate | date | 否 | 结束时间 [yyyy-MM-dd] |
| status | string | 否 | 状态 [已发行: ISSUED; 部分付款: PAID_IN_PART; 全额付款: PAID_IN_FULL; 注销: WRITTEN_OFF; 处理中: PROCESSING] |
| paymentMethod | string | 否 | 付款方式 [信用卡: CREDIT_CARD; 借记卡: DIRECT_DEBIT; 电子资金转账: ELECTRONIC_FUNDS_TRANSFER; 卖家账户: DEDUCT_FROM_PAYMENT; 统一计费: UNIFIED_BILLING] |
| marketIds | array<int> | 否 | 站点集合 |
| queryCurrency | string | 是 | 查询币种 |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | 接口返回数据 |
| extObj | object | 是 | 接口返回扩展对象 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |

### 请求示例

```json
{
    "page": 1,
    "pagesize":1,
    "queryCurrency":"USD"
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "total": 39,
        "size": 0
    },
    "extObj": {
        "syncTime": null,
        "toDate": null,
        "totalAmountDue": 19487.27,
        "currencySymbol": "$",
        "invoiceDate": null,
        "version": null,
        "marketId": null,
        "amountDue": null,
        "fromDate": null,
        "marketName": "",
        "paymentMethod": "",
        "currency": "USD",
        "invoiceId": "",
        "id": null,
        "status": ""
    }
}
```

---

## 153. 查询其他费用分摊列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询其他费用分摊列表 |
| 请求地址 | `/finance/asset/allocationDashboard/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 3次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| reversalFlag | string | 否 | 红蓝单 [0-蓝，1-红] |
| allocationType | string | 否 | 分摊类型 [expense-费用分摊，cost-成本分摊] |
| allocationStatusList | array<string> | 否 | 分摊状态 [un_allocate-未分摊，draft-草稿，under_review-审核中，pending-待分摊，allocated-已分摊，voided-已作废，review_rejected-审核驳回] |
| createdByList | array | 否 | 创建人id集合 |
| allocationRangeList | array<string> | 否 | 分摊维度 [productCategory-品类，market-站点，msku-MSKU] |
| allocationRuleList | array | 否 | 分摊规则 [sales_amount-销售额，sales_volume-销售量，days-天数均摊，real_weight-按实重（Kg），stock_volume-按体积（CBM），quantity-按数量，customize_price-自定义分摊金额，unit_price-申报单价] |
| createTimeBegin | date | 否 | 创建开始时间 [yyyy-MM-dd] |
| createTimeEnd | date | 否 | 创建结束时间 [yyyy-MM-dd] |
| updateTimeBegin | date | 否 | 修改开始时间 [yyyy-MM-dd] |
| updateTimeEnd | date | 否 | 修改结束时间 [yyyy-MM-dd] |
| sourceBillCodeList | array<string> | 否 | 其他费用单明细单编号集合 |
| sourceAllocationCodeList | array<string> | 否 | 源分摊单据集合 |
| originCodeList | array<string> | 否 | 其他费用单编号集合 |
| billCodeList | array<string> | 否 | 分摊编号集合 |
| currency | string | 否 | 币种 [参考Q&A-通用参数-币种] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 响应码 |
| data | object | 是 | messages |
| array<string> | 是 | 否 | traceId |
| string | 是 | 否 |  |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "currency": "YUAN"
}
```

### 响应示例

```json
{
    "traceId": "open_ca5dc0fbd76944d3a4ddfd3985eb294d",
    "code": 200,
    "data": {
        "total": 26,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "sourceBillIds": [
                    "162"
                ],
                "allocationRange": "msku",
                "confirmTrace": "1",
                "reversalFlag": "0",
                "busiDate": "2022-07-30",
                "apportionmentPeriod": "2022-07",
                "allocationRule": "quantity",
                "updateUser": "****",
                "billCode": "FT0F2207300028",
                "remark": "",
                "updateTime": "2022-07-30 13:48:01",
                "allocationType": "cost",
                "allocationCostItems": [
                    {
                        "confirmTrace": "",
                        "totalPrice": 2.8125311861339E9,
                        "num": 3,
                        "periodOut": 0,
                        "warehouseName": "*******",
                        "productName": "123",
                        "marketId": "27",
                        "historyOut": 3,
                        "warehouseTime": "2021-02-06 23:27:58",
                        "purchasePlan": "",
                        "remainOut": 0,
                        "currency": "USD",
                        "id": 31,
                        "inboundType": "fba_return",
                        "sku": "123",
                        "inboundOrder": "TF123456",
                        "allocationCategoryItemInDtos": [
                            {
                                "unitPrice": 9.375103953779E8,
                                "totalAmount": {
                                    "kilobitsAmount": "$2,812,531,186.1339",
                                    "currencyAmount": 2.8125311861339E9,
                                    "currencySymbol": "$",
                                    "currencyCode": "USD",
                                    "amountWithSymbol": "$2812531186.1339"
                                },
                                "createBy": 910,
                                "allocationItemCode": "FTCBITEM0F2207300031",
                                "totalPrice": 2.8125311861339E9,
                                "createTime": "2022-07-30 13:48:01",
                                "updateBy": 910,
                                "unitAmount": {
                                    "kilobitsAmount": "$937,510,395.3779",
                                    "currencyAmount": 9.375103953779E8,
                                    "currencySymbol": "$",
                                    "currencyCode": "USD",
                                    "amountWithSymbol": "$937510395.3779"
                                },
                                "currency": "USD",
                                "updateTime": "2022-07-30 13:48:01",
                                "id": 31,
                                "categoryCode": "FYX0F2206250029"
                            }
                        ],
                        "unitPrice": 0.0,
                        "realNum": 3,
                        "allocationCode": "FT0F220730123132",
                        "msku": "M******P",
                        "boundOrder": "IB210***",
                        "historyNotSaleOutQuantity": 0,
                        "allocationRule": "quantity",
                        "periodNotSaleOutQuantity": 0,
                        "deliveryOrder": "LN2102031430",
                        "inboundTypeName": "FBA买家退货",
                        "totalAmount": {
                            "kilobitsAmount": "$2,812,531,186.1339",
                            "currencyAmount": 2.8125311861339E9,
                            "currencySymbol": "$",
                            "currencyCode": "USD",
                            "amountWithSymbol": "$2812531186.1339"
                        },
                        "physicalBatch": "1615885687",
                        "marketName": "******",
                        "allocationItemCode": "*******",
                        "warehouseId": "42",
                        "purchaseOrder": "******",
                        "unitAmount": {
                            "kilobitsAmount": "$0.0000",
                            "currencyAmount": 0.0,
                            "currencySymbol": "$",
                            "currencyCode": "USD",
                            "amountWithSymbol": "$0.0000"
                        },
                        "historySaleOutQuantity": 3,
                        "periodSaleOutQuantity": 0
                    }
                ],
                "originCodes": [
                    "*******"
                ],
                "sourceBillCodes": [],
                "totalAmount": {
                    "kilobitsAmount": "$534,380,925,365.4424",
                    "currencyAmount": 5.343809253654424E11,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$534380925365.4424"
                },
                "createTime": "2022-07-30 13:48:01",
                "costType": "warehouse_cost",
                "createUser": "yuyuan",
                "id": 27,
                "exchangeTotalAmount": {
                    "kilobitsAmount": "$534,380,925,365.4424",
                    "currencyAmount": 5.343809253654424E11,
                    "currencySymbol": "$",
                    "currencyCode": "USD",
                    "amountWithSymbol": "$534380925365.4424"
                },
                "allocationBillItems": [],
                "sourceAllocationCode": "",
                "allocationStatus": "under_review"
            }
        ]
    },
    "messages": []
}
```

---

## 154. 查询FBA进销存列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA进销存列表 |
| 请求地址 | `/purchase/inventory/purchaseSaleStorageFba/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 此接口提供历史数据 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 |  |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| type | string | 否 | 数量级别时,对应的统计级别 [MSKU: MSKU; 仓库: WAREHOUSE] |
| valueType | string | 否 | 统计级别 [数量: QUANTITY; 成本: COST] |
| warehouseIds | string | 否 | 仓库ids |
| month | string | 否 | 统计月份 [yyyy-MM] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "code": 200,
    "messages": [],
    "data": {
        "total": 16262,
        "size": 1,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "fnsku": "B07TJRNMT1",
                "id": 95076,
                "sku": "JP284RG",
                "msku": "JP284RG",
                "customerReturnQuantity": 13,
                "erpShippedQuantity": 0,
                "adjustmentsLostQuantity": 0,
                "month": "2022-10",
                "endBookQuantity": 13,
                "adjustmentsOtherQuantity": 0,
                "fbaShippedQuantity": 0,
                "endQuantity": 0,
                "adjustmentsFoundQuantity": 0,
                "customerOrderQuantity": 0,
                "diffQuantity": -13,
                "warehouseName": "积加测试店铺4:NA_FBA",
                "beginQuantity": 0,
                "dimension": "NA",
                "inventoryReceiptsQuantity": 0,
                "removalReturnQuantity": 0,
                "adjustmentsDisopsalQuantity": 0,
                "currencySymbol": "￥",
                "updateTime": "2022-11-06 16:00:03",
                "orderDiffQuantity": 0,
                "createTime": "2022-11-06 16:00:03",
                "dateRangeReportOrderQuantity": 0
            }
        ]
    }
}
```

---

## 155. FBA库存分类账-一览视图-按日维度列表查询

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | FBA库存分类账-一览视图-按日维度列表查询 |
| 请求地址 | `/fulfillment/inventory/storageLedger/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | number | 是 | 当前第几页 |
| pagesize | number | 是 | 每页条数 [最大100条/页] |
| model | object | 是 |  |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 返回数据 |
| messages | array | 是 | 接口返回提示消息 |
| traceId | null | 是 | 接口返回traceId |
| code | number | 是 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "model": {

    }
}
```

### 响应示例

```json
{
    "traceId": "open_4a6003d88f0c4ebaa037e5cc1268c562",
    "code": 200,
    "data": {
        "total": 100,
        "size": 1,
        "footer": null,
        "pagesize": 1,
        "from": 0,
        "page": 1,
        "rows": [
            {
                "country": "CA",
                "fnsku": "*****",
                "warehouseName": "****",
                "unknownEvents": 0,
                "otherEvents": 0,
                "vendorReturns": 0,
                "skuName": null,
                "found": 0,
                "reportDate": "2023-03-01",
                "lost": 0,
                "warehouseTransferInAndOut": 0,
                "disposed": 0,
                "sku": "*******",
                "msku": "*******",
                "startingWarehouseBalance": 246,
                "endingWarehouseBalance": 246,
                "updateTime": "2023-03-07 15:15:53",
                "inTransitBetweenWarehouses": 2,
                "customerShipments": 0,
                "receipts": 0,
                "disposition": "SELLABLE",
                "warehouseId": 36,
                "createTime": "2023-03-07 15:15:53",
                "sourceMsku": "*****",
                "damaged": 0,
                "asin": "B******W",
                "customerReturns": 0
            }
        ]
    },
    "messages": []
}
```

---

## 156. FBA库存分类账-详细视图列表查询

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | FBA库存分类账-详细视图列表查询 |
| 请求地址 | `/purchase/inventory/storageLedgerDetail/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| model | object | 是 | 查询条件对象 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | null | 是 | 接口返回traceId |
| code | number | 是 | 响应码 |

### 请求示例

```json
{
    "page":1,
    "pagesize":10,
    "model": { 
          "beginReportDate":"2023-07-10",
          "endReportDate":"2023-07-17",
           "dispositions":["CUSTOMER_DAMAGED"],
          "eventTypes":["Adjustments","WhseTransfers"],
          "mskus":["xxx","yyy"],
           "skus":["xxx","yyy"],
          "warehouseIds":[1,2,3],
          "beginUpdateTime":"2023-07-17 11:13:57",
         "endUpdateTime":"2023-07-17 12:13:57"
    }
}
```

### 响应示例

```json
{
    "traceId": "open_02dcb4a8fa20463dba98aff6d91df4c3",
    "code": 200,
    "data": {
        "total": 67518,
        "pagesize": 10,
        "page": 1,
        "rows": [
            {
                "reason": "",
                "country": "US",
                "msku": "jp-284-Bk",
                "quantity": -1,
                "fnsku": "X001V0B963",
                "updateTime": "2022-11-14 09:01:31",
                "eventType": "Shipments",
                "warehouseName": "积加测试店铺4:US_FBA",
                "referenceId": "164880979356301",
                "skuName": "",
                "fulfillmentCenter": "BFL1",
                "disposition": "SELLABLE",
                "reportDate": "2022-11-08",
                "createTime": "2022-11-14 09:01:31",
                "sourceMsku": "",
                "asin": "B07GDH6STV",
                "sku": "jp-284-Bk",
                "showDetailButton": false
            }
        ]
    },
    "messages": [
        "request.success"
    ]
}
```

---

## 157. 查询库存动作列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询库存动作列表 |
| 请求地址 | `/purchase/store/inventoryEvent/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| warehouseIds | array<long> | 否 | 仓库id集合 |
| zeroTimeZoneDateBegin | date | 否 | 开始时间 [yyyy-MM-dd] |
| zeroTimeZoneDateEnd | date | 否 | 结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize":10
}
```

### 响应示例

```json
{
    "traceId": "open_7cc4b2d80d8f4050a2b7de310f9a270e",
    "code": 200,
    "data": {
        "total": 352068,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "snapshotDate": "2021-12-14T00:00:00-08:00",
                "country": "US",
                "product": "iPhone14",
                "quantity": -1,
                "fnsku": "FNGJX0000150",
                "fulfillmentCenterId": "CVG1",
                "zeroTimeZoneDate": "2021-12-14T08:00:00",
                "updateTime": "2021-12-23T13:56:04",
                "snapshotTime": "2021-12-14T16:00:00",
                "warehouseName": "积加测试店铺3:US_FBA",
                "productName": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time",
                "marketId": 0,
                "skuName": "iPhone 14 Pro 暗紫色 1TB",
                "transactionType": "VendorReturns",
                "disposition": "CUSTOMER_DAMAGED",
                "warehouseId": 6,
                "createTime": "2021-12-17T23:20:29",
                "marketDate": "2021-12-14T00:00:00",
                "id": 1089912,
                "sku": "TEST_MSKU_GJ ERP-QWE1114"
            }
        ]
    },
    "messages": [
        "请求成功"
    ]
}
```

---

## 158. 查询FBA盘库列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA盘库列表 |
| 请求地址 | `/purchase/store/inventoryAdjustments/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | 2023-02-01之后的数据请使用FBA库存分类账接口拉取 |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| msku | string | 否 | msku |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| reasons | array | 否 | 原因 [其他: [“3”, “4”, “O”, “P”, “Q”, “G”]; 丢失: [“5”, “M”]; 已找到: [“F”, “N”]; 弃置库存: [“D”]; 已残损: [“6”, “7”, “E”, “H”, “K”, “U”]] |
| warehouseIds | array<long> | 否 | 仓库id集合 |
| zeroTimeZoneBegin | date | 否 | 开始时间(零时区) [yyyy-MM-dd] |
| zeroTimeZoneEnd | date | 否 | 结束时间(零时区) [yyyy-MM-dd] |
| disposition | string | 否 | 描述 [可售: SELLABLE; 存在瑕疵: DEFECTIVE; 因买家导致的残损: CUSTOMER_DAMAGED; 因分销商导致的残损: DISTRIBUTOR_DAMAGED; 在库房出现残损: WAREHOUSE_DAMAGED; 因承运人导致的残损: CARRIER_DAMAGED; 已过期: EXPIRED] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 10
}
```

### 响应示例

```json
{
    "traceId": "open_9974cea8a96c47138b85d68739a35912",
    "code": 200,
    "data": {
        "total": 22655,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "msku": "TEST_MSKU_GJ ERP-QWE580",
                "quantity": 1,
                "transactionItemId": 27714613850,
                "warehouseName": "积加测试店铺2:US_FBA",
                "marketId": 4,
                "warehouseId": 5,
                "id": 43552
            }
        ]
    },
    "messages": ["请求成功"]
}
```

---

## 159. 查询已接收库存列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询已接收库存列表 |
| 请求地址 | `/purchase/store/inventoryReceipts/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| marketDateEnd | date | 否 | 结束时间(市场时区) [yyyy-MM-dd] |
| page | int | 是 | 页码 |
| pagesize | int | 是 | 每页条数 [最大500条/页] |
| warehouseIds | array<long> | 否 | 仓库id集合 |
| zeroZoneDateBegin | date | 否 | 开始时间(零时区) [yyyy-MM-dd] |
| zeroZoneDateEnd | date | 否 | 结束时间(零时区) [yyyy-MM-dd] |
| marketDateBegin | date | 否 | 开始时间(市场时区) [yyyy-MM-dd] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 接口返回提示消息 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 [成功: 0; 失败:1] |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 20
}
```

### 响应示例

```json
{
    "traceId": "open_ff5bda745a794725a5352b37a1f2ae56",
    "code": 200,
    "data": {
        "total": 9835,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "product": "GJ ERP_TEST_SKU-29",
                "quantity": 72,
                "fnsku": "FNGJX0000111",
                "zeroZoneDate": 1557702000000,
                "fulfillmentCenterId": "SMF3",
                "declareQuantity": 0,
                "fbaShipmentId": "FBA15GPSXCLM",
                "warehouseName": "积加测试店铺2:US_FBA",
                "productName": "gj erp listing name, Text is a way and tool that human beings use symbols to record and express information for a long time",
                "zeroTimeZone": "2019-05-13 07:00",
                "skuName": "积加ERP测试产品465552759",
                "warehouseId": 5,
                "receivedDateStr": "2019-05-13T07:00:00+00:00",
                "marketTimeZone": "2019-05-13 00:00",
                "marketDate": 1557676800000,
                "id": 16,
                "sku": "TEST_MSKU_GJ ERP-QWE580",
                "createDate": "2019-05-23 08:00"
            }
        ]
    },
    "messages": ["请求成功"]
}
```

---

## 160. 查询FBA库龄列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询FBA库龄列表 |
| 请求地址 | `/fulfillment/inventory/inventoryAge/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| warehouseIds | array<int> | 否 | 仓库ids |
| sku | string | 否 | sku |
| fnsku | string | 否 | fnsku |
| asin | string | 否 | asin |
| productName | string | 否 | 商品名称 |
| conditions | array<string> | 否 | 商品状况集合 [Refurbished，Used，New，Collectible] |
| storageTypes | array<string> | 否 | 仓储类型 [standard-标准尺寸，oversize-大件，apparel-服装，footwear-鞋靴，flammable-易燃物，aeroso-喷雾] |
| flagTypes | array<string> | 否 | 库龄标志 [flag0to30，flag31to60，flag61to90，flag91to180，flag181to270，flag270to365，flag365] |
| beginDate | date | 否 | 报告生成查询开始日期 [yyyy-MM-dd] |
| endDate | date | 否 | 报告生成查询结束日期 [yyyy-MM-dd] |
| beginCreateDate | date | 否 | 报表创建开始时间 [yyyy-MM-dd] |
| endCreateDate | date | 否 | 报表创建结束时间 [yyyy-MM-dd] |
| beginUpdateDate | date | 否 | 系统更新开始时间 [yyyy-MM-dd] |
| beginEndDate | date | 否 | 系统更新结束时间 [yyyy-MM-dd] |
| page | int | 是 | 页码 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 是 | 返回码 |
| data | object | 是 | 返回数据 |
| messages | array<string> | 是 | 返回信息 |
| traceId | string | 是 | 链路id |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_30328d9b6b0a4fa7b50908f2fb372e78",
    "code": 200,
    "data": {
        "total": 1234,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "projectedLtsf12Mo": "0.0",
                "estimatedStorageCost": null,
                "sellThrough": "2.1735946586258885",
                "itemVolume": "89.933764",
                "fnsku": "123",
                "salesPrice": "29.99",
                "lowestPriceNew": "29.99",
                "productName": "123",
                "yourPrice": "59.99",
                "invAge331To365Days": null,
                "invAge31To60Days": 0,
                "unitsShippedLast7Days": 127,
                "id": 728560,
                "sku": "123",
                "projectedLtsf6Mo": "0.0",
                "marketplace": null,
                "invAge91To180Days": 0,
                "estimatedCostSavingsOfRemoval": "0.0",
                "condition": "New",
                "recommendedSaleDuration": 0,
                "warehouseId": 705,
                "recommendedSalesPrice": "0.0",
                "invAge365PlusDays": 0,
                "recommendedRemovalQuantity": "0",
                "updateDate": "2022-05-31 07:31:57",
                "healthyInventoryLevel": 1375,
                "invAge271To365Days": 0,
                "warehouseName": "123",
                "qtyToBeChargedLtsf12Mo": 0,
                "invAge0To30Days": 0,
                "qtyToBeChargedLtsf6Mo": 0,
                "alert": "",
                "invAge0To90Days": 1021,
                "invAge61To90Days": 0,
                "invAge271To330Days": null,
                "currency": "USD",
                "invAge181To270Days": 0,
                "cubicFeet": "cubic feet",
                "qtyWithRemovalsInProgress": 0,
                "createDate": "2022-05-31 07:31:57",
                "snapshotDate": "2022-05-28 00:00:00",
                "unitsShippedLast90Days": 2523,
                "avaliableQuantity": 1021,
                "lowestPriceUsed": "0.0",
                "recommendedAction": "Improve recommendations",
                "imgUrl": "https://m.media-amazon.com/images/I/1234.jpg",
                "storageType": "标准尺寸",
                "asin": "123",
                "unitsShippedLast60Days": 1460,
                "unitsShippedLast30Days": 569
            }
        ]
    },
    "messages": [
        "请求成功"
    ]
}
```

---

## 161. FBA库存分类账-一览视图-按月维度列表查询

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | FBA库存分类账-一览视图-按月维度列表查询 |
| 请求地址 | `/fulfillment/inventory/storageLedgerMonth/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 5次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | 请求token |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | int | 是 | 第几页 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| warehouseIdList | array<int> | 否 | 仓库id集合 |
| startUpdateTime | date | 否 | 报告更新时间-开始日期 [yyyy-MM-dd] |
| endUpdateTime | date | 否 | 报告更新时间-结束日期 [yyyy-MM-dd] |
| monthList | array<string> | 是 | 月份集合，月份格式：[yyyy-MM] |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| code | int | 否 | 服务端响应码 |
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 返回的提示信息 |
| traceId | string | 否 | 链路追踪id |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1,
    "monthList": ["2022-01"]
}
```

### 响应示例

```json
{
    "traceId": "open_190e832629f74c6babdce731a622670a",
    "code": 200,
    "data": {
        "total": 3744,
        "pagesize": 1,
        "page": 1,
        "rows": [
            {
                "country": "ES",
                "fnsku": "X001AAQRNB",
                "warehouseName": "Group2-EU:EU_FBA",
                "unknownEvents": 0,
                "otherEvents": 0,
                "marketId": 0,
                "vendorReturns": 0,
                "found": 0,
                "reportDate": "2022-01",
                "lost": 0,
                "warehouseTransferInAndOut": 0,
                "disposed": 0,
                "id": null,
                "sku": "Q-WJJM200802",
                "msku": "CH20067SCVC",
                "startingWarehouseBalance": 0,
                "endingWarehouseBalance": 1,
                "updateTime": "2022-10-28 16:03:52",
                "inTransitBetweenWarehouses": 0,
                "customerShipments": 0,
                "receipts": 0,
                "disposition": "CUSTOMER_DAMAGED",
                "warehouseId": 106,
                "createTime": "2022-10-28 16:03:52",
                "sourceMsku": "CH20067SCVC",
                "damaged": 0,
                "asin": "B08KDTKZY3",
                "customerReturns": 1
            }
        ]
    },
    "messages": []
}
```

---

## 162. 查询多平台销售订单

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询多平台销售订单 |
| 请求地址 | `/platform/multiplatform/commonOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| marketPolymerizeIds | array<int> | 否 | 聚合店铺id集合 |
| msku | string | 否 | MSKU |
| orderCategory | string | 否 | 订单类别：standard 标准订单, multi_channel 多渠道订单 |
| omsPushStatus | int | 否 | 自发货推送状态 [0:不推送，1:待推送，2:推送成功，3:推送失败] |
| orderCancelStatus | int | 否 | 取消状态 [ 0:未取消，2:部分取消，3:已取消] |
| orderRefundStatus | int | 否 | 退款状态 [ 0:无退款，1:部分退款，2:全额退款] |
| platformOrderPerformingParty | int | 否 | 履约方 [0-自发货，1-平台发货，2-自发货、平台发货] |
| orderDeliveryStatus | int | 否 | 平台发货状态 [0-未发货，1-全部发货，2-部分发货] |
| page | int | 是 | 第几页 |
| pagesize | int | 是 | 每页条数 [最大100条/页] |
| platformId | string | 否 | 平台编码 [参考QA文档-全局参数-多平台编码] |
| platformOrderIds | array<string> | 否 | 平台订单编码 |
| platformOrderNumbers | array<string> | 否 | 平台单号编码（shopify请使用该字段查询） |
| viewPlatformOrderIdList | array<string> | 否 | 平台展示单号 |
| platformOrderStatusList | array<string> | 否 | 平台订单状态 [参考QA文档-全局参数-多平台状态] |
| updateTimeQueryBegin | datetime | 否 | 开始更新时间(北京时区) [yyyy-MM-dd HH:mm:ss] |
| updateTimeQueryEnd | datetime | 否 | 结束更新时间(北京时区) [yyyy-MM-dd HH:mm:ss] |
| timeType | string | 否 | 时间筛选类型(BEIJING:北京时区,UTC:零时区,MARKET:市场时区, 默认BEIJING) |
| orderingTimeQueryBegin | datetime | 否 | 开始订购时间(timeType) [yyyy-MM-dd HH:mm:ss] |
| orderingTimeQueryEnd | datetime | 否 | 结束订购时间(timeType) [yyyy-MM-dd HH:mm:ss] |
| paymentTimeQueryBegin | datetime | 否 | 开始付款时间(timeType) [yyyy-MM-dd HH:mm:ss] |
| paymentTimeQueryEnd | datetime | 否 | 结束付款时间(timeType) [yyyy-MM-dd HH:mm:ss] |
| deliveryTimeQueryBegin | datetime | 否 | 开始发货时间(timeType) [yyyy-MM-dd HH:mm:ss] |
| deliveryTimeQueryEnd | datetime | 否 | 结束发货时间(timeType) [yyyy-MM-dd HH:mm:ss] |
| erpShopIds | array<int> | 否 | 店铺ID |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 返回结果消息内容 |
| traceId | string | 否 | 跟踪号 |
| code | int | 否 | 响应码 |

### 请求示例

```json
{
    "page": 1,
    "pagesize": 1
}
```

### 响应示例

```json
{
    "traceId": "open_da51525062a345c485b5772ea5ae8875",
    "code": 200,
    "data": {
        "total": 53,
        "records": [
            {
                "orderPerformingParty": 0,
                "orderType": "基础",
                "erpShopName": "Shopee测试店铺",
                "orderDeliveryStatus": 0,
                "omsPushErrorMessage": "订单状态为已发货状态",
                "receiverMobilePhone": null,
                "orderingTime": "2023-03-19 18:32:20",
                "buyerAccountId": "149272538",
                "receiverPhone": "******39",
                "platformWarehouseName": null,
                "id": "1676107371982450690",
                "refundedTotalAmount": null,
                "customerMemo": null,
                "regionCnName": "马来西亚",
                "omsPushStatus": 0,
                "tax": null,
                "receiverAddressPostCode": "",
                "totalAmount": "826333",
                "orderCancelStatusName": "未取消",
                "platformOrderDeliveryTime": null,
                "platformOrderPaymentMethod": "COD",
                "soOrderNumber": null,
                "items": [
                    {
                        "platformOrderLineId": "232***********159052",
                        "orderId": "16761********450690",
                        "productTotalPrice": "49833",
                        "trackingNumberList": null,
                        "memo": null,
                        "productUnitPrice": "49833",
                        "buyQuantity": 1,
                        "platformOrderLineStatus": null,
                        "platformOrderLineNumber": null,
                        "productName": "********",
                        "skuName": null,
                        "goodsLocation": "CNZ",
                        "shippedQuantity": null,
                        "giftStatus": null,
                        "currency": "VND",
                        "id": "1676107371982450691",
                        "platformOrderId": "130******",
                        "sku": null,
                        "trackingNumber": null,
                        "skuLogisticsProperties": null,
                        "msku": "X*****6",
                        "productId": "23229719907",
                        "linePerformingParty": 0,
                        "buyerChooseLogistics": "Standard Express",
                        "productMainImageUrl": "https://cf.shopee.vn/file/ph-********n",
                        "listingUrl": "https://my.xiapibuy.com/product/5********",
                        "shippingTerm": null,
                        "platformOrderLineStatusName": null
                    }
                ],
                "viewPlatformOrderId": "130312JN6M1TMT",
                "orderRefundStatus": null,
                "receiverAddressArea": "Thị Trấn Liên Nghĩa",
                "timeTypeDesc": "北京时区",
                "baseCurrency": "CNY",
                "receiverAddressCountry": "Vietnam",
                "orderRefundStatusName": null,
                "buyerPayShipFee": "30000",
                "marketPolymerizeId": 1000220,
                "currency": "VND",
                "platformOrderStatus": "RETRY_SHIP",
                "platformOrderId": "130312JN6M1TMT",
                "paymentTime": null,
                "cancelReason": "",
                "omsPushStatusName": "不推送自发货",
                "platformWarehouseId": null,
                "receiverAddressState": "Lâm Đồng",
                "platformOrderStatusName": "重新揽收",
                "buyerAccountName": "tolong6839",
                "buyerAccountEmail": null,
                "platformCommission": "27953.28",
                "receiverName": "t******g",
                "estimateLatestDeliveryTime": "2023-03-23 00:30:00",
                "updateTime": "2023-09-19 10:15:56",
                "platformId": "SHOPEE",
                "receiverAddressCity": "Huyện Đức Trọng",
                "receiverAddressCountryCode": "VN",
                "buyerMessage": "",
                "transactionFee": "9111.1",
                "regionId": "202002",
                "buyerPayAmount": "455555",
                "platformOrderNumber": null,
                "receiverAddressDetail1": "39******",
                "orderCancelStatus": 0,
                "erpShopId": "1650771149945131010",
                "buyerTaxNumber": null,
                "receiverAddressDetail2": null
            }
        ],
        "pageSize": 20,
        "pageCurrent": 1
    },
    "messages": [
        "操作成功"
    ]
}
```

---

## 163. 查询多平台店铺信息

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 查询多平台店铺信息 |
| 请求地址 | `/platform/multiplatform/multiShop/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 2次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | array<object> | 是 | 接口返回数据 |
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{
    "traceId": "open_a22b1eb7d3ab4abcbc42efeda87b02b9",
    "code": 200,
    "data": [
        {
            "regionId": "204001",
            "countryCode": "US",
            "marketPolymerizeId": 1000957,
            "shopName": "测试店铺",
            "shopId": "1071",
            "platformId": "WALMART",
            "status": 0
        }
    ],
    "messages": [
        "操作成功"
    ]
}
```

---

## 164. 沃尔玛销售订单主列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 沃尔玛销售订单主列表 |
| 请求地址 | `/platform/multiplatform/walmartOrderSimple/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| size | int | 否 | 页大小 |
| current | int | 否 | 页码 |
| model | object | 否 |  |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 返回数据 |
| messages | array<string> | 否 | 提示信息 |
| traceId | string | 是 | 接口返回traceId |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "current": 1,
    "size": 1
}
```

### 响应示例

```json
{}
```

---

## 165. 沃尔玛销售订单

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 沃尔玛销售订单 |
| 请求地址 | `/platform/multiplatform/walmartOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| current | int | 是 | 页码 |
| size | int | 是 | 每页条数 [最大100条/页] |
| model | object | 是 | 查询条件 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |
| data | object | 是 | 接口返回数据 |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "current": 1,
    "size": 1,
    "model": {
        "currencyCode": "USD"
    }
}
```

### 响应示例

```json
{
    "traceId": "open_b315b5354e1f41a7adb389a64b2bb783",
    "code": 200,
    "data": {
        "total": 610,
        "current": 1,
        "size": 1,
        "records": [
            {
                "shippingAddressAddress1": "4 Brae St",
                "country": "US",
                "orderType": "普通订单",
                "lineItemPrice": 29.59,
                "shippingAddressState": "RI",
                "customerEmailId": "84C33A********.walmart.com",
                "originalCustomerOrderId": "",
                "customerOrderId": "*********",
                "shippingAddressName": "S******eiro",
                "shippingAddressAddress2": "",
                "orderLineQuantity": 1,
                "productName": null,
                "marketId": "1523*******17",
                "lineStatus": "Delivered",
                "shippingMethodCode": "Standard",
                "chargeItemPrice": 27.65,
                "platformWarehouseName": null,
                "itemProductName": "NBW************* Yellow",
                "chargeShippingPrice": 0.0,
                "marketPolymerizeId": 1000970,
                "orderDateCst": "2022-05-19T06:20:13",
                "sku": null,
                "trackUrl": "https://www.walmart.com/tracking?order_id=3***********&tracking_id=***********98",
                "platformWarehouseId": 284,
                "statusQuantity": 1,
                "shippingAddressCity": "North Providence",
                "trackNumber": "*************",
                "shipNodeType": "SellerFulfilled",
                "updateTime": "2022-08-31T17:14:21",
                "itemMsku": "ZYX-*******",
                "shippingAddressCountry": "USA",
                "itemId": "313032292",
                "marketName": "ZY_Walmart-NBW-WMRT-NA",
                "purchaseOrderId": "3871394296526",
                "shippingAddress": "4*******",
                "shippingAddressPostalCode": "02911",
                "lineNumber": "1",
                "taxAmount": 1.94,
                "trackCarrierName": "Fedex",
                "orderDate": "2022-05-18T15:20:13",
                "currencyCode": "USD"
            }
        ]
    },
    "messages": [
        "成功"
    ]
}
```

---

## 166. 沃尔玛退货订单

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 沃尔玛退货订单 |
| 请求地址 | `/platform/multiplatform/walmartReturnOrder/page` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| current | int | 是 | 页码 |
| size | int | 是 | 每页条数 [最大100条/页] |
| model | object | 是 | 查询条件 |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| messages | array<string> | 是 | 接口返回提示消息 |
| traceId | string | 是 | 接口返回traceId |
| data | object | 是 | 接口返回数据 |
| code | int | 是 | 响应码 |

### 请求示例

```json
{
    "current": 1,
    "size": 1,
    "model": {
        "currencyCode": "USD"
    }
}
```

### 响应示例

```json
{
    "traceId": "open_6c15e73e1f5349f7bde664e993b6c29b",
    "code": 200,
    "data": {
        "total": 40,
        "current": 1,
        "size": 1,
        "records": [
            {
                "country": "US",
                "customerEmailId": "1***********@relay.walmart.com",
                "customerOrderId": "********",
                "returnOrderLineNumber": "1",
                "lineUnitPrice": 14.12,
                "returnStatus": "COMPLETED",
                "productName": null,
                "currentDeliveryStatus": "DELIVERED_TO_RC",
                "marketId": 1523964771361775617,
                "refundedQty": 1,
                "returnReason": "INCORRECT_ITEM",
                "itemProductName": "J********",
                "statusTime": "2022-06-15 09:20:43",
                "currentRefundStatus": "REFUND_COMPLETED",
                "returnOrderId": "137296533434206192",
                "shipNodeTypeDesc": "自配送",
                "marketPolymerizeId": 1000970,
                "lineProductTaxes": 1.24,
                "id": 1534407889498484737,
                "sku": null,
                "lineTotal": 15.36,
                "shipNodeType": "SellerFulfilled",
                "updateTime": "2022-08-02 09:46:11",
                "refundChannel": "WALMART_TRIGGERED_REFUND",
                "returnChannel": "MyAccount",
                "currentDeliveryTime": "2022-06-15 09:20:43",
                "customerName": "EstherDixon",
                "itemMsku": "ZYX-*******",
                "currentRefundTime": "2022-06-15 09:20:43",
                "itemId": "151730649",
                "marketName": "ZY_*********",
                "replacementCustomerOrderId": "",
                "returnOrderDate": "2022-06-07 22:30:39",
                "returnByDate": "2022-06-14 17:00:00",
                "purchaseOrderId": "9871252638713",
                "refundMode": "FIRST_SCAN",
                "currencyCode": "USD",
                "returnType": "退款",
                "refundedLineAmount": 15.36
            }
        ]
    },
    "messages": [
        "成功"
    ]
}
```

---

## 167. 获取多平台仓库列表

### 基本信息

| 项目 | 内容 |
|------|------|
| 接口名称 | 获取多平台仓库列表 |
| 请求地址 | `/platform/multiplatform/multiShopWarehouse/query` |
| 请求方式 | POST |
| 限流规则 | 每 1秒 1次 |
| 接口说明 | - |

### 请求头参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| accessToken | string | 是 | accessToken |

### 请求体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| erpWarehouseIds | array<int> | 否 | erp仓库ID |
| pageCurrent | long | 是 | 当前页码 |
| pageSize | long | 是 | 单页返回的数据条数 |
| platformCode | string | 是 | 平台编码 |
| erpShopIds | array<string> | 否 | erp店铺ID |

### 响应体参数

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| data | object | 否 | 接口返回数据 |
| messages | array<string> | 否 | 返回结果消息内容 |
| traceId | string | 否 | 接口返回traceId |
| code | int | 否 | 响应码 |

### 请求示例

```json
{}
```

### 响应示例

```json
{
    "traceId": "open_a22b1eb7d3ab4abcbc42efeda87b02b9",
    "code": 200,
    "data": [
        {
            "regionId": "204001",
            "countryCode": "US",
            "marketPolymerizeId": 1000957,
            "shopName": "测试店铺",
            "shopId": "1071",
            "platformId": "WALMART",
            "status": 0
        }
    ],
    "messages": [
        "操作成功"
    ]
}
```

---

