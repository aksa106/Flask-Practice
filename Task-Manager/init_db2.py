



from pathlib import path 
import sqlite3 


db_path = path(__file__).resolve().parent/"tasks.db"

connection = sqlite3.connect(db_path)

connection.execute(
"""
    Create table if not exists 
    tasks(
        id integer primary key autoincrement,

        title text not null,

        description text default 'no description provided',

        priority text not null check(priority ib ('high', 'medium', 'low')),

        due_date text default null
    
    )
"""
)


connection.commit()


connection.close()

















