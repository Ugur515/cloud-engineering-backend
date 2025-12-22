from dotenv import load_dotenv
load_dotenv()

from app import create_app
from config.config import Config


app = create_app()

if __name__ == "__main__":
    app.run(
        debug=Config.DEBUG,
        host=Config.HOST,
        port=Config.PORT
    )