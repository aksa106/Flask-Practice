from database import get_db_connection
from flask import  Flask , render_template, request, url_for, redirect, abort

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('home.html')




#####################################################

#                  Add Task 


#####################################################



@app.route('/add_task', methods =['GET','POST'])
def add_task():

    ##########################################
#      RETRIEVING FORM VALUES THROUGH POST
    ########################################## 

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('desc')
        priority = request.form.get('priority')
        due_date = request.form.get('date')
        status = request.form.get('status')


        ###################################
    #   AFTER RETRIEVING VALUES, CONNECT THE
    #   DB 
        #####################################

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO tasks(title, description, priority, due_date, status)
            VALUES(?,?,?,?,?)
            """,
            (title, description, priority, due_date, status)
        )
       
        connection.commit()
        connection.close()
 




        return redirect(url_for('view_task'))

    return render_template('add_task.html')







####################################################

#                  VIEW TASK

####################################################

@app.route('/view_task')
def view_task():

    ################################################

#           connect databasse to display the stored 
#            tasks

    ################################################

    connection = get_db_connection()

    tasks = connection.execute("SELECT * FROM tasks").fetchall()


    connection.close()

    return render_template('view_task.html', tasks=tasks)




###############################################################


#               RETRIEVE TASKS USING TASK ID 


###############################################################

@app.route('/task/<int:task_id>')
def task_detail(task_id):

    connection = get_db_connection()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    if task is None:
        abort(404)

    return render_template('task_detail.html', task=task)





################################################################
if __name__ == '__main__':
    app.run(debug=True)






