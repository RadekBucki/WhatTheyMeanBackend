# tests/test_app.py
from backend import app
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_get_analysis(client):
    response = client.get('/analyse')
    assert response.status_code == 200
    assert [] == response.json

def test_get_analyse_by_id(client):
    response = client.get('/analyse/1')
    assert response.status_code == 200
    assert "Get analyse 1" == response.data.decode("utf-8")