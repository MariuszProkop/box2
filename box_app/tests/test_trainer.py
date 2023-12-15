import pytest



@pytest.mark.django_db
def test_trainer(client, trainer):
    response = client.get(f'/trainer_detail/{trainer.id}/')
    assert response.status_code == 200
    context = response.context
    print(context)
    assert context['trainer'].name == trainer.name
    assert context['trainer'].surname == trainer.surname
    assert context['trainer'].age == int(trainer.age)
    assert context['trainer'].email == trainer.email








