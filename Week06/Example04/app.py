from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)  # Flask application object created
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/main")
def main():
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
