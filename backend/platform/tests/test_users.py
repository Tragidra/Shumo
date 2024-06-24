from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={"username": "testuser", "email": "testuser@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"