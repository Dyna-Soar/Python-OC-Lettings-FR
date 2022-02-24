import pytest

from django.test import Client
from django.urls import reverse

c = Client()


@pytest.mark.django_db
def test_index():
    response = c.get(reverse('index'))
    assert response.status_code == 200
    assert b'Holiday Homes' in response.content
