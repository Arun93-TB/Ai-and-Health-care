/*=========================================
    AI HEALTH ASSISTANT
    JAVASCRIPT FILE
=========================================*/

document.addEventListener("DOMContentLoaded", function () {

    console.log("AI Health Assistant Loaded Successfully");

});

/*=========================================
    MOBILE MENU
=========================================*/

const menuBtn = document.querySelector(".menu-toggle");
const navMenu = document.querySelector("nav ul");

if (menuBtn) {

    menuBtn.addEventListener("click", () => {

        navMenu.classList.toggle("show");

    });

}

/*=========================================
    PASSWORD SHOW / HIDE
=========================================*/

const passwordFields = document.querySelectorAll("input[type='password']");

passwordFields.forEach(field => {

    const parent = field.parentElement;

    const icon = document.createElement("i");

    icon.className = "fa-solid fa-eye";

    icon.style.cursor = "pointer";

    icon.style.marginRight = "15px";

    parent.appendChild(icon);

    icon.addEventListener("click", () => {

        if (field.type === "password") {

            field.type = "text";

            icon.className = "fa-solid fa-eye-slash";

        }

        else {

            field.type = "password";

            icon.className = "fa-solid fa-eye";

        }

    });

});

/*=========================================
    PASSWORD STRENGTH
=========================================*/

const password = document.getElementById("password");

const fill = document.getElementById("strength-fill");

const text = document.getElementById("strength-text");

if (password) {

password.addEventListener("keyup", function () {

let value = password.value.length;

if (value < 6) {

fill.style.width = "30%";

fill.style.background = "red";

text.innerHTML = "Weak Password";

}

else if (value < 10) {

fill.style.width = "70%";

fill.style.background = "orange";

text.innerHTML = "Medium Password";

}

else {

fill.style.width = "100%";

fill.style.background = "green";

text.innerHTML = "Strong Password";

}

});

}

/*=========================================
    HISTORY SEARCH
=========================================*/

const search = document.getElementById("searchHistory");

if (search) {

search.addEventListener("keyup", function () {

let filter = search.value.toUpperCase();

let table = document.querySelector(".history-table table");

let tr = table.getElementsByTagName("tr");

for (let i = 1; i < tr.length; i++) {

let td = tr[i].getElementsByTagName("td")[1];

if (td) {

let txt = td.textContent || td.innerText;

tr[i].style.display = txt.toUpperCase().indexOf(filter) > -1 ? "" : "none";

}

}

});

}

/*=========================================
    SMOOTH SCROLL
=========================================*/

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

anchor.addEventListener("click", function (e) {

e.preventDefault();

document.querySelector(this.getAttribute("href")).scrollIntoView({

behavior: "smooth"

});

});

});

/*=========================================
    BMI CALCULATOR
=========================================*/

const heightInput = document.getElementById("height");
const weightInput = document.getElementById("weight");
const bmiResult = document.getElementById("bmiResult");

function calculateBMI() {

    if (!heightInput || !weightInput || !bmiResult) return;

    let height = parseFloat(heightInput.value);
    let weight = parseFloat(weightInput.value);

    if (height > 0 && weight > 0) {

        let bmi = weight / Math.pow(height / 100, 2);

        let status = "";

        if (bmi < 18.5) {

            status = "Underweight";

        } else if (bmi < 25) {

            status = "Normal";

        } else if (bmi < 30) {

            status = "Overweight";

        } else {

            status = "Obese";

        }

        bmiResult.innerHTML = `BMI : <strong>${bmi.toFixed(1)}</strong> (${status})`;

    }

}

if (heightInput) {

    heightInput.addEventListener("keyup", calculateBMI);

}

if (weightInput) {

    weightInput.addEventListener("keyup", calculateBMI);

}

/*=========================================
    SYMPTOM COUNTER
=========================================*/

const symptoms = document.querySelectorAll("input[type='checkbox']");
const symptomCount = document.getElementById("symptomCount");

function updateCounter() {

    if (!symptomCount) return;

    let total = 0;

    symptoms.forEach(symptom => {

        if (symptom.checked) {

            total++;

        }

    });

    symptomCount.innerHTML = total;

}

symptoms.forEach(symptom => {

    symptom.addEventListener("change", updateCounter);

});

/*=========================================
    FORM VALIDATION
=========================================*/

const forms = document.querySelectorAll("form");

forms.forEach(form => {

    form.addEventListener("submit", function (e) {

        const required = form.querySelectorAll("[required]");

        let valid = true;

        required.forEach(field => {

            if (field.value.trim() === "") {

                valid = false;

                field.style.border = "2px solid red";

            } else {

                field.style.border = "1px solid #ccc";

            }

        });

        if (!valid) {

            e.preventDefault();

            alert("Please fill all required fields.");

        }

    });

});

/*=========================================
    LOADING BUTTON
=========================================*/

const predictButton = document.getElementById("predictBtn");

if (predictButton) {

    predictButton.addEventListener("click", function () {

        predictButton.innerHTML = '<i class="fa fa-spinner fa-spin"></i> Predicting...';

    });

}

/*=========================================
    SCROLL TO TOP BUTTON
=========================================*/

const topButton = document.createElement("button");

topButton.innerHTML = "↑";

topButton.id = "topButton";

document.body.appendChild(topButton);

topButton.style.position = "fixed";
topButton.style.bottom = "25px";
topButton.style.right = "25px";
topButton.style.display = "none";
topButton.style.width = "50px";
topButton.style.height = "50px";
topButton.style.border = "none";
topButton.style.borderRadius = "50%";
topButton.style.background = "#0b5ed7";
topButton.style.color = "#fff";
topButton.style.cursor = "pointer";
topButton.style.fontSize = "22px";
topButton.style.zIndex = "999";

window.addEventListener("scroll", function () {

    if (window.scrollY > 300) {

        topButton.style.display = "block";

    } else {

        topButton.style.display = "none";

    }

});

topButton.addEventListener("click", function () {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

});

/*=========================================
    SUCCESS NOTIFICATION
=========================================*/

function showNotification(message) {

    const notification = document.createElement("div");

    notification.innerHTML = message;

    notification.style.position = "fixed";
    notification.style.top = "20px";
    notification.style.right = "20px";
    notification.style.background = "#198754";
    notification.style.color = "#fff";
    notification.style.padding = "15px 25px";
    notification.style.borderRadius = "10px";
    notification.style.boxShadow = "0 5px 15px rgba(0,0,0,.2)";
    notification.style.zIndex = "9999";

    document.body.appendChild(notification);

    setTimeout(() => {

        notification.remove();

    }, 3000);

}

/*=========================================
    DASHBOARD COUNTER ANIMATION
=========================================*/

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    const updateCounter = () => {

        const target = +counter.getAttribute("data-target");

        const current = +counter.innerText;

        const increment = target / 100;

        if (current < target) {

            counter.innerText = `${Math.ceil(current + increment)}`;

            setTimeout(updateCounter, 20);

        } else {

            counter.innerText = target;

        }

    };

    updateCounter();

});

/*=========================================
    END OF PART 2
=========================================*/
/*=========================================
    LIVE DATE & TIME
=========================================*/

function updateDateTime() {

    const dateElement = document.getElementById("currentDateTime");

    if (!dateElement) return;

    const now = new Date();

    dateElement.innerHTML = now.toLocaleString();

}

setInterval(updateDateTime,1000);

/*=========================================
    HEALTH TIPS ROTATOR
=========================================*/

const healthTips = [

"💧 Drink at least 2–3 liters of water daily.",

"🥗 Eat more fruits and vegetables.",

"🏃 Exercise for at least 30 minutes every day.",

"😴 Sleep for 7–8 hours every night.",

"🩺 Get regular health checkups.",

"🚭 Avoid smoking and excessive alcohol."

];

let tipIndex = 0;

function rotateHealthTips(){

    const tipBox = document.getElementById("healthTip");

    if(!tipBox) return;

    tipBox.innerHTML = healthTips[tipIndex];

    tipIndex++;

    if(tipIndex >= healthTips.length){

        tipIndex = 0;

    }

}

rotateHealthTips();

setInterval(rotateHealthTips,5000);

/*=========================================
    CONFIRM LOGOUT
=========================================*/

const logoutButton=document.getElementById("logoutBtn");

if(logoutButton){

logoutButton.addEventListener("click",function(e){

if(!confirm("Are you sure you want to logout?")){

e.preventDefault();

}

});

}

/*=========================================
    PRINT RESULT
=========================================*/

const printButton=document.getElementById("printBtn");

if(printButton){

printButton.addEventListener("click",function(){

window.print();

});

}

/*=========================================
    RESET SYMPTOMS FORM
=========================================*/

const resetButton=document.getElementById("resetBtn");

if(resetButton){

resetButton.addEventListener("click",function(){

document.querySelectorAll("input[type='checkbox']").forEach(function(item){

item.checked=false;

});

});

}

/*=========================================
    PAGE LOADER
=========================================*/

window.addEventListener("load",function(){

const loader=document.getElementById("loader");

if(loader){

loader.style.display="none";

}

});

/*=========================================
    END OF SCRIPT.JS
=========================================*/