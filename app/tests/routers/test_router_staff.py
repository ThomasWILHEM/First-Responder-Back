import pytest
from fastapi.testclient import TestClient
from app.main import app

all_staffs = {
     "results": [
        {
          "firstname": "Jack",
          "lastname": "Brown",
          "type_id": 1,
          "vehicle_id": None,
          "building_id": 2,
          "id": 1,
          "type": {
            "name": "Pompier",
            "id": 1
          },
          "vehicle": None,
          "building": {
            "name": "Caserne de pompier La Réole",
            "address": "4 Avenue du Mahon, 33190 La Réole, France",
            "coordinates_latitude": 44.5821,
            "coordinates_longitude": -0.03226,
            "type_id": 3,
            "id": 2,
            "type": {
              "name": "Caserne de pompier",
              "id": 3
            }
          }
        },
        {
          "firstname": "Marie",
          "lastname": "Lisle",
          "type_id": 2,
          "vehicle_id": None,
          "building_id": 1,
          "id": 2,
          "type": {
            "name": "Gendarme",
            "id": 2
          },
          "vehicle": None,
          "building": {
            "name": "Gendarmerie La Réole",
            "address": "Gendarmerie nationale, A la Bori, Rue de Caumont, 33190 La Réole, France",
            "coordinates_latitude": 44.5825,
            "coordinates_longitude": -0.03149,
            "type_id": 1,
            "id": 1,
            "type": {
              "name": "Poste de police",
              "id": 1
            }
          }
        }
      ]
}

staff_to_add = {
  "firstname": "ok",
  "lastname": "google",
  "type_id": 2,
  "vehicle_id": None,
  "building_id": None
}

staff_3_response = {
  "firstname": "ok",
  "lastname": "google",
  "type_id": 2,
  "vehicle_id": None,
  "building_id": None,
  "id": 3,
  "type": {
    "name": "Gendarme",
    "id": 2
  },
  "vehicle": None,
  "building": None
}

client = TestClient(app)


def test_get_all_building():
    response = client.get("/staffs/")

    assert response.status_code == 200
    assert (response.json() == all_staffs)


def test_create_building():
    response = client.post("/staffs/", json=staff_to_add)

    assert response.status_code == 200
    assert (response.json() == staff_3_response)


def test_get_building():
    response = client.get("/staffs/3")

    assert response.status_code == 200
    assert (response.json() == staff_3_response)

def test_delete_building():
    response = client.delete("/staffs/3")

    assert response.status_code == 200
    assert (response.json() == {'message': 'Staff deleted'})

    response = client.get("/staffs/3")
    assert response.status_code == 404

    response = client.get("/staffs/")

    assert response.status_code == 200
    assert (response.json() == all_staffs)
