#!/usr/bin/env python3
"""
积加ERP开放平台API调用脚本 - 支持JSON输出和Excel导出
"""
import requests
import json
import os
import sys
from typing import Optional, Dict, Any, List

class GerpGOClient:
    """积加API客户端"""

    BASE_URL = "https://open.gerpgo.com"

    def __init__(self, app_key: str, app_id: str):
        self.app_key = app_key
        self.app_id = app_id
        self.access_token: Optional[str] = None
        self.token_expires_at: Optional[int] = None

    def get_token(self) -> str:
        """获取accessToken"""
        url = f"{self.BASE_URL}/api/open/api_token"
        payload = {
            "appKey": self.app_key,
            "appId": self.app_id
        }
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        result = resp.json()

        if result.get("code") not in (0, 200):
            raise Exception(f"获取token失败: {result.get('messages')}")

        self.access_token = result["data"]["accessToken"]
        self.token_expires_at = result["data"]["expiresIn"]
        return self.access_token

    def call(self, endpoint: str, method: str = "POST",
             data: Optional[Dict] = None) -> Dict[str, Any]:
        """调用API接口"""
        if not self.access_token:
            self.get_token()

        # 确保endpoint以/开头，避免MSYS路径转换问题
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        url = f"{self.BASE_URL}/api/open{endpoint}"
        headers = {
            "accessToken": self.access_token,
            "Content-Type": "application/json"
        }

        if method.upper() == "POST":
            resp = requests.post(url, json=data, headers=headers, timeout=120)
        else:
            resp = requests.get(url, params=data, headers=headers, timeout=120)

        resp.raise_for_status()
        return resp.json()


def json_to_excel(data: Any, output_path: str, sheet_name: str = "Sheet1"):
    """将JSON数据（列表或包含data字段的dict）导出为Excel文件"""
    from openpyxl import Workbook

    # 提取列表数据 - 支持多层嵌套
    if isinstance(data, dict):
        if "data" in data and isinstance(data["data"], dict):
            # 处理 {data: {rows: [...]}} 结构
            sub = data["data"]
            if "rows" in sub:
                rows = sub["rows"]
            elif "records" in sub:
                rows = sub["records"]
            elif "list" in sub:
                rows = sub["list"]
            else:
                rows = [sub]
        elif "data" in data and isinstance(data["data"], list):
            rows = data["data"]
        elif "records" in data:
            rows = data["records"]
        elif "list" in data:
            rows = data["list"]
        else:
            rows = [data]
    elif isinstance(data, list):
        rows = data
    else:
        rows = [data]

    if not rows:
        print("警告: 没有数据可导出")
        return

    # 确保rows是列表
    if not isinstance(rows, list):
        rows = [rows]

    # 展平嵌套字典，收集所有字段
    def flatten(obj: Any, prefix: str = "") -> Dict[str, Any]:
        result = {}
        if isinstance(obj, dict):
            for k, v in obj.items():
                fk = f"{prefix}.{k}" if prefix else k
                if isinstance(v, (dict, list)):
                    if isinstance(v, list) and all(not isinstance(i, (dict, list)) for i in v):
                        result[fk] = json.dumps(v, ensure_ascii=False)
                    elif isinstance(v, dict):
                        result.update(flatten(v, fk))
                    else:
                        result[fk] = json.dumps(v, ensure_ascii=False)
                else:
                    result[fk] = v
        return result

    flat_rows = [flatten(r) for r in rows]

    # 收集所有字段作为表头
    all_keys: List[str] = []
    seen = set()
    for r in flat_rows:
        for k in r:
            if k not in seen:
                all_keys.append(k)
                seen.add(k)

    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name

    # 写入表头
    ws.append(all_keys)

    # 写入数据行
    for r in flat_rows:
        ws.append([r.get(k, "") for k in all_keys])

    wb.save(output_path)
    print(f"Excel已导出: {output_path} ({len(flat_rows)} 行, {len(all_keys)} 列)")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="积加ERP开放平台API调用工具")
    parser.add_argument("endpoint", help="API接口地址，如 /operation/crm/review/page")
    parser.add_argument("--app-key", help="appKey，默认从环境变量 GERPGO_APP_KEY 读取")
    parser.add_argument("--app-id", help="appId，默认从环境变量 GERPGO_APP_ID 读取")
    parser.add_argument("--data", "-d", help="请求体JSON字符串")
    parser.add_argument("--data-file", "-f", help="从文件读取请求体JSON")
    parser.add_argument("--excel", "-o", help="导出为Excel文件路径 (如 output.xlsx)")
    parser.add_argument("--sheet", help="Excel工作表名称", default="Sheet1")
    parser.add_argument("--pretty", "-p", action="store_true", help="格式化打印JSON")

    args = parser.parse_args()

    app_key = args.app_key or os.getenv("GERPGO_APP_KEY", "")
    app_id = args.app_id or os.getenv("GERPGO_APP_ID", "")

    if not app_key or not app_id:
        print("错误: 请提供 --app-key 和 --app-id，或设置环境变量 GERPGO_APP_KEY 和 GERPGO_APP_ID")
        sys.exit(1)

    # 解析请求体
    payload = None
    if args.data:
        payload = json.loads(args.data)
    elif args.data_file:
        with open(args.data_file, "r", encoding="utf-8") as f:
            payload = json.load(f)

    client = GerpGOClient(app_key, app_id)
    result = client.call(args.endpoint, data=payload)

    if args.excel:
        json_to_excel(result, args.excel, args.sheet)
    elif args.pretty:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
