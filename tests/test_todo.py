from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_todo():
    todo = {"id": 1, "title": "Test Task", "completed": False}
    response = client.post("/todos/", json=todo)
    assert response.status_code == 200
    assert response.json() == todo

    response = client.get("/todos/")
    assert response.status_code == 200
    assert todo in response.json()

def test_update_todo():
    updated_todo = {"id": 1, "title": "Updated Task", "completed": True}
    response = client.put("/todos/1", json=updated_todo)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted"
