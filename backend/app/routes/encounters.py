from flask import Blueprint, request, jsonify
from app.crud.encounters import create_encounter, read_encounters, update_encounter, delete_encounter

encounters_bp = Blueprint("encounters", __name__)

@encounters_bp.route("/", methods=["POST"])
def api_create_encounter():
    data = request.json
    encounter_id = create_encounter(
        data["patient_id"], data["encounter_type"], data["subtype"],
        data["location_id"], data["start_time"], data.get("end_time")
    )
    return jsonify({"encounter_id": encounter_id}), 201

@encounters_bp.route("/", methods=["GET"])
def api_read_encounters():
    encounters = read_encounters()
    return jsonify(encounters)

@encounters_bp.route("/<int:encounter_id>", methods=["PUT"])
def api_update_encounter(encounter_id):
    data = request.json
    updated_count = update_encounter(
        encounter_id,
        patient_id=data.get("patient_id"),
        encounter_type=data.get("encounter_type"),
        subtype=data.get("subtype"),
        location_id=data.get("location_id"),
        start_time=data.get("start_time"),
        end_time=data.get("end_time"),
    )
    return jsonify({"updated": updated_count})

@encounters_bp.route("/<int:encounter_id>", methods=["DELETE"])
def api_delete_encounter(encounter_id):
    deleted_count = delete_encounter(encounter_id)
    return jsonify({"deleted": deleted_count})
