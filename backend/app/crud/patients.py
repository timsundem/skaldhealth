from app.crud.shared import get_connection

### PATIENTS CRUD ###
def create_patient(first_name, last_name, date_of_birth, gender):
    query = "INSERT INTO patients (first_name, last_name, date_of_birth, gender) VALUES (?, ?, ?, ?)"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (first_name, last_name, date_of_birth, gender))
        conn.commit()
        return cursor.lastrowid

def read_patients():
    query = "SELECT * FROM patients"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def update_patient(patient_id, first_name=None, last_name=None, gender=None):
    query = """
    UPDATE patients
    SET first_name = COALESCE(?, first_name),
        last_name = COALESCE(?, last_name),
        gender = COALESCE(?, gender),
        updated_at = CURRENT_TIMESTAMP
    WHERE patient_id = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (first_name, last_name, gender, patient_id))
        conn.commit()
        return cursor.rowcount

def delete_patient(patient_id):
    query = "DELETE FROM patients WHERE patient_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (patient_id,))
        conn.commit()
        return cursor.rowcount