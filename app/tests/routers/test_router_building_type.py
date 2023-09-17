import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_all_building_type():
    response = client.get("/buildings-types/")

    assert response.status_code == 200
    assert (response.json() == {
        "results":
            [
                {"id": 1, "name": "Poste de police"},
                {"id": 2, "name": "Centre hospitalier"},
                {"id": 3, "name": "Caserne de pompier"},
            ]
    })


def test_create_building_type():
    data = {"name": "test"}
    response = client.post("/buildings-types/", json=data)

    assert response.status_code == 200
    assert (response.json() == {"id": 4, "name": "test"})


def test_get_building_type():
    response = client.get("/buildings-types/4")

    assert response.status_code == 200
    assert (response.json() == {"id": 4, "name": "test"})


def test_delete_building_type():
    response = client.delete("/buildings-types/4")

    assert response.status_code == 200
    assert (response.json() == {"id": 4, "name": "test"})

    response = client.get("/buildings-types/4")
    assert response.status_code == 404

    response = client.get("/buildings-types/")

    assert response.status_code == 200
    assert (response.json() == {
        "results":
            [
                {"id": 1, "name": "Poste de police"},
                {"id": 2, "name": "Centre hospitalier"},
                {"id": 3, "name": "Caserne de pompier"},
            ]
    })


