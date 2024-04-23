import pytest
from flaskr import create_app
from sqlalchemy import create_engine

@pytest.fixture()
def app():
    app = create_app()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()