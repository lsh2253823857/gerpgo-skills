-- ============================================================
-- Enterprise Knowledge Base — SQLite Schema
-- ============================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- ============================================================
-- 1. 用户表
-- ============================================================
CREATE TABLE users (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    username        TEXT    NOT NULL UNIQUE,
    display_name    TEXT    NOT NULL,
    role            TEXT    NOT NULL CHECK (role IN ('admin', 'editor', 'viewer')),
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- 2. 分类表（adjacency list 树形结构）
-- ============================================================
CREATE TABLE categories (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT    NOT NULL,
    description     TEXT,
    parent_id       INTEGER REFERENCES categories(id) ON DELETE SET NULL,
    sort_order      INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- 3. 文档表
-- ============================================================
CREATE TABLE documents (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    title           TEXT    NOT NULL,
    content         TEXT,
    category_id     INTEGER NOT NULL REFERENCES categories(id),
    created_by      INTEGER NOT NULL REFERENCES users(id),
    status          TEXT    NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'archived')),
    is_deleted      BOOLEAN DEFAULT 0,
    view_count      INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- 4. 标签表
-- ============================================================
CREATE TABLE tags (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT    NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- 5. 文档-标签关联表（多对多）
-- ============================================================
CREATE TABLE document_tags (
    document_id     INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    tag_id          INTEGER NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (document_id, tag_id)
);

-- ============================================================
-- 6. 文档版本历史表
-- ============================================================
CREATE TABLE document_versions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id     INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    version_number  INTEGER NOT NULL,
    title_snapshot  TEXT    NOT NULL,
    content_snapshot TEXT,
    changed_by      INTEGER NOT NULL REFERENCES users(id),
    change_summary  TEXT,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (document_id, version_number)
);

-- ============================================================
-- 7. 附件表（存路径不存 BLOB）
-- ============================================================
CREATE TABLE attachments (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id     INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    filename        TEXT    NOT NULL,
    file_path       TEXT    NOT NULL,
    mime_type       TEXT,
    file_size       INTEGER,
    uploaded_by     INTEGER NOT NULL REFERENCES users(id),
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- 8. 搜索日志表
-- ============================================================
CREATE TABLE search_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         INTEGER NOT NULL REFERENCES users(id),
    query_text      TEXT    NOT NULL,
    results_count   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- FTS5 全文搜索虚拟表
-- ============================================================
CREATE VIRTUAL TABLE documents_fts USING fts5(
    title,
    content,
    content='documents',
    content_rowid='id',
    tokenize='unicode61'
);

-- FTS 同步触发器 — INSERT
CREATE TRIGGER documents_ai AFTER INSERT ON documents BEGIN
    INSERT INTO documents_fts(rowid, title, content)
    VALUES (new.id, new.title, new.content);
END;

-- FTS 同步触发器 — UPDATE
CREATE TRIGGER documents_au AFTER UPDATE ON documents BEGIN
    INSERT INTO documents_fts(documents_fts, rowid, title, content)
    VALUES ('delete', old.id, old.title, old.content);
    INSERT INTO documents_fts(rowid, title, content)
    VALUES (new.id, new.title, new.content);
END;

-- FTS 同步触发器 — DELETE
CREATE TRIGGER documents_ad AFTER DELETE ON documents BEGIN
    INSERT INTO documents_fts(documents_fts, rowid, title, content)
    VALUES ('delete', old.id, old.title, old.content);
END;

-- ============================================================
-- 索引
-- ============================================================
CREATE INDEX idx_categories_parent      ON categories(parent_id);
CREATE INDEX idx_documents_category     ON documents(category_id);
CREATE INDEX idx_documents_created_by   ON documents(created_by);
CREATE INDEX idx_documents_status       ON documents(status, is_deleted);
CREATE INDEX idx_document_tags_doc      ON document_tags(document_id);
CREATE INDEX idx_document_tags_tag      ON document_tags(tag_id);
CREATE INDEX idx_document_versions_doc  ON document_versions(document_id);
CREATE INDEX idx_attachments_doc        ON attachments(document_id);
CREATE INDEX idx_search_log_user        ON search_log(user_id);
CREATE INDEX idx_search_log_time        ON search_log(created_at);
