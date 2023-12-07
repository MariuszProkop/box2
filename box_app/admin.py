from django.contrib import admin
from .models import Student, Trainer, BoxingClass, BoxingClassMembership

# Register your models here.
admin.site.register(Student)
admin.site.register(Trainer)
admin.site.register(BoxingClass)
admin.site.register(BoxingClassMembership)


