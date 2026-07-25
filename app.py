from flask import Flask, render_template

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Login Page
@app.route("/login")
def login():
    return render_template("login.html")


# Register Page
@app.route("/register")
def register():
    return render_template("register.html")


# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Symptoms Prediction Page
@app.route("/symptoms")
def symptoms():
    return render_template("symptoms.html")


# Result Page
@app.route("/result")
def result():
    return render_template("result.html")


# History Page
@app.route("/history")
def history():
    return render_template("history.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)