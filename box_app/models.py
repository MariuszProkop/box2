from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    teachers = models.ManyToManyField('Trainer', related_name='students')

    def __str__(self):
        return f'{self.name}  {self.surname}'


class BoxingClass(models.Model):
    class_name = models.CharField(max_length=20)
    level_choices = [
        ('1', 'Podstawowy'),
        ('2', 'Średnio-zaawansowany'),
        ('3', 'Zaawansowany'),
    ]
    level = models.CharField(max_length=1, choices=level_choices)
    teacher = models.ForeignKey('Trainer', on_delete=models.CASCADE, null=True, blank=True)
    students = models.ManyToManyField('Student', through='BoxingClassMembership')

    def __str__(self):
        return f'{self.class_name}'


class BoxingClassMembership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='class_memberships')
    boxing_class = models.ForeignKey(BoxingClass, on_delete=models.CASCADE, related_name='class_memberships')


class Trainer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
