import os 

class Config: 
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"
    HOST = os.getenv("FLASK_HOST", "127.0.0.1")
    PORT= int(os.getenv("FLASK_PORT", 5000))