CREATE TABLE IF NOT EXISTS issues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    cover_image TEXT,
    published_date TEXT  -- formato recomendado: 'YYYY-MM-DD'
);

CREATE TABLE IF NOT EXISTS team (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    photo TEXT,
    description TEXT
);
