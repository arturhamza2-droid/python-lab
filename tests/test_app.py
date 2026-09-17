from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Python Lab API работает"}


def test_greet() -> None:
    response = client.get("/greet/Artur")

    assert response.status_code == 200
    assert response.json() == {"message": "Привет, Artur!"}
