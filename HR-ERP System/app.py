from flask import Flask, render_template

app = Flask(__name__)


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



if __name__ == "__main__":
    app.run(debug=True)

