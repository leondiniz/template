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

    # JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
    # JWT_AUDIENCE: str = os.getenv('JWT_AUDIENCE')
    # try:
    #     JWT_RSA_KEY: Dict = json.loads(
    #         urlopen(os.getenv('JWT_URL_RSA_KEY')).read())
    # except Exception:
    #     JWT_RSA_KEY: Dict = None

    MONGO_URI: str = os.getenv('MONGO_URI')
    MONGO_DATABASE: str = os.getenv('MONGO_DATABASE')


def get_settings() -> Settings:
    return Settings()
