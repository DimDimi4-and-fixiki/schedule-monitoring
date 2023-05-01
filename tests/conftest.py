import pytest
from fastapi.testclient import TestClient

from commands.run_server import main_app


@pytest.fixture(scope='session')
def client() -> TestClient:
    app = main_app()
    return TestClient(app)
