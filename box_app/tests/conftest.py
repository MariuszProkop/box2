import pytest
from django.contrib.auth.models import User
from django.test import Client
from box_app.models import Trainer, Student


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def trainer():
    user = User.objects.create_user(username='karol_user', password='test123')
    trainer = Trainer.objects.create(name='Karol', surname='Karolak', age='33', email='karol@karol.pl', user=user)
    return trainer


@pytest.fixture
def student():
    user = User.objects.create_user(username='karol_user2', password='test1234')
    student = Student.objects.create(name='Karol', surname='Karolak', age='23', email='karol2@karol.pl', user=user)
    return student

@pytest.fixture
def user_client():
    user = User.objects.create_user(username='karol_user', password='test123')
    client = Client()
    client.force_login(user)
    return client

@pytest.fixture
def user_client_logout():
    user = User.objects.create_user(username='karol_user', password='test123')
    client = Client()
    client.force_login(user)
    client.logout()
    return client
