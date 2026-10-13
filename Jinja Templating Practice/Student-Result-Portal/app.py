## Create the Flask App

from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/about')
def about():

    return render_template('about.html')


## Flask receives the form by post methods

@app.route('/add_student')
def add_student():


            return render_template('add_student.html')



@app.route('/students', methods=['GET', 'POST'])
def students():

        if request.method == 'POST':
            student_name = request.form['student_name']
            roll_no = request.form['roll_no']
            email = request.form['email']

            dbms = request.form['dbms']
            pdsa = request.form['pdsa']
            sc = request.form['sc']

            

            return f'{render_template('students.html'),}, {student_name}, {roll_no}, {email}'

@app.route('/result')
def  result():
    return render_template('result.html')


app.run(debug=True)





























