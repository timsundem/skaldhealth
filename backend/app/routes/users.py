from flask import Blueprint, request, jsonify
from app.utils import hash_password
from app.crud.users import create_user, read_users, update_user, delete_user

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["POST"])
def api_create_user():
    data = request.json
    if not data or "email" not in data or "password" not in data or "role" not in data:
        return jsonify({"message": "Email, password, and role are required"}), 400

    password_hash = hash_password(data["password"])
    user_id = create_user(data["email"], password_hash, data["role"])
    return jsonify({"user_id": user_id}), 201

@users_bp.route("/", methods=["GET"])
def api_read_users():
    users = read_users()
    return jsonify(users)
