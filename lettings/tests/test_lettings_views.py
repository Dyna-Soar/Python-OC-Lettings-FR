import pytest

from django.test import Client
from django.urls import reverse

from lettings.models import Letting, Address


c = Client()


@pytest.mark.django_db(transaction=True)
def test_index():
    response = c.get(reverse('lettings:lettings_index'))
    assert response.status_code == 200
    assert b'Lettings' in response.content


@pytest.mark.django_db
def test_letting():
    address = Address.objects.create(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA"
    )
    Letting.objects.create(title="Joshua Tree Green Haus /w Hot Tub", address=address)
    response = c.get(reverse('lettings:letting', kwargs={'letting_id': 1}))
    assert response.status_code == 200
    assert b'Joshua Tree Green Haus /w Hot Tub' in response.content
