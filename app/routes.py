from Flask import Blueprint, jsonify, request
from .services import add_item_service, get_item_service

api = Blueprint('api', __name__)

@api.route("/items", methodes=["GET"])
def get_items():
    return jsonify(get_item_service())

@api.route("/items", methodes=["POST"])
def add_item():
    data = request.json
    if not data or "name" not in data: 
        return jsonify({"error": "Fehlende 'name'-Angabe"}), 400
    add_item_service(data)
    return jsonify({"message": "Item hinzugefügt"}), 201
