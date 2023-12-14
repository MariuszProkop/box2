from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from box_app.models import BoxingClass, Profile
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        self.user = authenticate(username=username, password=password)
        if self.user is None:
            raise forms.ValidationError('Nieprawidlowy login i haslo')


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Hasła różnią się')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class SearchForm(forms.Form):
    last_name = forms.CharField(max_length=64, label="wprowadz fragment nazwiska")


class AddStudentForm(forms.Form):
    name = forms.CharField(max_length=64, label="Imię")
    surname = forms.CharField(max_length=64, label="Nazwisko")
    class_name = forms.ModelChoiceField(queryset=BoxingClass.objects.all(), label="Klasa")
    age = forms.CharField(max_length=64, label="Wiek")
    email = forms.CharField(max_length=64, label="Email")


class TrainerForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'surname', 'email']
        fields = "__all__"


# class TrainerCreateForm(forms.ModelForm):
#     class Meta(UserCreateForm):
#         model = User
#
#         def save(self, commit=True):
#             user = super().save(commit=False)
#             user.is_teacher = True
#             if commit:
#                 user.save()
#             return user
#
# class StudentCreateForm(forms.ModelForm):
#     class Meta(UserCreateForm.Meta):
#         model = User
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_student = True
#         if commit:
#             user.save()
#         return user
