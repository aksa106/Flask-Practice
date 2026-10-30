
import sqlite3
from pathlib import Path

# Use the database file inside this project folder
db_path = Path(__file__).resolve().parent / "tasks.db"

connection = sqlite3.connect(db_path)

connection.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT DEFAULT 'No description provided',
        priority TEXT NOT NULL CHECK (priority IN ('High', 'Medium','Low')),
        due_date TEXT DEFAULT NULL
    )
""")

connection.commit()

# Verify the table exists
cursor = connection.execute('SELECT * FROM tasks')

print("One row:", cursor.fetchone())
print("Next two rows:", cursor.fetchmany(2))
print("Remaining rows:", cursor.fetchall())

connection.close()

print("Database initialized successfully:", db_path)























