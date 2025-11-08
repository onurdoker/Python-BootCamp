"""
Jinja2 templates:

1. Variables:
    {{ variables }}                             -> Prints the value of the given variable
    {{ user.name }}                             -> Accesses properties or keys in variables

2. Filters (postfixed to variables):
    {{ "hello" | upper }}                       -> Converts text to uppercase
    {{ 4 | length }}                            -> Gets the length of a string or collection

3. Comments:
    {# This is a comment. #}

4. Control structures:
    {% if user %} ... {% endif %}               -> Conditional rendering
    {% for item in items %} ... {% endfor %}    -> Loop through a sequence

5. Inheritance and inclusions:
    {% extends 'base.html' %}                   -> Inherit from other templates
    {% block content %} ... {% endblock %}      -> Define blocks to override
    {% include 'header.html' %}                 -> Include other templates

6. Macros:
    {% macro input(name, type='text') -%}
        <input type="{{ type }}" name="{{ name }}">
    {%- endmacro %}
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    texts = [
        {
            "title": "What is Flask",
            "content": "Flask is a lightweight Python web framework",
        },
        {
            "title": "I'm learning Jinja2",
            "content": "The templates engine is very useful",
        },
        {
            "title": "Virtual Environment",
            "content": "It is a great tool tTo isolate dependencies",
        },
    ]
    return render_template("index.html", texts=texts)


@app.route("/users")
def users():
    users = [
        {"name": "John", "active": True},
        {"name": "Jack", "active": False},
        {"name": "Tom", "active": True},
    ]
    return render_template("index.html", users=users)


@app.route("/products")
def products():
    categories = [
        {"name": "Electronic", "products": ["Laptop", "Phone", "Tablet"]},
        {"name": "Book", "products": ["Novel", "Poetry", "History"]},
    ]
    return render_template("products.html", categories=categories)


if __name__ == "__main__":
    app.run(debug=True)
