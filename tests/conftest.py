from typing import Callable, AsyncGenerator
from fastapi.applications import FastAPI
import pytest
import asyncio
from httpx import AsyncClient
from tests.integration.settings import get_settings as get_settings_test


def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = get_or_create_eventloop()
    yield loop
    loop.close()


@pytest.fixture()
async def override_get_db() -> Callable:
    async def _override_get_db():
        from tests.integration.database import get_database_async
        yield await get_database_async()

    return _override_get_db


@pytest.fixture()
def app(override_get_db: Callable,
        ) -> FastAPI:
    from app.database import get_database_async
    from app.config.settings import get_settings

    from app.main import app

    app.dependency_overrides[get_settings] = get_settings_test
    app.dependency_overrides[get_database_async] = override_get_db

    return app


@pytest.fixture()
async def async_client(
        app: FastAPI) -> AsyncGenerator:

    async with AsyncClient(app=app, base_url="http://testserver") as client:

        yield client
