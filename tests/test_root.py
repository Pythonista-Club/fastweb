from fastapi.testclient import TestClient
from src.app.api import app

client = TestClient(app)

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200 
    assert response.json() == {"resp":"Welcome for the Pythonista Club! "} 