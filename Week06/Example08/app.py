from flask import Flask, render_template, request

app = Flask(__name__)  # Flask application object created


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            return f"<h1>Hello {name} </h1><a href='/'>Go Back</a>"
        else:
            return "<h2>Error: The name cannot be empty</h2><a href='/'>Try again</a>"
    return """
    <h2>Enter your name</h2>
    <form method="POST">
    <input type = 'text' name = 'name' placeholder='Enter your name' required>
    <button type = 'submit'>Submit</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
