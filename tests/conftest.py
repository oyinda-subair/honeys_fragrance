from typing import Generator

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as test_client:
        yield test_client
        app.dependency_overrides = {}
