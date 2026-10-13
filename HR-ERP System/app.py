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


if __name__ == "__main__":
    app.run(debug=True)