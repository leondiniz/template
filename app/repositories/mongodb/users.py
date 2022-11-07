from app.schemas.users import User
from app.repositories.repository import BaseRepository
from bson.objectid import ObjectId
from typing import Dict


class UserRepository(BaseRepository):
    def __init__(self, db) -> None:
        super().__init__(db)
        self._collection_users = 'users'
        self._users_collection = db[self._collection_users]

    async def create_async(self, user: User) -> User:
        """
        Create a user on mongodb
        Parameters:
        user (dict): user that will be added.
        """
        user_dict = user.dict()

        user = User.from_dict(user_dict)

        await self._users_collection.insert_one(user)

        return user_dict

    async def get_by_code_async(self, code: str) -> User:
        """
        Get a user by code

        Parameters:
        code (string): user code identifier.
        """

        try:
            user = await self._users_collection.find_one(
                {'code': code}
            )
        except Exception:
            return None

        return user

    async def get_by_id_async(self, id: str) -> User:
        """
        Get a user by id
        Parameters:
        code (string): user id identifier.
        """

        user = await self._users_collection.find_one(
            {'_id': ObjectId(id)}
        )

        return user

    async def get_users_async(self):
        """
        Get all users

        Parameters:
        """
        data = []
        users = self._users_collection.find()

        async for file in users:
            data.append(file)
            print(file)

        return data

    async def delete_user_by_id(self, id: str) -> User:
        """
        delete a user by id
        Parameters:
        code (string): user id identifier.
        """

        await self._users_collection.delete_one(
            {'_id': ObjectId(id)}
        )

    async def update_user_by_id(
            self, id: str, item: Dict) -> User:
        """
        delete a user by id
        Parameters:
        code (string): user id identifier.
        """

        await self._users_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': item},   upsert=True)
