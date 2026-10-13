from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/employees")
def employees():
    return render_template("employees.html")


@app.route("/departments")
def departments():
    return render_template("departments.html")


@app.route("/attendance")
def attendance():
    return render_template("attendance.html")


@app.route("/leave")
def leave():
    return render_template("leave.html")


if __name__ == "__main__":
    app.run(debug=True)

