from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.utils import timezone
from workflow.models import Project


def index(request):
    return render(request, 'workflow/index.html')


# def project(request, project_id):
#     return render(request, 'workflow/project_detail.html')

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'workflow/project_detail.html'


class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'start_date', 'end_date']