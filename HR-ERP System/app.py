import sqlite3
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

DB_PATH = Path(__file__).resolve().parent/"employee.db"



# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# About Us Page
@app.route("/about")
def about():
    return render_template("about.html")


# Admin Login Page
@app.route("/login")
def login():
    return render_template("login.html")


# Contact Us Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Admin Dashboard
@app.route("/admin_dashboard",methods =["GET","POST"])
def admin_dashboard():
    return render_template("admin_dashboard.html")


@app.route("/admin_addEmployee")
def admin_addEmployee():
    return render_template("admin_addEmployee.html")

@app.route("/admin_showEmployee")
def admin_showEmployee():
    return render_template("admin_showEmployee.html")


@app.route("/admin_searchEmployee")
def admin_searchEmployee():
    return render_template("admin_searchEmployee.html")

# Logout
@app.route("/logout")
def logout():
    return render_template("home.html")


@app.route("/save", methods=['POST'])
def save():

   

    empId = request.form['txtEmpId']
    name = request.form['txtname']
    email = request.form['txtemail']
    mobile = request.form['txtmobile'] 
    designation = request.form['txtdesignation'] 
    salary = request.form['txtsalary']


        ## Establish Databasea connection

    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
    INSERT INTO employee_new (EmpID, name, email, mobile, designation, salary)
    SELECT EmpID, name, email, mobile, designation, salary
    FROM employee
    """)    

    connection.commit()
    connection.close()










    return render_template('admin_registrationSuccess.html')










if __name__ == "__main__":
    app.run(debug=True)

