from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

SECRET_KEY = "your_secret_key"  # Replace with your actual secret key

def hash_password(password):
    return generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)

def verify_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def generate_token(user_id, role):
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
