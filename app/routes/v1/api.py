from fastapi import APIRouter
from app.routes.v1.endpoints import user


endpoint_router = APIRouter()


endpoint_router.include_router(
    user.router, prefix="/users", tags=["Users"]
)
