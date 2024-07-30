import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture
def task_data():
    return {"title": "Test Task", "description": "This is a test task"}


def test_create_task(task_data):
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    assert response.json()["title"] == task_data["title"]


def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
