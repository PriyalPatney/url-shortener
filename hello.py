from flask import Flask
# this is nothing but the name of our flask app
app = Flask(__name__)

@app.route("/")
def home():
    return 'hello there this is the end' #python will automaticly send it as http response string