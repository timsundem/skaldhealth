from flask import Flask, send_from_directory
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key"  # Used for JWT and other secrets


    # Enable CORS
    CORS(app)

    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.users import users_bp
    from app.routes.patients import patients_bp
    from app.routes.encounters import encounters_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(patients_bp, url_prefix="/patients")
    app.register_blueprint(encounters_bp, url_prefix="/encounters")

    # Default route
    @app.route("/")
    def index():
        return send_from_directory("static", "index.html")

    return app
