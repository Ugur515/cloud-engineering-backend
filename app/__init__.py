import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.config.Config")

    db.init_app(app)

    
    from app.routes import api
    app.register_blueprint(api)

    app.logger.info("Flask App erfolgreich gestartet")

    with app.app_context():
        db.create_all()  # Tabellen erstellen, falls nicht vorhanden

    return app
