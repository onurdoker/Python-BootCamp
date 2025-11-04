from flask import Flask

app = Flask(__name__)  # Flask application object created
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")  # main page url
def index():
    return "Hello World! Welcome to Python Bootcamp Course"


@app.route("/about")
def about():
    return "You are in about page"


@app.route("/contact/<name>")
def contact(name):
    return f"Contact page: {name}"


@app.route("/year/<int:year>")
def year(year):
    return f"Year: {year}"


if __name__ == "__main__":
    app.run(debug=True)
