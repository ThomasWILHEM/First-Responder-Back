import pytest
from fastapi.testclient import TestClient
from app.main import app

all_types = {
    "results": [
        {
          "name": "Ambulance",
          "id": 2
        },
        {
          "name": "Voiture de patrouille",
          "id": 3
        },
        {
          "name": "VSAV",
          "id": 1
        }
      ]
}

type_4_response = {"id": 4, "name": "Véhicule banalisé"}

client = TestClient(app)


def test_get_all_building_type():
    response = client.get("/vehicles-types/")

    assert response.status_code == 200
    assert (response.json() == all_types)


def test_create_building_type():
    data = {"name": "Véhicule banalisé"}
    response = client.post("/vehicles-types/", json=data)

    assert response.status_code == 200
    assert (response.json() == type_4_response)


def test_get_building_type():
    response = client.get("/vehicles-types/4")

    assert response.status_code == 200
    assert (response.json() == type_4_response)


def test_delete_building_type():
    response = client.delete("/vehicles-types/4")

    assert response.status_code == 200
    assert (response.json() == type_4_response)

    response = client.get("/vehicles-types/4")
    assert response.status_code == 404

    response = client.get("/vehicles-types/")

    assert response.status_code == 200
    assert (response.json() == all_types)



