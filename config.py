"""Enterprise Knowledge Base — 数据库配置"""
import sqlite3
from pathlib import Path

# __file__ = 本文件路径
# .parent = 上一级目录（enterprise-kb/）
# / "db" / "enterprise_kb.db" = 拼接完整路径
DB_PATH = Path(__file__).parent / "db" / "enterprise_kb.db"


def get_connection() -> sqlite3.Connection:
    """返回一个配置好的 SQLite 连接"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")          # 启用外键约束
    conn.row_factory = sqlite3.Row                     # 查询结果能用 row['列名'] 访问
    return conn
