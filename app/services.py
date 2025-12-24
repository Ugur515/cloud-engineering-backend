from . import db
from .models import Item
import logging
from app.repositories.item_repository_sqlalchemy import ItemRepository

repo = ItemRepository()

def get_items_service():
    try:
        return repo.get_all()
    except Exception:
        logging.exception("Fehler im Service (get_items)")
        raise

def add_item_service(data):
    if "name" not in data or not data["name"]:
        raise ValueError("Name fehlt")

    try:
        repo.add(data["name"])
    except Exception:
        logging.exception("Fehler im Service (add_item)")
        raise
