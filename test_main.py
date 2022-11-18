'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

JWT_SECRET = os.environ.get('JWT_SECRET', 'abc123abc1234')
TOKEN = os.environ.get(
    'TOKEN', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjEzMDY3OTAsIm5iZiI6MTU2MDA5NzE5MCwiZW1haWwiOiJ3b2xmQHRoZWRvb3IuY29tIn0.IpM4VMnqIgOoQeJxUbLT-cRcAjK41jronkVrqRLFmmk')
EMAIL = os.envron.get('EMAIL', 'wolf@thedoor.com')
PASSWORD = os.environ.get('PASSWORD', 'huff12puff34;-)')


@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = JWT_SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client


def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'
    assert False


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth',
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
