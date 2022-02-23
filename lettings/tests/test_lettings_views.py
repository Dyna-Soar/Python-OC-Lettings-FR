import pytest
from django.test import Client

c = Client()


def test_index():
    response = c.get('/lettings/')
    assert response.status_code == 200
    assert response.data == b'Lettings'


def test_letting():
    response = c.get('/lettings/1')
    assert response.status_code == 200
    assert response.data == b'Joshua Tree Green Haus /w Hot Tub'
