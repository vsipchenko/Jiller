from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectTeam, Issue


def index(request):
    return render(request, 'workflow/index.html')


def create_issue(request, project_id):
    return render(request, 'workflow/create_issue.html', {'project_id': project_id})


def edit_issue(request, project_id, issue_id):
    return render(request, 'workflow/edit_issue.html', {'project_id': project_id, 'issue_id': issue_id})


def team(request, project_id):

    return render(request, 'workflow/team.html', {'project_id': project_id})


def not_found(request):
    return render(request, 'workflow/not_found.html')