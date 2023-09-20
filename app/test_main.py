from dotenv import load_dotenv
load_dotenv(".env.tests")

from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_read_main(initialize_database):
    response = client.get("/buildings-types/")
    assert response.status_code == 200
    assert response.json() == {"message": "Test"}

