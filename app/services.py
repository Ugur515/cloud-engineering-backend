from . import db
from .models import Item
import logging

def get_items_service():
    try:
        items = Item.query.all()
        return [{"id": i.id, "name": i.name} for i in items]
    except Exception as e:
        logging.exception("Fehler beim Abrufen der Items aus DB")
        raise e

def add_item_service(data):
    try:
        item = Item(name=data["name"])
        db.session.add(item)
        db.session.commit()
        logging.info(f"Item '{data['name']}' in DB gespeichert")
    except Exception as e:
        db.session.rollback()
        logging.exception("Fehler beim Hinzufügen eines Items in DB")
        raise e
