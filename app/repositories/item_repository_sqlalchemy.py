from app import db
from app.models import Item
import logging

class ItemRepository :

    def get_all(self):
        items = Item.query.all()
        return [{"id": i.id, "name": i.name} for i in items]
    
    def add(self, name: str):
        item = Item(name=name)
        db.session.add(item)
        db.session.commit()
        logging.info(f"Item '{name}' gespeichert")
 