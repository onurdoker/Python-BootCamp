#! First Example
# from flask import Flask
#
# app = Flask(__name__)  # Flask application object created
# app.config["TEMPLATES_AUTO_RELOAD"] = True
#
#
# @app.route("/")  # main page url
# def index():
#     return "Hello World! Welcome to Python Bootcamp Course"
#
#
# @app.route("/about")
# def about():
#     return "You are in about page"
#
#
# # @app.route("/contact/")
# # def contact():
# #     return "You are in contact page"
#
#
# @app.route("/contact/<name>")
# def contact(name):
#     return f"Contact page: {name}"
#
#
# @app.route("/year/<int:year>")
# def year(year):
#     return f"Year: {year}"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


# ! Second Example
# from flask import Flask, render_template
#
# app = Flask(__name__)  # Flask application object created
# app.config["TEMPLATES_AUTO_RELOAD"] = True
#
#
# @app.route("/")  # main page url
# def index():
#     return render_template("index.html")
#
#
# @app.route("/user/<name>")
# def user(name):
#     return render_template("user.html")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


# ! Third Example
# from flask import Flask, render_template
# from datetime import datetime
#
# app = Flask(__name__)  # Flask application object created
# app.config["TEMPLATES_AUTO_RELOAD"] = True
#
#
# @app.route("/")  # main page url
# def index():
#     return render_template("index.html")
#
#
# @app.route("/user/<name>")
# def user(name):
#     today = datetime.now().strftime("%d.%m.%Y")
#     return render_template("user.html", name=name.capitalize(), today=today)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# ! Fourth Example
# from flask import Flask, render_template, url_for, redirect
#
# app = Flask(__name__)  # Flask application object created
# app.config["TEMPLATES_AUTO_RELOAD"] = True
#
# app.secret_key = "qwertasdfg12345"
#
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
#
# @app.route("/about")
# def about():
#     return render_template("about.html")
#
#
# @app.route("/user/<username>")
# def user(username):
#     return render_template("user.html", username=username)
#
#
# @app.route("/main")
# def main():
#     return redirect(url_for("index"))
#
#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"), 404
#
#
# if __name__ == "__main__":
#     app.run(debug=True)  # Open server for developer while 'debug=True'

# ! Fifth Example
# from flask import Flask, render_template, url_for, redirect
#
# app = Flask(__name__)  # Flask application object created
# app.config["TEMPLATES_AUTO_RELOAD"] = True
#
# app.secret_key = "qwertasdfg12345"
#
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
#
# @app.route("/about")
# def about():
#     return render_template("about.html")
#
#
# @app.route("/user/<username>")
# def user(username):
#     return render_template("user.html", username=username)
#
#
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")
#
#
# @app.route("/main")
# def main():
#     return redirect(url_for("index"))
#
#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"), 404
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# ! Fifth Example
# from flask import Flask, render_template, url_for, redirect, request
#
# app = Flask(__name__)  # Flask application object created
# app.config["TEMPLATES_AUTO_RELOAD"] = True
#
# app.secret_key = "qwertasdfg12345"
#
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
#
# @app.route("/about")
# def about():
#     return render_template("about.html")
#
#
# @app.route("/user/<username>")
# def user(username):
#     return render_template("user.html", username=username)
#
#
# @app.route("/contact", methods=["POST", "GET"])
# def contact():
#     if request.method == "POST":
#         name = request.form["name"]
#         message = f"Thank you {name}"
#         return render_template("contact.html", message=message)
#     return render_template("contact.html")
#
#
# @app.route("/main")
# def main():
#     return redirect(url_for("index"))
#
#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"), 404
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# ! Sixth Example
"""
Jinja2 template tags:
{{ ... }} for expressions to print to the page
{% ... %} for statements and variable expressions (if, for, etc.)
{# ... #} for comments
"""
from flask import Flask, render_template

app = Flask(__name__)  # Flask application object created


@app.route("/")
def index():
    texts = [
        {
            "title": "What is Flask?",
            "content": "Flask is a lightweight Python web framework",
        },
        {
            "title": "I learn Jinja2",
            "content": "The template engine is very useful",
        },
        {
            "title": "Virtual Environment",
            "content": "Isolating dependencies is great",
        },
    ]
    return render_template("index2.html", text=texts)


@app.route("/users")
def users():
    users = [
        {"name": "John", "active": True},
        {"name": "Jack", "active": False},
        {"name": "Tom", "active": True},
    ]
    return render_template("users.html", users=users)


@app.route("/products")
def products():
    categories = [
        {"name": "Electronic", "products": ["Laptop", "Phone", "Tablet"]},
        {"name": "Book", "products": ["Novel", "Poetry", "History"]},
    ]
    return render_template("products.html", categories=categories)


if __name__ == "__main__":
    app.run(debug=True)
