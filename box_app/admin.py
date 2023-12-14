from django.contrib import admin
from .models import BoxingClass, BoxingClassMembership, User, Profile

# Register your models here.

admin.site.register(BoxingClass)
admin.site.register(BoxingClassMembership)
