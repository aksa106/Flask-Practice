
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


if __name__ == '__main__':
    app.run(debug=True)

