from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'workflow/index.html')


def login(request):
    return render(request, 'workflow/login.html')

def registration(request):
    return render(request, 'workflow/registration.html')

