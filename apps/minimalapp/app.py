from email_validator import EmailNotValidError, validate_email
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

# Adding SECRET_KEY

app.config["SECRET_KEY"] = "7-dRj?'RPwQ6:KEapv$&nvMZMmh"


@app.route(
    "/",
)
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}"


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")

#  permitting GET and POST 


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # get form input by request.form
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # check inputs

        is_valid = True

        if not username:
            flash("Please fill in the Username")
            is_valid = False
        
        if not email:
            flash("Please fiill in the Email")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Please fill in a valid Email")
            is_valid = False

        if not description:
            flash("Please fill in the contact description")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))


        # Send email

        # Redirect to Contact Complete Endpoint

        flash("Thank you for contacting us")
        return redirect(url_for("contact_complete"))

    # if GET, render contact_complete.html    
    return render_template("contact_complete.html")


# get url using url_for function


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=ichiro
    print(url_for("show_name", name="ichiro", page="1"))
    # css styling
    print(url_for("static", filename="style.css"))
