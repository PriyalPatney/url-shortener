from flask import Flask, render_template, request, redirect, url_for
# this is nothing but the name of our flask app
app = Flask(__name__)


@app.route("/")
def home():
    # pssing templates with jinja
    return render_template('home.html', name="Priyal")


@app.route("/your_url", methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        # using request info is passed through post req by for
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home')) # or redirect('/home')