import pytest
from fastapi.testclient import TestClient
from app.main import app

all_buildings = {
    "results": [
        {
          "coordinates_latitude": 44.5825,
          "coordinates_longitude": -0.03149,
          "type_id": 3,
          "call_id": None,
          "building_id": 1,
          "id": 1,
          "type": {
            "name": "Voiture de patrouille",
            "id": 3
          },
          "call": None,
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
        },
        {
          "coordinates_latitude": 44.5821,
          "coordinates_longitude": -0.03226,
          "type_id": 3,
          "call_id": None,
          "building_id": 1,
          "id": 2,
          "type": {
            "name": "Voiture de patrouille",
            "id": 3
          },
          "call": None,
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
        },
        {
          "coordinates_latitude": 44.5821,
          "coordinates_longitude": -0.03226,
          "type_id": 1,
          "call_id": None,
          "building_id": 2,
          "id": 3,
          "type": {
            "name": "VSAV",
            "id": 1
          },
          "call": None,
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
        }
      ]
}

vehicle_to_add = {
    "coordinates_latitude": 0,
    "coordinates_longitude": 0,
    "type_id": 1,
    "call_id": None,
    "building_id": 2
}

vehicle_4_response = {
    "coordinates_latitude": 0,
    "coordinates_longitude": 0,
    "type_id": 1,
    "call_id": None,
    "building_id": 2,
    "id": 4,
    "type": {
        "name": "VSAV",
        "id": 1
    },
    "call": None,
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
}

client = TestClient(app)


def test_get_all_building():
    response = client.get("/vehicles/")

    assert response.status_code == 200
    assert (response.json() == all_buildings)


def test_create_building():
    response = client.post("/vehicles/", json=vehicle_to_add)

    assert response.status_code == 200
    assert (response.json() == vehicle_4_response)


def test_get_building():
    response = client.get("/vehicles/4")

    assert response.status_code == 200
    assert (response.json() == vehicle_4_response)


def test_add_vehicle_to_building():
    response = client.post("/vehicles/add_to_building?vehicle_id=4&building_id=1")
    assert response.status_code == 200
    assert response.json() == {
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


def test_send_vehicle_to_call():
    response = client.post("/vehicles/send_to_call?vehicle_id=4&call_id=1")
    assert response.status_code == 200
    assert response.json() == {
        "coordinates_latitude": 44.5825,
        "coordinates_longitude": -0.03149,
        "datetime": "2023-09-27T22:28:30",
        "completion_datetime": "2023-09-27T22:28:30",
        "scenario_id": 1,
        "mission_status": "En cours",
        "id": 1,
        "scenario": {
            "name": "Vol de voiture",
            "description": "Un individu à volé une voiture",
            "type_id": 1,
            "id": 1,
            "type": {
              "name": "Police",
              "id": 1
            }
        }
    }


def test_delete_building():
    response = client.delete("/vehicles/4")

    assert response.status_code == 200
    assert (response.json() == {'message': 'Vehicle deleted'})

    response = client.get("/vehicles/4")
    assert response.status_code == 404

    response = client.get("/vehicles/")

    assert response.status_code == 200
    assert (response.json() == all_buildings)

def test_read_vehicles_from_building():
    response = client.get("/vehicles/from-building/1")

    assert response.status_code == 200
    assert (response.json() == {
        "results": [
            {
                "coordinates_latitude": 44.5825,
                "coordinates_longitude": -0.03149,
                "type_id": 3,
                "call_id": None,
                "building_id": 1,
                "id": 1,
                "type": {
                    "name": "Voiture de patrouille",
                    "id": 3
                },
                "call": None,
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
            },
            {
                "coordinates_latitude": 44.5821,
                "coordinates_longitude": -0.03226,
                "type_id": 3,
                "call_id": None,
                "building_id": 1,
                "id": 2,
                "type": {
                    "name": "Voiture de patrouille",
                    "id": 3
                },
                "call": None,
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
    })
