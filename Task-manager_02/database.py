
import sqlite3 
from pathlib import Path 


DB_PATH = Path(__file__).resolve().parent/'tasks.db'


def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection





if __name__ == '__main__':

    con = get_db_connection()

    tasks = con.execute("select * from tasks").fetchall()

    for task in tasks:
        print(dict(task))


    con.close()










