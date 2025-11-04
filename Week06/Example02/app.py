from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)  # Flask application object created
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")  # main page url
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    today = datetime.now().strftime("%d.%m.%Y")
    return render_template("user.html", name=name.capitalize(), today=today)


if __name__ == "__main__":
    app.run(debug=True)
