from app.crud.shared import get_connection

def create_principal_problem(encounter_id, description):
    query = "INSERT INTO principal_problems (encounter_id, description) VALUES (?, ?)"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (encounter_id, description))
        conn.commit()
        return cursor.lastrowid

def read_principal_problems():
    query = "SELECT * FROM principal_problems"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def update_principal_problem(problem_id, description=None):
    query = """
    UPDATE principal_problems
    SET description = COALESCE(?, description),
        updated_at = CURRENT_TIMESTAMP
    WHERE problem_id = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (description, problem_id))
        conn.commit()
        return cursor.rowcount

def delete_principal_problem(problem_id):
    query = "DELETE FROM principal_problems WHERE problem_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (problem_id,))
        conn.commit()
        return cursor.rowcount