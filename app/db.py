import sqlite3

DATABASE_URL = "local_database.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_URL)
    return conn
