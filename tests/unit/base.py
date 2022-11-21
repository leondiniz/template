import asyncpg
import sqlalchemy
from tests.unit.helper import set_envs_for_tests
from tests.unit.database import get_database
from app.schemas.users import User
from tests.unit.settings import get_settings
from app.repositories.mongodb.users import UserRepository
from bson.objectid import ObjectId
from typing import Dict


class BaseTest:

    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        set_envs_for_tests()
        cls.database = get_database()

        cls.users_collection = cls.database.get_collection(
            'users')
        cls.images_collection = cls.database.get_collection(
            'images')
        cls.user = 'admin@teste.com.br'
        cls.settings = get_settings()

    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a call to
        setup_class.
        """
        for collection in cls.database.list_collection_names():
            cls.database.drop_collection(collection)

    def create_user(self, user: dict):

        self.users_collection.insert_one(user)

    def get_user_by_code(self, code: str) -> User:
        """
        get a user by your code, not id
        """

        response = self.users_collection.find_one({"code": code})

        return response

    def get_by_id_async(self, id: str) -> User:
        """
        Get a user by id
        Parameters:
        code (string): user id identifier.
        """

        user = self.users_collection.find_one(
            {'_id': ObjectId(id)}
        )

        return user

    async def get_users_async(self):
        """
        Get all users

        Parameters:
        """
        data = []
        users = self.users_collection.find()

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

        self.users_collection.delete_one(
            {'_id': ObjectId(id)}
        )

    async def update_user_by_id(self, id: str, item: Dict) -> User:
        """
        delete a user by id
        Parameters:
        id (string): user id identifier.
        """

        self.users_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': item},   upsert=True)

    def create_image(self, image: dict):

        self.images_collection.insert_one(image)

    def get_image_user_by_id_async(self, userid: str):
        """
        Get a image by userid
        Parameters:
        userid (string): userid identifier.
        """

        response = self.images_collection.find_one({"userid": userid})

        return response

    async def delete_image_by_id(self, image: Dict):
        """
        delete a user image by id
        Parameters:
        id (string): image id identifier.
        """

        self.images_collection.delete_one(
            image
        )
