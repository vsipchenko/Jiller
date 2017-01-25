from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect

from workflow.forms import LoginForm, RegistrationForm
from workflow.models import Employee


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
            employee = Employee.objects.create_user(username, email, password, last_name=last_name,
                                                    first_name=first_name)
            return redirect('workflow:profile')
    else:
        form = RegistrationForm()
    return render(request, 'workflow/registration.html', {'form': form.as_p()})
