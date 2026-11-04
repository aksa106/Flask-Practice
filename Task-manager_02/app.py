from flask import Flask , render_template, request, url_for, redirect, flash


app = Flask(__name__)


tasks = []

@app.route('/')
def home():
    return render_template('home.html')


#####################################################

#                  Add Task 



@app.route('/add_task', methods =['GET','POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('desc')
        priority = request.form.get('priority')
        due_date = request.form.get('date')
        status = request.form.get('status')


        ## Temporarely making a python list to store task 

        task = {
            'title' : title ,
            'description' : description,
            'priority' : priority,
            'due_date' : due_date,
            'status' : status 
        }

        tasks.append(task)




        return redirect(url_for('view_task'))

    return render_template('add_task.html')




####################################################

#                  VIEW TASK

@app.route('/view_task')
def view_task():
    
    return render_template('view_task.html', tasks=tasks)





app.run(debug=True)






