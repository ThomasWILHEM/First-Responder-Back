import pytest
import datetime
from fastapi.testclient import TestClient
from app.main import app

now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
print(now)

all_calls = {
    "results": [
        {
            "coordinates_latitude": 0,
            "coordinates_longitude": 0,
            "datetime": "2023-10-02T20:51:56.166Z",
            "completion_datetime": "2023-10-02T20:51:56.166Z",
            "scenario_id": 0,
            "mission_status": "string",
            "id": 0,
            "scenario": {
                "name": "string",
                "description": "string",
                "type_id": 0,
                "id": 0,
                "type": {
                    "name": "string",
                    "id": 0
                }
            }
        }
    ]
}


call_to_add = {
  "coordinates_latitude": 0,
  "coordinates_longitude": 0,
  "datetime": now,
  "completion_datetime": now,
  "scenario_id": 1,
  "mission_status": "string"
}

call_2_response = {
        "coordinates_latitude": 0,
        "coordinates_longitude": 0,
        "datetime": now,
        "completion_datetime": now,
        "scenario_id": 1,
        "mission_status": "string",
        "id": 2,
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


client = TestClient(app)


#def test_get_all_call():
#    response = client.get("/calls/")
#
#    assert response.status_code == 200
#    assert (response.json() == all_calls)
#
#
#def test_create_call():
#    response = client.post("/calls/", json=call_to_add)
#
#    assert response.status_code == 200
#    assert (response.json() == call_2_response)
#
#
#def test_get_call():
#    response = client.get("/calls/2")
#
#    assert response.status_code == 200
#    assert (response.json() == call_2_response)
#
#
#def test_delete_call():
#    response = client.delete("/calls/2")
#
#    assert response.status_code == 200
#    assert (response.json() == {'message': 'Call deleted'})
#
#    response = client.get("/calls/2")
#    assert response.status_code == 404
#
#    response = client.get("/calls/")
#
#    assert response.status_code == 200
#    assert (response.json() == all_calls)
