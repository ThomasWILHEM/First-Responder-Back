import pytest
from sqlalchemy import create_engine, text
import os

@pytest.fixture(scope="module")
def initialize_database():
    host = "localhost"
    user = "root"
    password = "admin"
    database = "first-responder-tests"
    port = "3307"

    engine = create_engine(
        os.environ.get("DATABASE_URL")
    )

    # Exécutez le script SQL
    with engine.connect() as conn:
        conn.execute(text(open("app/utils/create_tests_base.sql", "r").read()))
