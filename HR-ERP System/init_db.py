
## Emp ID , Name , Email, Mobile, Designzation , Salry

import sqlite3
from pathlib import Path 

db_path = Path(__file__).resolve().parent/'employee.db'

connection = sqlite3.connect(db_path)


connection.execute(

    """
        Create table if not exists employee(
        
        EmpID integer primary key autoincrement,
        name text not null,
        email text not null,
        mobile integer ,
        designation text not null,
        salary real not null
        
        
        )
    """
)


connection.execute("""
    CREATE TABLE employee_new (

        EmpID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        mobile INTEGER,
        designation TEXT NOT NULL,
        salary REAL NOT NULL

    )
""")










connection.commit()


cursor = connection.execute('Select * from employee')

print(f"employee data : {cursor}")
print(cursor.fetchall())

connection.close()












