import sqlite3 
from pathlib import Path 



#######################################################################

#             MAKING DB PATH ABSSOLUTE AND CRETAING A DATABASE : tasks.db




db_path = Path(__file__).resolve().parent/'tasks.db'


## Database Creation
connection = sqlite3.connect(db_path)

print("Database initialized successfully:", db_path)



#######################################################################



#               CREATING A TABLE : tasks



#######################################################################


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


#         [COMMITING TO TABLE : tasks]



# connection.commit()




#######################################################################


#                       INSERTING RECORDS 


#######################################################################


connection.execute(
    """
    INSERT INTO tasks(title, description, priority, due_date, status)
    VALUES(?,?,?,?,?)
    """, ('Learn Flask','Practice sqlite3','High','05-11-2026','In Progress')
)



#                    [] COMMITTING TO INSERTED RECORDS]



#connection.commit()



#######################################################################

#                ALTER TABLE (making changes in table schema)

#######################################################################



# Add a new column

connection.execute(
    """
    ALTER TABLE tasks
    ADD COLUMN created_at TEXT

    """
)

#                    COMMITING TO ALTERED RECORDS 

connection.commit()



#######################################################################

#                      DELETING A COLUMN 


#Delete the newly added column 

connection.execute("""

ALTER TABLE tasks 
DROP COLUMN created_at


    """)

#                committing to changes

connection.commit()

#######################################################################

#                  RERIEVING RECORDS / READING 

#######################################################################


cursor = connection.execute("Select * from tasks")

for task in cursor.fetchall():
    print(task)

print(cursor.fetchmany(1))



#######################################################################


#                CLOSING CONNECTION 

#######################################################################



connection.close()


#-------------------------------------------------------------------------












































