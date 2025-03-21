import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json["message"] == "Example Python Application"

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_info(client):
    response = client.get('/info')
    assert response.status_code == 200
    assert "app" in response.json
    assert "version" in response.json