

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


connection.close()


























