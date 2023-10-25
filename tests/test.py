from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_client():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hi Dev!"}

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
