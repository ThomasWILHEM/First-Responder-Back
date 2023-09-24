import pytest
from fastapi.testclient import TestClient
from app.main import app

all_types = {
    "results":
        [
            {"id": 1, "name": "Poste de police"},
            {"id": 2, "name": "Centre hospitalier"},
            {"id": 3, "name": "Caserne de pompier"},
        ]
}

type_4_response = {"id": 4, "name": "test"}

client = TestClient(app)


def test_get_all_building_type():
    response = client.get("/buildings-types/")

    assert response.status_code == 200
    assert (response.json() == all_types)


def test_create_building_type():
    data = {"name": "test"}
    response = client.post("/buildings-types/", json=data)

    assert response.status_code == 200
    assert (response.json() == type_4_response)


def test_get_building_type():
    response = client.get("/buildings-types/4")

    assert response.status_code == 200
    assert (response.json() == type_4_response)


def test_delete_building_type():
    response = client.delete("/buildings-types/4")

    assert response.status_code == 200
    assert (response.json() == type_4_response)

    response = client.get("/buildings-types/4")
    assert response.status_code == 404

    response = client.get("/buildings-types/")

    assert response.status_code == 200
    assert (response.json() == all_types)



