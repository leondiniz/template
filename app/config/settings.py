import json
import os
from typing import Dict
from urllib.request import urlopen
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """ Configurações globais """

    API_V1: str = "/api/v1"

    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
    JWT_AUDIENCE: str = os.getenv('JWT_AUDIENCE')
    try:
        JWT_RSA_KEY: Dict = json.loads(
            urlopen(os.getenv('JWT_URL_RSA_KEY')).read())
    except Exception:
        JWT_RSA_KEY: Dict = None

    MONGO_URI: str = os.getenv('MONGO_URI')
    MONGO_DATABASE: str = os.getenv('MONGO_DATABASE')

    # Postgres settings
    POSTGRES_HOST: str = os.getenv("host")
    POSTGRES_USER: str = os.getenv("user")
    POSTGRES_PASSWORD: str = os.getenv("password")
    POSTGRES_DATABASE: str = os.getenv("dbname")
    POSTGRES_PORT: str = os.getenv("port")
    POSTGRESQL_URI: str = os.getenv("POSTGRESQL_URI")
    AUTH0_MANAGEMENT_URL: str = os.getenv('AUTH0_MANAGEMENT_URL')
    AUTH0_CLIENTE_ID: str = os.getenv('AUTH0_CLIENTE_ID')
    AUTH0_CLIENT_SECRET: str = os.getenv('AUTH0_CLIENT_SECRET')
    AUTH0_AUDIENCE: str = os.getenv('AUTH0_AUDIENCE')
    AUTH0_GRANT_TYPE: str = os.getenv('AUTH0_GRANT_TYPE')
    JWT_ISSUER: str = os.getenv('JWT_ISSUER')
    JWT_URL_RSA_KEY = os.getenv('JWT_URL_RSA_KEY')
    CELERY_BROKEN_URL = os.getenv("CELERY_BROKEN_URL")
    CELERY_RESULT_URL = os.getenv("CELERY_RESULT_URL")


def get_settings() -> Settings:
    return Settings()
