import json
import os
import uuid

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret_key_123"

UPLOAD_FOLDER = "./static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def read_users():
    try:
        with open("./data/users.json", "r", encoding="UTF-8") as file:
            content = file.read()
            users = content.strip()

            if not users:
                return []

            return json.loads(users)

    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        print(f"Error reading or parsing JSON file: {error}")
        return []


def write_users(users):
    with open("./data/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)


@app.route("/")
def index():
    users = read_users()
    return render_template("index.html", users=users)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    surname = request.form.get("surname")
    picture = request.files.get("picture")

    users = read_users()
    new_id = max([u["id"] for u in users], default=0) + 1

    file_name = None
    if picture and picture.filename:
        file_extension = picture.filename.rsplit(".", 1)[-1]
        file_name = f"{uuid.uuid4().hex}.{file_extension}"
        picture.save(os.path.join(UPLOAD_FOLDER, file_name))

    users.append({"id": new_id, "name": name, "surname": surname, "picture": file_name})
    write_users(users)
    flash("User added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/delete/<int:user_id>")
def delete(user_id):
    users = read_users()
    users = [u for u in users if u["id"] != user_id]
    write_users(users)
    flash("User deleted successfully.", "success")
    return redirect(url_for("index"))


@app.route("/update/<int:user_id>", methods=["GET", "POST"])
def update(user_id):
    users = read_users()
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        flash("User not found.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        picture = request.files.get("picture")

        # Update user information
        user["name"] = name
        user["surname"] = surname

        # Update if the picture is changed
        if picture and picture.filename:
            file_extension = picture.filename.rsplit(".", 1)[-1]
            file_name = f"{uuid.uuid4().hex}.{file_extension}"
            picture.save(os.path.join(UPLOAD_FOLDER, file_name))
            user["picture"] = file_name

        write_users(users)
        flash("User information updated successfully.", "success")
        return redirect(url_for("index"))

    # GET request - display the update page
    return render_template("update.html", user=user)


@app.route("/user/<int:user_id>")
def user_info(user_id):
    users = read_users()
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        flash("User not found.", "error")
        return redirect(url_for("index"))
    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
