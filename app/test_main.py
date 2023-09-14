from fastapi.testclient import TestClient
from unittest.mock import patch
from .main import app

client = TestClient(app)

@patch('main.Database.get_data_from_db')
def test_read_main(mock_get_data_from_db):
    # Configurez le comportement simulé de la méthode get_data_from_db
    mock_get_data_from_db.return_value = ["Donnée fictive 1", "Donnée fictive 2"]

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Test"}
