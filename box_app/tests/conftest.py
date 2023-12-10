import pytest
from django.contrib.auth.models import User
from django.test import Client
from box_app.models import Trainer


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def trainer():
    user = User.objects.create_user(username='karol_user', password='test123')
    trainer = Trainer.objects.create(name='Karol', surname='Karolak', age='33', email='karol@karol.pl', user=user)
    return trainer
