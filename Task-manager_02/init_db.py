import sqlite3 
from pathlib import Path 

db_path = Path(__file__).resolve().parent/'tasks.db'

connection = sqlite3.connect(db_path)


connection.execute(""" 

    CREATE TABLE IF NOT EXISTS tasks(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT DEFAULT 'No description provided',
        priority TEXT NOT NULL 
            CHECK(priority in ('High', 'Medium', 'Low')),
        due_date TEXT DEFAULT NULL,
        status TEXT NOT NULL 
            CHECK(status in ('Pending', 'In Progress', 'Completed'))
    )
""")


cursor = connection.execute("PRAGMA table_info(tasks)")
print(cursor.fetchall())


connection.commit()
connection.close()

print("Database initialized successfully:", db_path)












































