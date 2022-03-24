CREATE_MESSAGE_ID_TABLE = """
    CREATE TABLE IF NOT EXISTS message_ids (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    breakfast TEXT,
    lunch TEXT,
    dinner TEXT,
    syrup_1 TEXT,
    syrup_2 TEXT,
    iron TEXT,
    vitamin TEXT,
    regular TEXT
    );
"""

CREATE_RECORD_TABLE = """
    CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    breakfast TEXT,
    lunch TEXT,
    dinner TEXT,
    syrup_1 TEXT,
    syrup_2 TEXT,
    iron TEXT,
    vitamin TEXT,
    regular TEXT,
    date TEXT
    );
"""

CREATE_OFFSET_TABLE = """
    CREATE TABLE IF NOT EXISTS message_ids (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    offset TEXT,
    );
"""