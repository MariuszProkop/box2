import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_boxing_class_detail_view_logout(user_client_logout):
    response = user_client_logout.get(reverse("logout"))
    assert response.status_code == 302
