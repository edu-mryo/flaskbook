from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


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
