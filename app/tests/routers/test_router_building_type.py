import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_all_building_type():
    response = client.get("/buildings-types/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Poste de police"},
        {"id": 2, "name": "Centre hospitalier"},
        {"id": 3, "name": "Caserne de pompier"},
    ]
