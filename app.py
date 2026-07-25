from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# ==========================
# Home Page
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Register Page
# ==========================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        print("===== REGISTER =====")
        print("Name:", name)
        print("Email:", email)
        print("Password:", password)

        # Later this will save to database

        return redirect(url_for("login"))

    return render_template("register.html")


# ==========================
# Login Page
# ==========================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        print("===== LOGIN =====")
        print("Email:", email)
        print("Password:", password)

        # Later verify from database

        return redirect(url_for("dashboard"))

    return render_template("login.html")


# ==========================
# Dashboard
# ==========================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ==========================
# Symptoms Page
# ==========================
@app.route("/symptoms", methods=["GET", "POST"])
def symptoms():

    if request.method == "POST":

        age = request.form.get("age")
        gender = request.form.get("gender")

        symptoms = request.form.getlist("symptoms")

        print("===== SYMPTOMS =====")
        print("Age:", age)
        print("Gender:", gender)
        print("Symptoms:", symptoms)

        # Temporary values
        disease = "Flu"
        confidence = 92
        recommendation = "Drink plenty of water, take rest, and consult a doctor if symptoms worsen."

        return render_template(
            "result.html",
            disease=disease,
            confidence=confidence,
            recommendation=recommendation
        )

    return render_template("symptoms.html")


# ==========================
# Result Page
# ==========================
@app.route("/result")
def result():

    return render_template(
        "result.html",
        disease="No Prediction",
        confidence=0,
        recommendation="Please submit your symptoms first."
    )


# ==========================
# History Page
# ==========================
@app.route("/history")
def history():
    return render_template("history.html")


# ==========================
# About Page
# ==========================
@app.route("/about")
def about():
    return render_template("about.html")


# ==========================
# Run Flask
# ==========================
if __name__ == "__main__":
    app.run(debug=True)