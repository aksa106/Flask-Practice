import sqlite3
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'Task106'

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
        status = request.form.get('status')


        if not title or not title.strip():
            return "Task title is required", 400

        if priority not in ['High', 'Medium', 'Low']:
            return "Invalid Priority", 400

        if status not in ['Pending', 'In Progress', 'Completed']:
            return "Invalid status", 400

        connection = sqlite3.connect(DB_PATH)

        connection.execute(
            """
            INSERT INTO tasks (title, description, priority, due_date, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, description, priority, due_date, status)
        )

        connection.commit()
        connection.close()
        flash('Task added successfully!', 'success')

        return redirect(url_for('view_task'))

    return render_template('add_task.html')









@app.route('/view_task')
def view_task():

    search = request.args.get('search', '')
    status = request.args.get('status', '')
    sort = request.args.get('sort', '')

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    query = """
        SELECT * FROM tasks
        WHERE title LIKE ?
        AND (? = '' OR status = ?)
    """

    if sort == 'due_asc':
        query += " ORDER BY due_date ASC"

    elif sort == 'due_desc':
        query += " ORDER BY due_date DESC"

    elif sort == 'priority':
        query += """
            ORDER BY
            CASE priority
                WHEN 'High' THEN 1
                WHEN 'Medium' THEN 2
                WHEN 'Low' THEN 3
            END
        """

    cursor = connection.execute(
        query,
        ('%' + search + '%', status, status)
    )

    tasks = cursor.fetchall()
    connection.close()
    flash('Task updated successfully!', 'success')

    return render_template(
        'view_task.html',
        tasks=tasks,
        search=search,
        status=status,
        sort=sort
    )






@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):

    connection = sqlite3.connect(DB_PATH)

    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()
    flash('Task deleted successfully!', 'success')

    return redirect(url_for('view_task'))


@app.route('/update_task/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):

    if request.method == 'POST':

        title = request.form.get('text')
        description = request.form.get('desc')
        priority = request.form.get('priority')
        due_date = request.form.get('date')
        status = request.form.get('status')

        if not title or not title.strip():
            return "Task title is required", 400

        if priority not in ['High', 'Medium', 'Low']:
            return "Invalid priority", 400

        if status not in ['Pending', 'In Progress', 'Completed']:
            return "Invalid status", 400

        connection = sqlite3.connect(DB_PATH)

        connection.execute(
            """
            UPDATE tasks
            SET title = ?,
                description = ?,
                priority = ?,
                due_date = ?,
                status = ?
            WHERE id = ?
            """,
            (title, description, priority, due_date, status, task_id)
        )

        connection.commit()
        connection.close()

        return redirect(url_for('view_task'))

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()
    connection.close()

    if task is None:
        return "Task not found", 404

    return render_template('update_task.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)