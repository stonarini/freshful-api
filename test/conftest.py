import pytest
from app import create_app
from repository.db import init_db, drop_db


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture(scope="module")
def client(app):
    with app.app_context():
        init_db("TestGildedRose")

        yield app.test_client()

        drop_db("TestGildedRose")
