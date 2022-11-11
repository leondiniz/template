from app.config.settings import get_settings
from app.routes.v1 import api
import logging
import sys
import orjson
import typing

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_400_BAD_REQUEST
from loguru import logger
from app.database import close_connection_async, \
    get_mongo_async
from fastapi_utils.tasks import repeat_every

LOG_LEVEL = logging.getLevelName("INFO")


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content)


def create_app() -> FastAPI:
    current_app = FastAPI(title="Fastapi",
                          description="Sample FastAPI Application",
                          version="1.0.0",
                          default_response_class=ORJSONResponse)

    current_app.include_router(
        api.endpoint_router, prefix=get_settings().API_V1)

    return current_app


app = create_app()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """Overrides default status code for validation errors
     from 422 to 400."""

    error_res = [
        {"type": err["type"], "msg": str(err["msg"]) +
         " in " + str(err["loc"][1]) if len(err["loc"]) > 1 else
         " ,".join(str(err["loc"]))}
        for err in exc.errors()
    ]

    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": error_res}),
    )


# origins = [
#     "http://localhost",
#     "http://localhost:4000",
#     "http://localhost:3000"
#     "http://localhost:8000"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.on_event('shutdown')
async def app_shutdown():
    await close_connection_async()


@app.on_event("startup")
async def app_start():
    await get_mongo_async()
