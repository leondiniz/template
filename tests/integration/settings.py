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
    _settings.POSTGRESQL_URI = str = os.getenv("POSTGRESQL_URI")
    _settings.AUTH0_MANAGEMENT_URL = str = os.getenv('AUTH0_MANAGEMENT_URL')
    _settings.AUTH0_CLIENTE_ID = str = os.getenv('AUTH0_CLIENTE_ID')
    _settings.AUTH0_CLIENT_SECRET = str = os.getenv('AUTH0_CLIENT_SECRET')
    _settings.AUTH0_GRANT_TYPE = str = os.getenv('AUTH0_GRANT_TYPE')
    _settings.JWT_URL_RSA_KEY = str = os.getenv('JWT_URL_RSA_KEY')
    _settings.JWT_AUDIENCE = str = os.getenv('AUTH0_AUDIENCE')
    return _settings
