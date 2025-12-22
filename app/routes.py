from flask import Blueprint, jsonify, request
from .services import add_item_service, get_items_service
import logging 

api = Blueprint('api', __name__)

@api.route("/items", methods=["GET"])
def get_items():
    try:
        logging.info("GET /items aufgerufen")
        items = get_items_service()
        logging.info(f"{len(items)} Items zurückgegeben")
        return jsonify(items)
    except Exception as e:
        logging.exception("Fehler beim Abrufen der Items")
        return jsonify({"error": "Interner Serverfehler"}), 500

@api.route("/items", methods=["POST"])
def add_item():
    try:
        data = request.json
        logging.info(f"POST /items aufgerufen mit Daten: {data}")
        if not data or "name" not in data:
            logging.warning("POST /items - fehlende 'name'-Angabe")
            return jsonify({"error": "Fehlende 'name'-Angabe"}), 400
        add_item_service(data)
        logging.info(f"Item hinzugefügt: {data['name']}")
        return jsonify({"message": "Item hinzugefügt"}), 201
    except Exception as e:
        logging.exception("Fehler beim Hinzufügen eines Items")
        return jsonify({"error": "Interner Serverfehler"}), 500