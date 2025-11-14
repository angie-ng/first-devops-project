import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as c:
        yield c

def test_index(client):
    r = client.get("/")
    assert r.status_code == 200
    data = r.get_json()
    assert "message" in data

def test_echo(client):
    r = client.post("/echo", json={"text": "Ahoj"})
    assert r.status_code == 200
    data = r.get_json()
    assert data["data"]["text"] == "Ahoj"

