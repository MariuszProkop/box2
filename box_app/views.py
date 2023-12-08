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
    login_url = '/base/'

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


"""
UserCreateView - is a view for registration of new user. Its using CreateView which is Django class-based view for user
registration, this view is using template_name = 'form' to render upon successful user registration, success_url = '/' 
is redirecting user to MainView after successful registration.
"""


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'form.html'
    success_url = '/'


"""
BaseView - is a view that allows user to login, its also shows which user is currently logged, and its giving option for 
user to logout.
"""


class BaseView(View):
    def get(self, request):
        return render(request, 'baza.html')


"""
BoxingClassDetailView - is a view that's show information's about specific instance of the 'BoxingClass' model, its 
showing details about level of boxing class, who's teaching it, and who is student in this class
"""


class BoxingClassDetailView(DetailView):
    model = BoxingClass
    template_name = 'boxing_class_detail.html'
    context_object_name = 'boxing_class'


"""
TrainerView - is view that show detail information about trainer, his name, surname, age, mail, what student is asigned 
to him and in what class he is teaching. Method get is giving access to Trainer object and trainer_id,  
student = trainer.student is giving access to details about student that is assigned to him, 
taught = trainer.boxingclass_set.all() is giving access to BoxingClass from build in relation that Django automatically 
created
"""


class TrainerView(View):
    def get(self, request, trainer_id):
        trainer = get_object_or_404(Trainer, pk=trainer_id)
        student = trainer.student
        taught = trainer.boxingclass_set.all()
        context = {"trainer": trainer,
                   "student": student,
                   "taught": taught}
        return render(request, "Trainer.html", context)


"""
StudentView - is a view that detail information about student, his name, surname, age, mail and to which trainer is 
assigned for individual training
"""
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
