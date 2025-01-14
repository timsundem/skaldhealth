from app.crud.shared import get_connection


### Example for Encounters ###
def create_encounter(patient_id, encounter_type, subtype, location_id, start_time):
    query = "INSERT INTO encounters (patient_id, encounter_type, subtype, location_id, start_time) VALUES (?, ?, ?, ?, ?)"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (patient_id, encounter_type, subtype, location_id, start_time))
        conn.commit()
        return cursor.lastrowid

def read_encounters():
    query = "SELECT * FROM encounters"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
def read_encounter_by_id(encounter_id):
    query = "SELECT * FROM encounters WHERE encounter_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (encounter_id,))
        return cursor.fetchone()

def update_encounter(encounter_id, patient_id=None, encounter_type=None, subtype=None, location_id=None, start_time=None, end_time=None):
    query = """
    UPDATE encounters
    SET patient_id = COALESCE(?, patient_id),
        encounter_type = COALESCE(?, encounter_type),
        subtype = COALESCE(?, subtype),
        location_id = COALESCE(?, location_id),
        start_time = COALESCE(?, start_time),
        end_time = COALESCE(?, end_time),
        updated_at = CURRENT_TIMESTAMP
    WHERE encounter_id = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (patient_id, encounter_type, subtype, location_id, start_time, end_time, encounter_id))
        conn.commit()
        return cursor.rowcount

def delete_encounter(encounter_id):
    query = "DELETE FROM encounters WHERE encounter_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (encounter_id,))
        conn.commit()
        return cursor.rowcount