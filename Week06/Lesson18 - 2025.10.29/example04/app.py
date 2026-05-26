from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

USERS_FILE = "users.json"


def load_users():
    # Reads user data from a JSON file. Returns an empty list if the file does not exist or is empty.
    if not os.path.exists(USERS_FILE) or os.path.getsize(USERS_FILE) == 0:
        return []
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            # If the file is empty or contains invalid JSON (JSONDecodeError), it is caught.
            return json.load(f)
    except json.JSONDecodeError:
        # If the JSON is corrupted, display an error message and continue with an empty list.
        print(
            f"WARNING: The file {USERS_FILE} is corrupted or contains invalid JSON. Continuing with an empty list."
        )
        return []


def save_users(users):
    # Writes user data to a JSON file.
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def initialize_users_file():
    # Creates the users.json file with sample data when the application is run for the first time.
    if not os.path.exists(USERS_FILE) or os.path.getsize(USERS_FILE) == 0:
        # We are setting the sample data provided by the user as the default.
        initial_users = [
            {"id": 1, "name": "John Doe", "email": "johndoe@example.com"},
            {"id": 2, "name": "Jack Black", "email": "jackblack@example.com"},
        ]
        save_users(initial_users)
        print(f"The file {USERS_FILE} has been created with sample data.")


# --- API Routes ---


# Main Page
@app.route("/", methods=["GET"])
def home():
    # Lists the general status of the API and available endpoints
    return jsonify(
        {
            "message": "Flask REST API is running! Endpoints for user management:",
            "endpoints": {
                "GET /users": "Lists all users",
                "GET /users/<id>": "Retrieves a specific user",
                "POST /users": "Creates a new user (Required: name, email)",
                "PUT /users/<id>": "Updates the user (Optional: name, email)",
                "DELETE /users/<id>": "Delete user",
            },
        }
    )


# 1. Lists all users
@app.route("/users", methods=["GET"])
def get_users():
    # Lists all users
    users = load_users()
    # For debugging: If an empty list is returned, print information to the console
    if not users:
        print(
            "DEBUG INFO: The '/users' endpoint returned an empty list. Ensure that the 'users.json' file is in the correct location, is not empty, and contains valid JSON."
        )
    return jsonify(users), 200


# 2. Retrieves a specific user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # Retrieves the user with a specific ID.
    users = load_users()
    # Find the user in a single line using next(), returning None if not found
    user = next((u for u in users if u["id"] == user_id), None)

    if user:
        return jsonify(user), 200
    else:
        # Returns 404 Not Found if the user is not found
        return jsonify({"error": f"User with ID {user_id} not found"}), 404


# 3. Add new user
@app.route("/users", methods=["POST"])
def create_user():
    # Create a new user
    # silent=True ensures that if the request is not in JSON format, the error is silently absorbed and None is returned.
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Valid JSON data is required."}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "The 'name' and 'email' fields are required."}), 400

    users = load_users()

    # ID generation: Find the current maximum ID and increment it by 1.
    # With default=0, it starts from 1 in case of an empty list.
    new_id = max([u.get("id", 0) for u in users], default=0) + 1

    new_user = {"id": new_id, "name": name, "email": email}
    users.append(new_user)
    save_users(users)

    # Return the newly created user with a 201 Created status code
    return jsonify(new_user), 201


# 4. Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    # Updates the user with a specific ID.
    users = load_users()
    # Finding the user's index using next() and enumerate()
    user_index = next((i for i, u in enumerate(users) if u["id"] == user_id), None)

    if user_index is None:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Valid JSON data is required."}), 400

    updated = False

    # Update only the fields that were sent
    if "name" in data and data["name"]:  # Also prevent empty strings from being sent
        users[user_index]["name"] = data["name"]
        updated = True
    if "email" in data and data["email"]:
        users[user_index]["email"] = data["email"]
        updated = True

    if updated:
        save_users(users)
        return jsonify(users[user_index]), 200
    else:
        # Return 400 Bad Request if there is no valid update data
        return jsonify({"error": "No valid field (name or email) found to update"}), 400


# 5. Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Deletes the user with a specific ID.
    users = load_users()
    # Finding the user's index using next() and enumerate()
    user_index = next((i for i, u in enumerate(users) if u["id"] == user_id), None)

    if user_index is None:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    # Remove the user from the list using pop()
    deleted_user = users.pop(user_index)
    save_users(users)

    # Return a success message with a 200 OK status code
    return jsonify(
        {"message": f"User ID {user_id} ({deleted_user['name']}) successfully deleted"}
    ), 200


# Start the application
if __name__ == "__main__":
    # Check the users.json file at startup and create it with sample data if necessary.
    initialize_users_file()
    app.run(debug=True, host="0.0.0.0", port=5001)
