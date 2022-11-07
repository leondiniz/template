import os
from dotenv.main import load_dotenv
import app.config.settings as settings
import json
import importlib
from fastapi_jwt import JwtAccessBearer
from app.config.settings import get_settings


_path = os.path.join(os.getcwd(), 'tests', 'integration',
                     'keys', 'private.json')

with open(_path, 'r') as key:
    PRIVATE_KEY = json.load(key)

KID = '62c38dfe2630428bae5898ed2c0a0dae'


def set_envs_for_tests():
    if os.path.exists(os.path.join(os.getcwd(), '.env-tests')):
        os.environ['APP_PATH'] = os.getcwd()
        load_dotenv(os.path.join(os.getcwd(), '.env-tests'), override=True)
        importlib.reload(settings)


def generate_jwt_token(email: str, code: str):

    access_security = JwtAccessBearer(secret_key=str(
        get_settings().JWT_RSA_KEY), auto_error=True)

    token = access_security.create_access_token(
        subject={"code": code, "email": email})
    return token
