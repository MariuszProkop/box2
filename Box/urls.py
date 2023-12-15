"""
URL configuration for Box project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from box_app.views import (UserCreateView, MainView, LoginView, UserLogoutView, BaseView, BoxingClassDetailView,
                           TrainerView, StudentView, SearchView, AddStudentView, AddTrainerView, AddStudentSuccessView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_user/', UserCreateView.as_view(), name='add_user'),
    path('', MainView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('base/', BaseView.as_view(), name='baza'),
    path('boxing_class/<int:pk>/', BoxingClassDetailView.as_view(), name='boxing_class_detail'),
    path('trainer_detail/<int:trainer_id>/', TrainerView.as_view(), name='trainer_detail'),
    path('student_detail/<int:student_id>/', StudentView.as_view(), name='student_detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('add_student/', AddStudentView.as_view(), name="add_student"),
    path('add_trainer/', AddTrainerView.as_view(), name="add_trainer"),
    path('add_student_success/', AddStudentSuccessView.as_view(), name="add_student_success")



]
