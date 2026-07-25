from flask import Flask, render_template, request, redirect, url_for
from database import get_connection
from werkzeug.security import generate_password_hash
from model.predict import predict_disease


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
        phone = request.form.get("phone")
        age = request.form.get("age")
        gender = request.form.get("gender")

        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")


        if password != confirm_password:
            return "Passwords do not match"


        hashed_password = generate_password_hash(password)


        print("========== REGISTER ==========")
        print(name)
        print(email)
        print(phone)
        print(age)
        print(gender)
        print("==============================")


        # Database connection later


        return redirect(url_for("login"))


    return render_template("register.html")



# ==========================
# Login Page
# ==========================
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method=="POST":

        email=request.form.get("email")
        password=request.form.get("password")


        print("LOGIN")
        print(email)


        return redirect(url_for("dashboard"))


    return render_template("login.html")



# ==========================
# Dashboard
# ==========================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



# ==========================
# AI Prediction
# ==========================
@app.route("/symptoms", methods=["GET","POST"])
def symptoms():


    if request.method=="POST":


        name=request.form.get("name")
        age=request.form.get("age")
        gender=request.form.get("gender")


        fever = 1 if request.form.get("fever")=="Yes" else 0
        cough = 1 if request.form.get("cough")=="Yes" else 0
        headache = 1 if request.form.get("headache")=="Yes" else 0
        fatigue = 1 if request.form.get("fatigue")=="Yes" else 0
        body_pain = 1 if request.form.get("body_pain")=="Yes" else 0
        vomiting = 1 if request.form.get("vomiting")=="Yes" else 0
        breathing = 1 if request.form.get("breathing")=="Yes" else 0



        # Machine Learning Prediction

        disease, confidence = predict_disease(
            fever,
            cough,
            headache,
            fatigue,
            body_pain,
            vomiting,
            breathing
        )



        # Risk

        if confidence >= 90:
            risk="High"

        elif confidence >=70:
            risk="Medium"

        else:
            risk="Low"



        # Store Prediction

        connection=get_connection()


        if connection:

            cursor=connection.cursor()


            sql="""

            INSERT INTO predictions
            (patient_name, age, gender, disease, confidence)

            VALUES(%s,%s,%s,%s,%s)

            """


            values=(
                name,
                age,
                gender,
                disease,
                confidence
            )


            cursor.execute(sql,values)

            connection.commit()

            cursor.close()

            connection.close()



        recommendations=[

            "Drink plenty of water",
            "Take proper rest",
            "Maintain healthy food habits",
            "Consult doctor if symptoms increase"

        ]



        diet=[

            "Fresh fruits",
            "Vegetables",
            "Protein rich foods",
            "Warm soup",
            "Enough fluids"

        ]



        exercises=[

            "Walking",
            "Yoga",
            "Breathing exercise",
            "Stretching"

        ]



        return render_template(

            "result.html",

            disease=disease,

            confidence=confidence,

            risk=risk,

            recommendations=recommendations,

            diet=diet,

            exercises=exercises

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

        risk="Low",

        recommendations=[],

        diet=[],

        exercises=[]

    )



# ==========================
# History
# ==========================
@app.route("/history")
def history():

    return render_template("history.html")



# ==========================
# About
# ==========================
@app.route("/about")
def about():

    return render_template("about.html")



# ==========================
# Run
# ==========================
if __name__=="__main__":

    app.run(debug=True)