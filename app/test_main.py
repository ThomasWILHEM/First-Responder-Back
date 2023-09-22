import pytest
import mysql.connector
import os
import sqlalchemy
from dotenv import load_dotenv
load_dotenv(".env.tests")

from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)
@pytest.fixture(scope="session")
def initialize_database():
    host_args = {
        "host": "localhost",
        "user": "root",
        "password": "admin",
        "database": "first-responder-tests",
        "port": 3307
    }

    con = mysql.connector.connect(**host_args)

    cur = con.cursor(dictionary=True)
    with open('app/utils/create_tests_base.sql', 'r') as sql_file:
        result_iterator = cur.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            print(f"Affected {res.rowcount} rows")

        con.commit()


def test_read_main(initialize_database):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Test"}