from app.crud.shared import get_connection
from werkzeug.security import generate_password_hash

### USERS CRUD ###
def create_user(email, password, role):
    password_hash = generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)
    query = "INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (email, password_hash, role))
        conn.commit()
        return cursor.lastrowid

def read_users():
    query = "SELECT * FROM users"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def update_user(user_id, email=None, role=None):
    query = "UPDATE users SET email = COALESCE(?, email), role = COALESCE(?, role), updated_at = CURRENT_TIMESTAMP WHERE user_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (email, role, user_id))
        conn.commit()
        return cursor.rowcount

def delete_user(user_id):
    query = "DELETE FROM users WHERE user_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        conn.commit()
        return cursor.rowcount