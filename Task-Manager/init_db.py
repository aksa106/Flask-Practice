
import sqlite3
from pathlib import Path

# Use the database file inside this project folder
db_path = Path(__file__).resolve().parent / "tasks.db"

connection = sqlite3.connect(db_path)

connection.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT NOT NULL,
        due_date TEXT
    )
""")

connection.commit()

# Verify the table exists
cursor = connection.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())

connection.close()

print("Database initialized successfully:", db_path)

