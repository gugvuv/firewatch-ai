import os

import pytest
from fastapi.testclient import TestClient

# Ensure settings load in test env
os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://firewatch:firewatch@localhost:5432/firewatch")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")

from app.main import app  # noqa: E402


@pytest.fixture
def client():
    return TestClient(app)
