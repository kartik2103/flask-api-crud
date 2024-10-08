from flask import Blueprint, request, jsonify
from app.models import Profile
from pydantic import ValidationError
from app.db import mongo

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['POST'])
def create_profile():
    try:
        profile_data = Profile(**request.json)  # Validate incoming payload using Pydantic model
        profile_id = mongo.db.profiles.insert_one(profile_data.dict()).inserted_id  # Insert into MongoDB

        return jsonify({
            "message": "Profile created successfully",
            "profile_id": str(profile_id)
        }), 201

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
