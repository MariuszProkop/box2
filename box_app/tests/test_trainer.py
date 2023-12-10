import pytest
from box_app.models import Trainer


@pytest.mark.django_db
def test_trainer(client, trainer):
    response = client.get(f'/trainer_detail/{trainer.id}/')
    assert response.status_code == 200
    context = response.context
    assert context['name'] == trainer.name
    assert context['surname'] == trainer.surname
    assert context['age'] == trainer.age
    assert context['email'] == trainer.email








