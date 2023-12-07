from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, FormView, DetailView
from django.contrib.auth import login, logout
from box_app.forms import UserCreateForm, LoginForm, SearchForm, AddStudentForm
from box_app.models import BoxingClass, BoxingClassMembership, Student, Trainer
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

"""
MainView - Is a view that display list of boxing classes, LoginRequiredMixin allows only authenticated users to view 
this site, by redirecting them to login view using login_url, method get retrieve object from model BoxingClass, and 
render it with Template base.html
"""


class MainView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        boxingclasses = BoxingClass.objects.all().order_by('pk')
        return render(request, "base.html", {'boxingclassess': boxingclasses})


"""
LoginView - Is a view for user login. Its using FormView which is generic form to display a view. LoginView is using 
form_class = LoginForm for user to login, template_name = 'form.html' is rendering login form, success_url = '/' is 
redirecting user to MainView using form_valid(self,form) for handling valid form submission.
"""


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'form.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.user
        login(self.request, user)
        return super().form_valid(form)


"""
UserLogoutView - is a view for user logout. Its using LogoutView which is Django class-based view for user logout, this
view is using template_name = 'form.html' to render template upon successful user logout.
"""


class UserLogoutView(LogoutView):
    template_name = 'form.html'


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'form.html'
    success_url = '/'


class BaseView(View):
    def get(self, request):
        return render(request, 'baza.html')


class BoxingClassDetailView(DetailView):
    model = BoxingClass
    template_name = 'boxing_class_detail2.html'
    context_object_name = 'boxing_class'


class TrainerView(View):
    def get(self, request, trainer_id):
        trainer = get_object_or_404(Trainer, pk=trainer_id)
        student = trainer.student
        taugh = trainer.boxingclass_set.all()
        context = {"trainer": trainer,
                   "student": student,
                   "taugh": taugh}
        return render(request, "Trainer.html", context)


class StudentView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        trainer = student.teachers.all()
        context = {"student": student,
                   "trainer": trainer}
        return render(request, "student.html", context)


class SearchView(View):
    def get(self, request):
        form = SearchForm()
        return render(request, "search.html", {"form": form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            trainer = Trainer.objects.filter(surname__icontains=form.cleaned_data['last_name'])
            ctx = {"form": form,
                   "trainer": trainer}
            return render(request, "search.html", ctx)
        else:
            return render(request, "search.html", {"form": form})


class AddStudent(View):
    def get(self, request):
        form = AddStudentForm()
        return render(request, "add_student.html", {"form": form})

    def post(self, request):
        form = AddStudentForm(request.POST)
        if form.is_valid():
            new_student = Student.objects.create(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
            )

            class_name = form.cleaned_data['class_name']
            boxing_class = BoxingClass.objects.get(class_name=class_name)
            boxing_class.students.add(new_student)

            return redirect("student_detail", new_student.pk)
        else:
            return render(request, "add_student.html", {"form": form})
