from django.shortcuts import render
from .models import Project, Issue


def index(request):
    return render(request, 'workflow/index.html')


def backlog(request, pr_id):
    project = Project.objects.filter(pk=pr_id)
    issues = Issue.objects.filter(project=pr_id).filter(status__isnull=True)

    return render(request, 'workflow/backlog.html', {'project': project,
                                                     'issues': issues})
