import pytest
from django.urls import reverse



@pytest.mark.django_db
def test_boxing_class_detail_view_logout(user_client_logout):
    response = user_client_logout.get(reverse('baza'))
    assert response.context['user'].is_authenticated is False
