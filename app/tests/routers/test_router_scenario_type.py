import pytest
from fastapi.testclient import TestClient
from app.main import app

all_types = {
    "results": [
        {
          "name": "Police",
          "id": 1
        },
        {
          "name": "Pompier",
          "id": 2
        }
      ]
}

type_3_response = {"id": 3, "name": "Secours"}

client = TestClient(app)


def test_get_all_scenario_type():
    response = client.get("/scenarios-types/")

    assert response.status_code == 200
    assert (response.json() == all_types)


def test_create_scenario_type():
    data = {"name": "Secours"}
    response = client.post("/scenarios-types/", json=data)

    assert response.status_code == 200
    assert (response.json() == type_3_response)


def test_get_scenario_type():
    response = client.get("/scenarios-types/3")

    assert response.status_code == 200
    assert (response.json() == type_3_response)


def test_delete_scenario_type():
    response = client.delete("/scenarios-types/3")

    assert response.status_code == 200
    assert (response.json() == type_3_response)

    response = client.get("/scenarios-types/3")
    assert response.status_code == 404

    response = client.get("/scenarios-types/")

    assert response.status_code == 200
    assert (response.json() == all_types)



