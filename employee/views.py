from django.shortcuts import render

from workflow.models import Employee


def employee_index_view(request):
    employee_list = Employee.objects.all()
    render(request, 'employee/index.html', {'employee_list': employee_list})
