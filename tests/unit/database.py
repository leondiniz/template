from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from pymongo.database import Database
import databases
from tests.integration.settings import get_settings

_mongo_async = None
_mongo = None


def get_mongo():
    global _mongo
    if not _mongo:
        _mongo = MongoClient(
            get_settings().MONGO_URI, connect=False,)
    return _mongo


def get_database() -> Database:
    return get_mongo()[get_settings().MONGO_DATABASE]


def close_connection():
    get_mongo().close()


async def get_mongo_async():
    global _mongo_async
    if not _mongo_async:
        _mongo_async = AsyncIOMotorClient(
            get_settings().MONGO_URI, connect=False)
    return _mongo_async


async def get_database_async() -> Database:
    _mongo = await get_mongo_async()
    return _mongo[get_settings().MONGO_DATABASE]


def close_connection_async():
    get_mongo_async().close()


async def get_postgresql_async():
    global _postgresql_async
    if not _postgresql_async:
        _postgresql_async = databases.Database(get_settings().POSTGRESQL_URI)
    return _postgresql_async


async def get_postgresql_database_async() -> Database:
    _postgresql = await get_postgresql_async()
    await _postgresql.connect()
    return _postgresql


def close_postgresql_connection_async():
    get_postgresql_async().close()
