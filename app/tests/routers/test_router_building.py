import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_building():
    response = client.get("/buildings/")

    assert response.status_code == 200
    assert (response.json() == {
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
                    "coordinates_latitude": 44.582074,
                    "coordinates_longitude": -0.032260,
                    "type_id": 3,
                    "id": 2,
                    "type": {
                        "name": "Caserne de pompier",
                        "id": 3
                    }
                }
            ]
    })


def test_create_building():
    data = {
        "name": "Centre Hospitalier La Réole",
        "address": "Chemin de Ronde, 33190 La Réole, France",
        "coordinates_latitude": 44.586246,
        "coordinates_longitude": -0.03791,
        "type_id": 2,
    }
    response = client.post("/buildings/", json=data)

    assert response.status_code == 200
    assert (response.json() == {
        "name": "Centre Hospitalier La Réole",
        "address": "Chemin de Ronde, 33190 La Réole, France",
        "coordinates_latitude": 44.586246,
        "coordinates_longitude": -0.03791,
        "type_id": 2,
        "id": 3,
        "type": {
            "name": "Centre hospitalier",
            "id": 2
        }
    })


#def test_get_building():
#    response = client.get("/buildings-types/4")
#
#    assert response.status_code == 200
#    assert (response.json() == {"id": 4, "name": "test"})
#
#
#def test_delete_building():
#    response = client.delete("/buildings-types/4")
#
#    assert response.status_code == 200
#    assert (response.json() == {"id": 4, "name": "test"})
#
#    response = client.get("/buildings-types/4")
#    assert response.status_code == 404
#
#    response = client.get("/buildings-types/")
#
#    assert response.status_code == 200
#    assert (response.json() == {
#        "results":
#            [
#                {"id": 1, "name": "Poste de police"},
#                {"id": 2, "name": "Centre hospitalier"},
#                {"id": 3, "name": "Caserne de pompier"},
#            ]
#    })
