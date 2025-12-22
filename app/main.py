from dotenv import load_dotenv
load_dotenv()

import logging 
from logging.handlers import RotatingFileHandler

from app import create_app
from config.config import Config
from flask import jsonify


#Logging konfigurieren 
logging.basicConfig(
    level=logging.DEBUG, #Minimal-Level für die Konsole
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

#Rotierende Log-Datei(max. 5MB pro Datei, 3 Backup-Dateien)
file_handler = RotatingFileHandler('app.log', maxBytes=5*1024*1024, backupCount=3)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s'))

#Handler zum Root-logger hinzufügen
logging.getLogger().addHandler(file_handler) 

logging.debug("Das ist ein Debug-Log")
logging.info("Server gestartet auf Port 5000")
logging.warning("Etwas könnte schiefgehen")
logging.error("Ein Fehler ist aufgetreten")
logging.critical("Schwerwiegender Fehler, Abbruch nötig")

#Flask-App erstellen 
app = create_app()

#Globales Fehlerhandling
@app.errorhandler(Exception)
def handle_exception(e):
    logging.exception("Unerwarteter Fehler:")
    response = {"error": "Interner Serverfehler", "message": str(e)}
    return jsonify(response), 500

@app.errorhandler(404)
def not_found(e):
    logging.warning(f"404 Fehler: {e}")
    return jsonify({"error": "Nicht gefunden"}), 404

#App Starten
if __name__ == "__main__":
    app.run(
        debug=Config.DEBUG,
        host=Config.HOST,
        port=Config.PORT
    )