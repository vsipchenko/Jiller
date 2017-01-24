from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from workflow.forms import LoginForm, RegistrationForm
from workflow.models import Employee
from workflow.models import Project



def index(request):
    return render(request, 'workflow/index.html')


def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('workflow:profile')
            else:
                messages.error(request, _("Wrong username or password"))
                return redirect('workflow:login')
    else:
        form = LoginForm()
    return render(request, 'workflow/login.html', {'form': form})



def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            employee = Employee.objects.create_user(username, email, password, last_name=last_name, first_name=first_name)
            return redirect('workflow:profile')

    form = RegistrationForm()
    return render(request, 'workflow/registration.html')



def project_detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'workflow/project_detail.html',
                  {'project': project})


def projtest(request):
    return render(request, 'workflow/project_navbar.html')


class ProjectDetail(DetailView):
    queryset = Project.objects.all()

    def get_object(self):
        object = super(ProjectDetail, self).get_object()
        return object


class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'end_date']
    template_name_suffix = '_create_form'


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'end_date']
    template_name_suffix = '_update_form'


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('author-list')
    template_name_suffix = '_delete_form'
