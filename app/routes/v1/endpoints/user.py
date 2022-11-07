
from app.services.users import UserService
from fastapi.params import Depends
from fastapi import APIRouter
from app.dependencies import get_service
from app.schemas.users import User, UserList


router = APIRouter()


@router.post("")
async def create_user(
        user: User,
        service: UserService = Depends(
            get_service(UserService)),
) -> User:
    user = await service.insert_user(user)
    return user


@router.get("/{id}")
async def get_user(
    id=str,
    service: UserService = Depends(
        get_service(UserService)),
):
    data = await service.find_user_by_id(id)
    return {
        "user": service.db_to_dict(data)
    }


@router.get("/", response_model=UserList)
async def get_users(
    service: UserService = Depends(
        get_service(UserService)),
):
    data = await service.get_users()

    return {
        "data": data
    }


@router.delete("/{id}")
async def delete_users(
    id: str,
    service: UserService = Depends(
        get_service(UserService)),
):

    await service.delete_user_by_id(id)

    return {
        "message": "user deleted"
    }


@router.put("/{id}")
async def update_users(
    id: str,
    item: dict,
    service: UserService = Depends(
        get_service(UserService)),

):
    await service.update_user_by_id(id, item)

    return {
        "message": "user updated"
    }
