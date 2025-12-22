from flask import Blueprint, jsonify, request
from .services import add_item_service, get_items_service

api = Blueprint('api', __name__)

@api.route("/items", methods=["GET"])
def get_items():
    return jsonify(get_items_service())

@api.route("/items", methods=["POST"])
def add_item():
    data = request.json
    if not data or "name" not in data: 
        return jsonify({"error": "Fehlende 'name'-Angabe"}), 400
    add_item_service(data)
    return jsonify({"message": "Item hinzugefügt"}), 201
