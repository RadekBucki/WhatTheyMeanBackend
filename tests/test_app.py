# tests/test_app.py
import app
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert b'Connected' in response.data

def test_register(client):
    response = client.post('/register', data={'username': 'testuser'})
    assert b'Registration successful' in response.data