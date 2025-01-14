import sqlite3

def initialize_database(db_name, schema_file):
    with sqlite3.connect(db_name) as conn:
        with open(schema_file, 'r') as f:
            conn.executescript(f.read())
        print(f"Database '{db_name}' initialized successfully.")

if __name__ == "__main__":
    initialize_database("skaldhealth.db", "schema.sql")
