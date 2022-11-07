from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Database
from app.config.settings import get_settings
import databases
import gridfs
from app.utils import api_errors

_mongo_async = None
_postgresql_async = None


async def get_mongo_async():
    global _mongo_async
    if not _mongo_async:
        _mongo_async = AsyncIOMotorClient(
            get_settings().MONGO_URI, connect=False)
    return _mongo_async


async def get_database_async() -> Database:
    try:
        _mongo = await get_mongo_async()
        return _mongo[get_settings().MONGO_DATABASE]
    except Exception:
        api_errors.raise_error_response(
            api_errors.ErrorResourceInvalid,
            detail="Invalid resource.DataBase disconnected",
        )


async def close_connection_async():
    get_mongo_async().close()
