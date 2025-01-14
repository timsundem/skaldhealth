from flask import Flask, request, jsonify
from crud import (
    create_user, read_users, update_user, delete_user,
    create_patient, read_patients, update_patient, delete_patient,
    create_encounter, read_encounters, update_encounter, delete_encounter
)

app = Flask(__name__)

# Users APIs
@app.route('/users', methods=['POST'])
def api_create_user():
    data = request.json
    user_id = create_user(data['email'], data['password_hash'], data['role'])
    return jsonify({"user_id": user_id}), 201

@app.route('/users', methods=['GET'])
def api_read_users():
    users = read_users()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['PUT'])
def api_update_user(user_id):
    data = request.json
    updated_count = update_user(
        user_id,
        email=data.get('email'),
        role=data.get('role')
    )
    return jsonify({"updated": updated_count})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    deleted_count = delete_user(user_id)
    return jsonify({"deleted": deleted_count})

# Patients APIs
@app.route('/patients', methods=['POST'])
def api_create_patient():
    data = request.json
    patient_id = create_patient(
        data['first_name'], data['last_name'], data['date_of_birth'], data['gender']
    )
    return jsonify({"patient_id": patient_id}), 201

@app.route('/patients', methods=['GET'])
def api_read_patients():
    patients = read_patients()
    return jsonify(patients)

@app.route('/patients/<int:patient_id>', methods=['PUT'])
def api_update_patient(patient_id):
    data = request.json
    updated_count = update_patient(
        patient_id,
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        gender=data.get('gender')
    )
    return jsonify({"updated": updated_count})

@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def api_delete_patient(patient_id):
    deleted_count = delete_patient(patient_id)
    return jsonify({"deleted": deleted_count})

# Encounters APIs
@app.route('/encounters', methods=['POST'])
def api_create_encounter():
    data = request.json
    encounter_id = create_encounter(
        data['patient_id'], data['encounter_type'], data['subtype'],
        data['location_id'], data['start_time'], data.get('end_time')
    )
    return jsonify({"encounter_id": encounter_id}), 201

@app.route('/encounters', methods=['GET'])
def api_read_encounters():
    encounters = read_encounters()
    return jsonify(encounters)

@app.route('/encounters/<int:encounter_id>', methods=['PUT'])
def api_update_encounter(encounter_id):
    data = request.json
    updated_count = update_encounter(
        encounter_id,
        patient_id=data.get('patient_id'),
        encounter_type=data.get('encounter_type'),
        subtype=data.get('subtype'),
        location_id=data.get('location_id'),
        start_time=data.get('start_time'),
        end_time=data.get('end_time')
    )
    return jsonify({"updated": updated_count})

@app.route('/encounters/<int:encounter_id>', methods=['DELETE'])
def api_delete_encounter(encounter_id):
    deleted_count = delete_encounter(encounter_id)
    return jsonify({"deleted": deleted_count})

if __name__ == '__main__':
    app.run(debug=True)
