from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')


@app.route("/price")
def price():
    return render_template('price.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


@app.route("/feedbacks")
def feedbacks():
    return render_template('feedbacks.html')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)
