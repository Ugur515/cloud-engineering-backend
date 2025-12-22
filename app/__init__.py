import logging
from flask import Flask 

def create_app():
    app = Flask(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    from .routes import api
    app.register_blueprint(api)

    app.logger.info("Flask App erfolgreich gestartet")
    
    return app