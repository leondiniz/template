from app.repositories.mongodb.users import UserRepository

from typing import Dict
from app.utils import api_errors


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def insert_user(
        self,
        user: Dict
    ):

        user_data = await self.find_user_by_code(user.code)

        if user_data:
            api_errors.raise_error_response(
                api_errors.ErrorResourceInvalid,
                detail="The user already exists",
            )

        user_data = await self._user_repository.create_async(
            user)
        return self.db_to_dict(user_data)

    async def find_user_by_code(self, code: str) -> None:
        """
        Get a user by code

        Parameters:
        code (string): user code identifier.
        """

        user = await self._user_repository.get_by_code_async(code)

        return user

    async def find_user_by_id(self, id: str) -> None:
        """
        Get a user by id
        Parameters:
        code (string): user id identifier.
        """
        try:
            user = await self._user_repository.get_by_id_async(id)

            if user is None:
                api_errors.raise_error_response(
                    api_errors.ErrorResourceInvalid,
                    detail="The user not found",
                )

        except Exception:
            api_errors.raise_error_response(
                api_errors.ErrorResourceInvalid,
                detail="The user not found",
            )

        return user

    async def get_users(self):
        """
        Get users list
        Parameters:
        code (string): user id identifier.
        """

        contracts = await self._user_repository.get_users_async()
        data = []
        for file in contracts:
            self.db_to_dict(file)
            data.append(file)

        return data

    async def delete_user_by_id(self, id: str):
        """
        delete a user by id
        Parameters:
        id (string): user id identifier.
        """
        user = await self.find_user_by_id(id)

        if user is None:
            api_errors.raise_error_response(
                api_errors.ErrorResourceInvalid,
                detail="The user not found",
            )

        await self._user_repository.delete_user_by_id(id)

    async def update_user_by_id(self, id: str, item: dict):
        """
        update a user by id
        Parameters:
        id (string): user id identifier.
        """
        user = await self.find_user_by_id(id)

        if user is None:
            api_errors.raise_error_response(
                api_errors.ErrorResourceInvalid,
                detail="The user not found",
            )

        for key, value in item.items():
            print(key, value)
            user[key] = value

        await self._user_repository.update_user_by_id(id, user)

    def db_to_dict(self, user_data: Dict):
        data = {}
        for key, value in user_data.items():
            data[key] = value
        data["_id"] = str(data['_id'])

        return data
