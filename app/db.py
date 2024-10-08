from flask_pymongo import PyMongo
from flask import current_app

# Create a PyMongo instance
mongo = PyMongo()

def init_db(app):
    mongo.init_app(app)  # Initialize the PyMongo instance with the Flask app
