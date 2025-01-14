import sqlite3

DB_PATH = "backend/skaldhealth.db"

# Helper function for database connection
def get_connection():
    return sqlite3.connect(DB_PATH)

### USERS CRUD ###
def create_user(email, password_hash, role):
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

# Similar CRUD functions for other tables (e.g., Encounters, Diagnoses, Medications, Locations) can be written following this pattern.

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

def create_location(facility_name, building=None, unit=None, room=None, bed=None):
    query = "INSERT INTO locations (facility_name, building, unit, room, bed) VALUES (?, ?, ?, ?, ?)"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (facility_name, building, unit, room, bed))
        conn.commit()
        return cursor.lastrowid

def read_locations():
    query = "SELECT * FROM locations"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def update_location(location_id, facility_name=None, building=None, unit=None, room=None, bed=None):
    query = """
    UPDATE locations
    SET facility_name = COALESCE(?, facility_name),
        building = COALESCE(?, building),
        unit = COALESCE(?, unit),
        room = COALESCE(?, room),
        bed = COALESCE(?, bed),
        updated_at = CURRENT_TIMESTAMP
    WHERE location_id = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (facility_name, building, unit, room, bed, location_id))
        conn.commit()
        return cursor.rowcount

def delete_location(location_id):
    query = "DELETE FROM locations WHERE location_id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (location_id,))
        conn.commit()
        return cursor.rowcount
