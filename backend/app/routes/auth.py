from flask import Blueprint, request, jsonify
from app.utils import hash_password, verify_password, generate_token
from app.crud.users import read_users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    users = read_users()  # Fetch users from database
    user = next((u for u in users if u[1] == email), None)

    if not user or not verify_password(user[2], password):
        return jsonify({"message": "Invalid email or password"}), 403

    token = generate_token(user[0], user[3])  # user[0] is ID, user[3] is role
    return jsonify({"message": "Login successful", "token": token}), 200
