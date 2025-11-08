from flask import Flask, redirect, render_template, request

app = Flask(__name__)

users = []
user = {}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", False)
        email = request.form.get("email", False)
        if name and email:
            users.append({"name": name, "email": email})
        return redirect("/")

    return render_template("index.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
