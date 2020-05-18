from flask import Flask, render_template
# this is nothing but the name of our flask app
app = Flask(__name__)


@app.route("/")
def about():
    return 'hello there this is the'  # python will send this http res


@app.route("/home")
def home():
    return render_template("home.html", name="Priyal")  # pssing templates with jinja

