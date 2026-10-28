from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'xq2a94cv'

app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_DB'] = 'hr_erp_db'

mysql = MySQL(app)  #This is an object created from class mysql

##-------------------------------------------------








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

    #Database connection
    cur = mysql.connection.cursor()

    #Query specification
    cur.execute('insert into registration(EmpID, empname, email, mobile, Designation, Salary) values(%s, %s, %s, %s, %s, %s)',(empId, name, email, mobile, designation, salary))

    #Transactions saved 
    mysql.connection.commit()

    #Database connection closed
    cur.close()


    return "Employee Registered Successfull "










if __name__ == "__main__":
    app.run(debug=True)

