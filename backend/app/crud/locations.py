from app.crud.shared import get_connection


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