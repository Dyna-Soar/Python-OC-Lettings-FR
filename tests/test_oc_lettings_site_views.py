import pytest
from django.test import Client

c = Client()


def test_index():
    response = c.get('')
    assert response.status_code == 200
    assert response.data == b'Holiday Homes'
