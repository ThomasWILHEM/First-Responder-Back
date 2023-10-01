import pytest
from fastapi.testclient import TestClient
from app.main import app

all_scenarios = {
    "results": [
        {
            "name": "Vol de voiture",
            "description": "Un individu à volé une voiture",
            "type_id": 1,
            "id": 1,
            "type": {
                "name": "Police",
                "id": 1
            }
        },
        {
            "name": "Ivresse sur la voie publique",
            "description": "Un individu est ivre sur la voie publique",
            "type_id": 1,
            "id": 2,
            "type": {
                "name": "Police",
                "id": 1
            }
        },
        {
            "name": "Accident de la route",
            "description": "Un accident à eu lieu sur la voie publique",
            "type_id": 2,
            "id": 3,
            "type": {
                "name": "Pompier",
                "id": 2
            }
        }
    ]
}

scenario_to_add = {
    "name": "Arbre sur la voie publique",
    "description": "Un arbre est tombé sur la voie publique et bloque la route",
    "type_id": 2
}

scenario_4_response = {
    "name": "Arbre sur la voie publique",
    "description": "Un arbre est tombé sur la voie publique et bloque la route",
    "type_id": 2,
    "id": 4,
    "type": {
        "name": "Pompier",
        "id": 2
    }
}

client = TestClient(app)


def test_get_all_scenario():
    response = client.get("/scenarios/")

    assert response.status_code == 200
    assert (response.json() == all_scenarios)


def test_create_scenario():
    response = client.post("/scenarios/", json=scenario_to_add)

    assert response.status_code == 200
    assert (response.json() == scenario_4_response)


def test_get_scenario():
    response = client.get("/scenarios/4")

    assert response.status_code == 200
    assert (response.json() == scenario_4_response)


def test_delete_scenario():
    response = client.delete("/scenarios/4")

    assert response.status_code == 200
    assert (response.json() == {'message': 'Scenario deleted'})

    response = client.get("/scenarios/4")
    assert response.status_code == 404

    response = client.get("/scenarios/")

    assert response.status_code == 200
    assert (response.json() == all_scenarios)
