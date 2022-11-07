import os
import json
from dotenv import load_dotenv
from urllib.request import urlopen
from app.config.settings import Settings


def get_settings() -> Settings:
    if os.path.exists(os.path.join(os.getcwd(), '.env-tests')):
        os.environ['APP_PATH'] = os.getcwd()
        load_dotenv(os.path.join(os.getcwd(), '.env-tests'), override=True)

    _settings = Settings()

    _settings.API_V1 = "/api/v1"

    _settings.MONGO_URI = os.getenv('MONGO_URI')
    _settings.MONGO_DATABASE = os.getenv('MONGO_DATABASE')
    # Postgres settings
    _settings.POSTGRES_HOST = str = os.getenv("host")
    _settings.POSTGRES_USER = str = os.getenv("user")
    _settings.POSTGRES_PASSWORD = str = os.getenv("password")
    _settings.POSTGRES_DATABASE = str = os.getenv("dbname")
    _settings.POSTGRES_PORT = str = os.getenv("port")
    _settings.POSTGRESQL_URI = str = os.getenv("POSTGRESQL_URI")

    return _settings
