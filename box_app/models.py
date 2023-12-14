from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class BoxingClass(models.Model):
    class_name = models.CharField(max_length=20)
    level_choices = [
        ('1', 'Podstawowy'),
        ('2', 'Średnio-zaawansowany'),
        ('3', 'Zaawansowany'),
    ]
    level = models.CharField(max_length=1, choices=level_choices)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True,
                                limit_choices_to={'is_teacher': True}, related_name='classes_as_teacher')
    students = models.ManyToManyField('User', through='BoxingClassMembership', limit_choices_to={'is_student': True}, related_name='classes_as_student')

    def __str__(self):
        return f'{self.class_name}'


class BoxingClassMembership(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_memberships',
                                limit_choices_to={'is_student': True})
    boxing_class = models.ForeignKey(BoxingClass, on_delete=models.CASCADE, related_name='class_memberships')


class Profile(models.Model):
    age = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    teachers = models.ManyToManyField(User, related_name='students')
    students = models.ManyToManyField(User, related_name='teachers')
    #type = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)



CHOICES = (
    (1, "Student"),
    (2, "Trainer"),
)
