from flask import Flask, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

DATA_FILE = "users.json"


# Load users from JSON file
def load_users():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


# Save users to JSON file
def save_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)


users = load_users()


# Home route
@app.route("/")
def home():
    return {
        "message": "Welcome to User Management REST API",
        "status": "API is running successfully"
    }, 200


# API status route
@app.route("/status", methods=["GET"])
def status():
    return {
        "status": "Running",
        "total_users": len(users)
    }, 200


# GET all users
@app.route("/users", methods=["GET"])
def get_users():

    sorted_list = sorted(users, key=lambda x: x["name"])
    
    return jsonify({
        "total_users": len(users),
        "users": users
    }), 200

# GET single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200

    return {"message": "User not found"}, 404

# POST add new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json

    # Input validation
    if not data or "name" not in data or "email" not in data:
        return {"message": "Invalid input"}, 400

    # Duplicate email check (ADD THIS PART HERE ⭐)
    for user in users:
        if user["email"] == data["email"]:
            return {"message": "Email already exists"}, 409

    # Create new user
    new_user = {
        "id": max([user["id"] for user in users], default=0) + 1,
        "name": data["name"],
        "email": data["email"],
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    users.append(new_user)
    save_users(users)

    return {
        "message": "User added successfully",
        "user": new_user
    }, 201

# PUT update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json

    if not data:
        return {"message": "Invalid input"}, 400

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            user["updated_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            save_users(users)

            return {"message": "User updated successfully"}, 200

    return {"message": "User not found"}, 404


# DELETE single user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            save_users(users)

            return {"message": "User deleted successfully"}, 200

    return {"message": "User not found"}, 404


# DELETE all users
@app.route("/users", methods=["DELETE"])
def delete_all_users():
    users.clear()
    save_users(users)

    return {"message": "All users deleted successfully"}, 200


# Search user by name
@app.route("/search", methods=["GET"])
def search_user():
    name = request.args.get("name")

    if not name:
        return {"message": "Please provide name parameter"}, 400

    results = [
        user for user in users
        if name.lower() in user["name"].lower()
    ]

    return jsonify(results), 200


if __name__ == "__main__":
    app.run(debug=True)