import pytest
from django.test import Client

c = Client()


def test_index():
    response = c.get('/profiles/')
    assert response.status_code == 200
    assert response.data == b'profiles'


def test_profile():
    response = c.get('/profiles/1/')
    assert response.status_code == 200
    assert response.data == b'Buenos Aires'
