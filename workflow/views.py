from django.shortcuts import render

# Create your views here.
from workflow.models import Employee

Employee
def index(request):
    return render(request, 'workflow/index.html')

