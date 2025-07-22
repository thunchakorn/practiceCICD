from fastapi.testclient import TestClient
from main import app
import psycopg2

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    response = client.get("/items/42?q=example")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "example"}


def test_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5436,
        user="username",
        password="pass123",
        dbname="test_db",
    )
    assert conn.status == psycopg2.extensions.STATUS_READY
