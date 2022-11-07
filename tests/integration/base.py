from tests.integration.helper import set_envs_for_tests
from tests.integration.database import get_database
from tests.integration.settings import get_settings


class BaseTest:

    @classmethod
    async def setup_class(cls):
        """setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        set_envs_for_tests()
        cls.database = get_database

        cls.users_collection = await cls.database.get_collection(
            'users')

        cls.user = 'admin@teste.com.br'
        cls.settings = get_settings()

    @classmethod
    async def teardown_class(cls):
        """teardown any state that was previously setup with a call to
        setup_class.
        """
        for collection in cls.database.list_collection_names():
            await cls.database.drop_collection(collection)
