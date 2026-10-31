
import sqlite3
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database path: tasks.db inside the project folder
DB_PATH = Path(__file__).resolve().parent / "tasks.db"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('text')
        description = request.form.get('desc')
        priority = request.form.get('priority')
        due_date = request.form.get('date')

        connection = sqlite3.connect(DB_PATH)

        connection.execute(
            """
            INSERT INTO tasks (title, description, priority, due_date)
            VALUES (?, ?, ?, ?)
            """,
            (title, description, priority, due_date)
        )

        connection.commit()
        connection.close()

        return redirect(url_for('view_task'))

    return render_template('add_task.html')


@app.route('/view_task')
def view_task():
    connection = sqlite3.connect(DB_PATH)

    connection.row_factory = sqlite3.Row

    cursor = connection.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    connection.close()

    return render_template('view_task.html', tasks=tasks)


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):

    connection = sqlite3.connect(DB_PATH)

    connection.execute(
        "Delete from tasks where id = ?", (task_id,)
    )


    connection.commit()
    connection.close()
    return redirect(url_for('view_task'))





@app.route('/update_task/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):

    if request.method == 'POST':

        title = request.form.get('text')
        description = request.form.get('desc')
        priority = request.form.get('priority')
        due_date = request.form.get('date')

        connection = sqlite3.connect(DB_PATH)

        connection.execute(
            """
            UPDATE tasks
            SET title = ?, description = ?, priority = ?, due_date = ?
            WHERE id = ?
            """,
            (title, description, priority, due_date, task_id)
        )

        connection.commit()
        connection.close()

        return redirect(url_for('view_task'))

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    )

    task = cursor.fetchone()
    connection.close()

    if task is None:
        return "Task not found", 404

    return render_template('update_task.html', task=task)




if __name__ == '__main__':
    app.run(debug=True)

