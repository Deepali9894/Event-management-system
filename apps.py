from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email and password:
            return redirect("/")

    return render_template("login.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        return redirect("/login")

    return render_template("register.html")


# Events
@app.route("/events")
def events():
    return render_template("events.html")


# Booking
@app.route("/booking")
def booking():
    return render_template("booking.html")


# Confirmation
@app.route("/confirmation", methods=["POST"])
def confirmation():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    event = request.form["event"]
    tickets = request.form["tickets"]

    return render_template(
        "confirmation.html",
        name=name,
        email=email,
        phone=phone,
        event=event,
        tickets=tickets
    )
#generate
@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    event = request.form["event"]
    tickets = request.form["tickets"]

    return render_template(
        "generate.html",
        name=name,
        event=event,
        tickets=tickets
    )

# About
@app.route("/about")
def about():
    return render_template("about.html")


# Contact
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        return "Message sent successfully!"

    return render_template("contact.html")


# Logout
@app.route("/logout")
def logout():
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)