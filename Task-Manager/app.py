from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/add_task')
def add_task():
    return render_template('add_task.html')


#----------------------------------------------------------------------------


@app.route('/view_task')
def view_task():

    tasks = [
        # {
        #     "id" : 1,
        #     "title" : "Practice Python",
        #     "description" : "Solve function problems",
        #     "priority" : "High",
        #     "due_date" : "2026-11-01"

        # },

        # {
        #         "id" : 2,
        #         "title" : "Practice Python",
        #         "description" : "Solve function problems",
        #         "priority" : "High",
        #         "due_date" : "2026-11-01"
        
        # },

        # {
        #     "id" : 3,
        #     "title" : "Practice Python",
        #     "description" : "Solve function problems",
        #     "priority" : "High",
        #     "due_date" : "2026-11-01"
        
        # },

    ]


    return render_template('view_task.html', tasks=tasks)















if __name__ == "__main__":
    app.run(debug=True)

















