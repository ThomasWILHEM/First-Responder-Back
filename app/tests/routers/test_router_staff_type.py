import pytest
from fastapi.testclient import TestClient
from app.main import app

all_types = {
    "results": [
        {
          "name": "Gendarme",
          "id": 2
        },
        {
          "name": "Pompier",
          "id": 1
        }
      ]
}

type_3_response = {"id": 3, "name": "Ambulancier"}

client = TestClient(app)


def test_get_all_staff_type():
    response = client.get("/staffs-types/")

    assert response.status_code == 200
    assert (response.json() == all_types)


def test_create_staff_type():
    data = {"name": "Ambulancier"}
    response = client.post("/staffs-types/", json=data)

    assert response.status_code == 200
    assert (response.json() == type_3_response)


def test_get_staff_type():
    response = client.get("/staffs-types/3")

    assert response.status_code == 200
    assert (response.json() == type_3_response)


def test_delete_staff_type():
    response = client.delete("/staffs-types/3")

    assert response.status_code == 200
    assert (response.json() == type_3_response)

    response = client.get("/staffs-types/3")
    assert response.status_code == 404

    response = client.get("/staffs-types/")

    assert response.status_code == 200
    assert (response.json() == all_types)



