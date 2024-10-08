from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config
from app.db import init_db

# Create an instance of PyMongo
mongo = PyMongo()

def create_app():
    app = Flask(__name__)  # Create a Flask app instance
    app.config.from_object(Config)  # Load configuration from config.py
    
    init_db(app) 

    with app.app_context():
        from app.routes import profile_bp  # Import routes
        app.register_blueprint(profile_bp)  # Register the profile blueprint

    return app
