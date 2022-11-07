
from tests.unit.base import BaseTest
from tests.unit.helper import generate_jwt_token
import pytest
from httpx import AsyncClient
import json
from bson.objectid import ObjectId


class TestPlan(BaseTest):

    @classmethod
    def setup_class(cls):
        """ Setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        super().setup_class()

    @pytest.mark.asyncio
    async def test_create_user__insert_user__expected_inserted_ok(  # noqa
        self, async_client: AsyncClient
    ):
        # FIXTURE

        payload = {
            "code": "4i",
            "name": "4teste",
            "admin": True,
            "created_at": None,
            "active": True,
            "email": "teste@teste.com"
        }
        self.create_user(payload)

        # EXERCISE

        user = self.get_user_by_code("4i")

        # ASSERTS

        assert user['code'] == '4i'
        assert user['name'] == '4teste'
        assert user['admin'] == True
        assert user['active'] == True
        assert user['email'] == 'teste@teste.com'

    @pytest.mark.asyncio
    async def test_update_user__update_user_with_dict__expected_update_ok(  # noqa
        self, async_client: AsyncClient
    ):
        # FIXTURE

        payload = {
            "code": "4i",
            "name": "4teste",
            "admin": True,
            "created_at": None,
            "active": True,
            "email": "teste@teste.com"
        }

        self.create_user(payload)

        payload_user = {
            "code": "4i",
            "name": "4upload",
            "admin": True,
            "created_at": None,
            "active": True,
            "email": "upload@teste.com"
        }

        # EXERCISE

        user = self.get_user_by_code("4i")

        await self.update_user_by_id(str(user["_id"]), payload_user)
        user = self.get_user_by_code("4i")
        # ASSERTS

        assert user['code'] == payload_user['code']
        assert user['name'] == payload_user['name']
        assert user['admin'] == payload_user['admin']
        assert user['active'] == payload_user['active']
        assert user['email'] == payload_user['email']

    @pytest.mark.asyncio
    async def test_delete_user__delete_user_with_dict__expected_delete_ok(  # noqa
        self, async_client: AsyncClient
    ):
        # FIXTURE

        payload = {
            "code": "4i",
            "name": "4teste",
            "admin": True,
            "created_at": None,
            "active": True,
            "email": "teste@teste.com"
        }

        self.create_user(payload)

        # EXERCISE

        user = self.get_user_by_code("4i")

        await self.delete_user_by_id(str(user["_id"]))
        user = self.get_by_id_async(str(user["_id"]))
        # ASSERTS

        assert user == None
