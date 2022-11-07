from app.repositories.mongodb.users import UserRepository as UserRepositorymongodb

from app.services.users import UserService

from typing import Type, Callable
from app.database import get_database_async
from fastapi import Depends
from app.repositories.repository import BaseRepository

from typing import List
from fastapi import Request
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_service(service_type: Type[any]
                ) -> Callable:
    """ get service is responsible for """
    """database connection services.
    """

    if service_type == UserService:
        def _get_user_service(
                plan_repository=Depends(get_repository(
                    UserRepositorymongodb))):
            return service_type(plan_repository)
        return _get_user_service


def get_repository(repo_type: Type[any]
                   ) -> Callable:

    if repo_type == UserRepositorymongodb:

        def __get_repo(db=Depends(get_database_async)
                       ) -> BaseRepository:
            return repo_type(db)

        return __get_repo
