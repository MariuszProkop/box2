import pytest

from django.urls import reverse
@pytest.mark.django_db
def test_student_view_requires_login(client, student):
    response = client.get(reverse('student_detail', args=[student.id]))
    assert response.status_code == 302
   # context = response.context
    #assert context['student'].name == student.name
    #assert context['student'].surname == student.surname
    #assert context['student'].age == int(student.age)
    #assert context['student'].email == student.email
