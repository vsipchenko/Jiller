from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Project, ProjectTeam, Issue


def index(request):
    return render(request, 'workflow/index.html')


def create_issue(request, project_id):
    return render(request, 'workflow/create_issue.html',
                  {'project_id': project_id})


def edit_issue(request, project_id, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    return render(request, 'workflow/edit_issue.html', {'project_id': project_id, 'issue': issue})


def team(request, project_id):
    current_project = get_object_or_404(Project, pk=project_id)
    team_list = get_list_or_404(ProjectTeam, project=current_project)
    return render(request, 'workflow/team.html', {'team_list': team_list, 'project_id': project_id})


