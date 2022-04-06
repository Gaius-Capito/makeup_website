from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/price")
def price():
    return render_template('price.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
