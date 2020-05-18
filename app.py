from flask import Flask, render_template, request
# this is nothing but the name of our flask app
app = Flask(__name__)


@app.route("/")
def about():
    return 'hello there this is the'  # python will send this http res


@app.route("/home")
def home():
    return render_template('home.html', name="Priyal")  # pssing templates with jinja


@app.route("/your_url")
def your_url():
    return render_template('your_url.html', code=request.args['code']) #using request info is passed through post req by form