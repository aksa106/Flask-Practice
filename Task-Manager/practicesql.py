

import sqlite3
from pathlib import Path 


db_path = Path(__file__).resolve().parent/"tasks.db"


connection = sqlite3.connect(db_path)

##-------------------------------------------------------

# Filtering

# cursor = connection.execute(
#     "SELECT * FROM tasks WHERE priority = ?",
#     ("High",)
# )

# tasks = cursor.fetchall()




## Order By

# cursor1 = connection.execute(
#     "Select * from tasks order by due_date ASC"
# )

# order_by = cursor1.fetchone()

# print(order_by)



## Limit

# cursor2 = connection.execute(
#     "select * from tasks limit 2"
# )

# limit = cursor2.fetchall()

# print(limit)


###-----------------------------------------------

#                  UPDATE

######################################################



# UPDATE table_name
# SET column_name = value 
# WHERE condition




# cursor3 = connection.execute("UPDATE tasks SET priority = ? WHERE id = ?", ("High", 1))

# connection.commit()



# cursor4 = connection.execute("Select * from tasks where id = ?", (1,))

# update = cursor4.fetchall()

# print(update)


########################################################

#                DELETE

########################################################


# DELETE FROM table_name
# WHERE condition;


## delete task with id = 3 

# connection.execute("DELETE FROM tasks WHERE id = ?", (3,))



# connection.commit()



# cursor5 = connection.execute("select id from tasks")

# delete = cursor5.fetchall()

# print(delete)










# connection.close()