import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_main_view_requires_login(client):
    response = client.get(reverse('index'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_main_view_accessible_after_login(user_client):
    response = user_client.get(reverse('index'))
    assert response.status_code == 200
