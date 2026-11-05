import sqlite3



connection = sqlite3.connect('tasks.db')


#######################################################################

#                     PRACTICING ROLLBACK

#######################################################################

connection.execute(
    """
    INSERT INTO tasks(title, description, priority, due_date, status)
    VALUES(?,?,?,?,?)
    """,
        ('Learn Flask', 'Practice rollback', 'High', '2026-11-05','Pending')
    )


print("BEFORE ROLL BACK : ")
print()

print(connection.execute("Select * from tasks").fetchall())

print()

connection.rollback()

print("AFTER ROLL BACK : ")
print()

print(connection.execute("select * from tasks").fetchall())


connection.close()




#-----------------------------------------------------------------------



# Important rules
# Rollback only undoes changes made since the last commit.
# It cannot undo changes that have already been committed.
# It works with INSERT, UPDATE, DELETE and other transactional operations.
# You don't need rollback after SELECT.

# Remember: commit() = Save changes. rollback() = Undo uncommitted changes.





