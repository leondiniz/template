import os
from dotenv.main import load_dotenv
import app.config.settings as settings
import json
import importlib
from fastapi_jwt import JwtAccessBearer
from app.config.settings import get_settings
from jose import jwt
from typing import Dict, List

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


def generate_jwt_token(user_email: str, scopes: List[str] = []):

    payload = {
        "https://dev-nzseols2.com/email": "lediz1@gmail.com",
        "iss": "https://dev-nzseols2.us.auth0.com/",
        "sub": "auth0|6310b4d9290855877226e3a3",
        "aud": "template",
        "iat": 1662418489,
        "exp": 1662504889,
        "azp": "FVjzOmoM02QG7mqxCjR70FvUbz7x6kn9",
        "gty": "password",
        "permissions": [
            "create:users",
            "read:users"
        ]
    }

    token = jwt.encode(payload, PRIVATE_KEY,
                       algorithm=jwt.ALGORITHMS.RS256,
                       headers={
                           "alg": "RS256",
                           "typ": "JWT",
                           "kid": "1uwCWcOJE5Qzgt7KFaw_f"
                       }
                       )

    return token
