from flask import Blueprint, request, jsonify
from app.crud.patients import create_patient, read_patients, update_patient, delete_patient

patients_bp = Blueprint("patients", __name__)

@patients_bp.route("/", methods=["POST"])
def api_create_patient():
    data = request.json
    patient_id = create_patient(
        data["first_name"], data["last_name"], data["date_of_birth"], data["gender"]
    )
    return jsonify({"patient_id": patient_id}), 201

@patients_bp.route("/", methods=["GET"])
def api_read_patients():
    patients = read_patients()
    return jsonify(patients)

@patients_bp.route("/<int:patient_id>", methods=["PUT"])
def api_update_patient(patient_id):
    data = request.json
    updated_count = update_patient(
        patient_id,
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        gender=data.get("gender"),
    )
    return jsonify({"updated": updated_count})

@patients_bp.route("/<int:patient_id>", methods=["DELETE"])
def api_delete_patient(patient_id):
    deleted_count = delete_patient(patient_id)
    return jsonify({"deleted": deleted_count})
