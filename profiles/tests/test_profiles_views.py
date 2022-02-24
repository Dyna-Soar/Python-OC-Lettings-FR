import pytest

from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

from profiles.models import Profile

c = Client()


@pytest.mark.django_db
def test_index():
    response = c.get(reverse('profiles:profiles_index'))
    assert response.status_code == 200
    assert b'profiles' in response.content


@pytest.mark.django_db
def test_profile():
    user = User.objects.create_user(
        username='HeadlinesGazer',
        password='Abc1234!',
        first_name='Jamie',
        last_name='Lal',
        email='jssssss33@acee9.live'
    )
    Profile.objects.create(user=user, favorite_city='Buenos Aires')
    response = c.get(reverse('profiles:profile', kwargs={'username': 'HeadlinesGazer'}))
    assert response.status_code == 200
    assert b'HeadlinesGazer' in response.content
