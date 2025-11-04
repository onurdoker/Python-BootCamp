"""
Jinja2 templates tags:
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
            "content": "The templates engine is very useful",
        },
        {
            "title": "Virtual Environment",
            "content": "Isolating dependencies is great",
        },
    ]
    return render_template("index.html", text=texts)


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
