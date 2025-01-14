from app.crud.shared import get_connection


def create_medication(encounter_id, name, dosage, frequency, start_date, end_date=None):
    query = "INSERT INTO medications (encounter_id, name, dosage, frequency, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (encounter_id, name, dosage, frequency, start_date, end_date))
        conn.commit()
        return cursor.lastrowid

def read_medications():
    query = "SELECT * FROM medications"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def update_medication(medication_id, name=None, dosage=None, frequency=None, start_date=None, end_date=None):
    query = """
    UPDATE medications
    SET name = COALESCE(?, name),
        dosage = COALESCE(?, dosage),
        frequency = COALESCE(?, frequency),
        start_date = COALESCE(?, start_date),
        end_date = COALESCE(?, end_date),
        updated_at = CURRENT_TIMESTAMP
    WHERE medication_id = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (name, dosage, frequency, start_date, end_date, medication_id))
        conn.commit()
        return cursor.rowcount

def delete_medication(medication_id):
    query = "DELETE FROM medications WHERE medication_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (medication_id,))
        conn.commit()
        return cursor.rowcount