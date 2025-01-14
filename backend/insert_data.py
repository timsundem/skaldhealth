import sqlite3

DB_PATH = "skaldhealth.db"

def insert_sample_data():
    data = [
        # Users
        ("INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)",
         [('admin@skaldhealth.com', 'hashedpassword1', 'admin'),
          ('doctor@skaldhealth.com', 'hashedpassword2', 'clinician'),
          ('nurse@skaldhealth.com', 'hashedpassword3', 'nurse')]),
        
        # Patients
        ("INSERT INTO patients (first_name, last_name, date_of_birth, gender) VALUES (?, ?, ?, ?)",
         [('John', 'Doe', '1980-05-12', 'male'),
          ('Jane', 'Smith', '1992-11-23', 'female')]),
        
        # Locations
        ("INSERT INTO locations (facility_name, building, unit, room, bed) VALUES (?, ?, ?, ?, ?)",
         [('General Hospital', 'A', 'ICU', '101', '1A'),
          ('General Hospital', 'B', 'Ward', '202', '2B')]),
        
        # Encounters
        ("INSERT INTO encounters (patient_id, encounter_type, subtype, location_id, start_time) VALUES (?, ?, ?, ?, ?)",
         [(1, 'inpatient', 'surgery', 1, '2025-01-13 09:00:00'),
          (2, 'outpatient', 'checkup', 2, '2025-01-12 14:30:00')]),
        
        # Diagnoses
        ("INSERT INTO diagnoses (encounter_id, diagnosis_code, description) VALUES (?, ?, ?)",
         [(1, 'I10', 'Essential (primary) hypertension'),
          (2, 'E11.9', 'Type 2 diabetes mellitus without complications')]),
        
        # Medications
        ("INSERT INTO medications (encounter_id, name, dosage, frequency, start_date) VALUES (?, ?, ?, ?, ?)",
         [(1, 'Metformin', '500mg', 'Twice daily', '2025-01-13'),
          (2, 'Lisinopril', '10mg', 'Once daily', '2025-01-12')]),
        
        # Principal Problems
        ("INSERT INTO principal_problems (encounter_id, description) VALUES (?, ?)",
         [(1, 'High blood pressure requiring monitoring'),
          (2, 'Routine diabetes checkup')]),
    ]

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        for query, records in data:
            cursor.executemany(query, records)
        conn.commit()
        print("Sample data inserted successfully.")

if __name__ == "__main__":
    insert_sample_data()
