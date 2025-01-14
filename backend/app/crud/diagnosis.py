from app.crud.shared import get_connection


def create_diagnosis(encounter_id, diagnosis_code, description):
    query = "INSERT INTO diagnoses (encounter_id, diagnosis_code, description) VALUES (?, ?, ?)"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (encounter_id, diagnosis_code, description))
        conn.commit()
        return cursor.lastrowid

def read_diagnoses():
    query = "SELECT * FROM diagnoses"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def update_diagnosis(diagnosis_id, diagnosis_code=None, description=None):
    query = """
    UPDATE diagnoses
    SET diagnosis_code = COALESCE(?, diagnosis_code),
        description = COALESCE(?, description),
        updated_at = CURRENT_TIMESTAMP
    WHERE diagnosis_id = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (diagnosis_code, description, diagnosis_id))
        conn.commit()
        return cursor.rowcount

def delete_diagnosis(diagnosis_id):
    query = "DELETE FROM diagnoses WHERE diagnosis_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (diagnosis_id,))
        conn.commit()
        return cursor.rowcount