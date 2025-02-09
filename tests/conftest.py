from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> TestClient:
    from src.api import app

    return TestClient(app)
