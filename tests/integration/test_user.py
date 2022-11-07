
from tests.integration.base import BaseTest
from tests.integration.helper import generate_jwt_token
import pytest
from httpx import AsyncClient
import json
import requests
import requests_mock
from requests.models import Response
from mock.mock import Mock, patch, call


class TestUser(BaseTest):

    @classmethod
    def setup_class(cls):
        """ Setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        super().setup_class()

    @pytest.mark.asyncio
    async def test_create_user__insert_user_with_no_duplicate__expected_inserted_ok(  # noqa
        self, async_client: AsyncClient
    ):
        # FIXTURE

        url = 'http://127.0.0.1:8000/api/v1/users'

        token = "token_test"
        payload = {
            "code": "4ismongo",
            "name": "4teste",
            "admin": True,
            "created_at": None,
            "active": True,
            "email": "teste@teste.com"
        }

        headers = {"authorization": f"Bearer {token}"}

        # EXERCISE
        with requests_mock.Mocker() as mock_request:
            mock_request.post(url,
                              json=payload,
                              status_code=200
                              )
            response = requests.post(url,
                                     data=json.dumps(payload),
                                     headers=headers
                                     )
        assert response.status_code == 200
        assert response.json() == payload

    @pytest.mark.asyncio
    async def test_create_user__insert_user_duplicate__expected_error_400(  # noqa
        self, async_client: AsyncClient
    ):
        # FIXTURE

        url = 'http://127.0.0.1:8000/api/v1/users'

        token = "token_test"
        payload = {
            "code": "4ismongo",
            "name": "4teste",
            "admin": True,
            "created_at": None,
            "active": True,
            "email": "teste@teste.com"
        }

        headers = {"authorization": f"Bearer {token}"}

        # EXERCISE
        with requests_mock.Mocker() as mock_request:
            mock_request.post(url,
                              text='{"detail": {"type": "invalid_resource", "description": "The requested resource is invalid.", "detail": "The user already exists"}}',
                              status_code=400
                              )
            response = requests.post(url,
                                     data=json.dumps(payload),
                                     headers=headers
                                     )
        assert response.status_code == 400
        assert response.text == '{"detail": {"type": "invalid_resource", "description": "The requested resource is invalid.", "detail": "The user already exists"}}'  # noqa
