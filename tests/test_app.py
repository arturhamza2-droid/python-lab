from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Python Lab API работает"}


def test_calculate() -> None:
    response = client.post("/calculate", json={"price": 100, "quantity": 2})

    assert response.status_code == 200
    assert response.json() == {"price": 100.0, "quantity": 2, "total": 200.0}


def test_calculate_rejects_zero_price() -> None:
    response = client.post("/calculate", json={"price": 0, "quantity": 2})

    assert response.status_code == 422


def test_calculate_rejects_negative_quantity() -> None:
    response = client.post("/calculate", json={"price": 100, "quantity": -1})

    assert response.status_code == 422


def test_greet() -> None:
    response = client.get("/greet/Artur")

    assert response.status_code == 200
    assert response.json() == {"message": "Привет, Artur!"}
