from django.shortcuts import render
from .models import Project, Sprint


def index(request):
    return render(request, 'workflow/index.html')


def sprints_list(request, pr_id):
    project = Project.objects.filter(pk=pr_id)
    sprints = Sprint.objects.filter(project=pr_id)

    return render(request, 'workflow/sprints_list.html', {'project': project,
                                                          'sprints': sprints})
