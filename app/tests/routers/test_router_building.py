import pytest
from fastapi.testclient import TestClient
from app.main import app

all_buildings = {
    "results":
        [
            {
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
            },
            {
                "name": "Caserne de pompier La Réole",
                "address": "4 Avenue du Mahon, 33190 La Réole, France",
                "coordinates_latitude": 44.5821,
                "coordinates_longitude": -0.032260,
                "type_id": 3,
                "id": 2,
                "type": {
                    "name": "Caserne de pompier",
                    "id": 3
                }
            }
        ]
}

building_to_add = {
    "name": "Centre Hospitalier La Réole",
    "address": "Chemin de Ronde, 33190 La Réole, France",
    "coordinates_latitude": 44.5862,
    "coordinates_longitude": -0.03791,
    "type_id": 2,
}

building_3_response = {
    "name": "Centre Hospitalier La Réole",
    "address": "Chemin de Ronde, 33190 La Réole, France",
    "coordinates_latitude": 44.5862,
    "coordinates_longitude": -0.03791,
    "type_id": 2,
    "id": 3,
    "type": {
        "name": "Centre hospitalier",
        "id": 2
    }
}

client = TestClient(app)


def test_get_all_building():
    response = client.get("/buildings/")

    assert response.status_code == 200
    assert (response.json() == all_buildings)


def test_create_building():
    response = client.post("/buildings/", json=building_to_add)

    assert response.status_code == 200
    assert (response.json() == building_3_response)


def test_get_building():
    response = client.get("/buildings/3")

    assert response.status_code == 200
    assert (response.json() == building_3_response)


def test_delete_building():
    response = client.delete("/buildings/3")

    assert response.status_code == 200
    assert (response.json() == {'message': 'Building deleted'})

    response = client.get("/buildings/3")
    assert response.status_code == 404

    response = client.get("/buildings/")

    assert response.status_code == 200
    assert (response.json() == all_buildings)

