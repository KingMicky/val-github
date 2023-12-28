import pytest
from flask import Flask

from valentine_api import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def api_test(client):
    response = client.get('/valentine')
    assert response.status_code == 200
    data = response.get_json()
    assert 'quote' in data

def api_test(client):
    response = client.post('/will_you_be_my_valentine', data={'answer': 'yes'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'yes' in data['message'].lower()

    response = client.post('/will_you_be_my_valentine', data={'answer': 'no'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'no' in data['message'].lower()
