from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse

from .forms import ProjectForm
from .models import Project, ProjectTeam, Issue, Sprint


# project views
class ProjectListView(ListView):
    model = Project
    template_name = 'project/projects.html'

    def get_queryset(self):
        return Project.objects.filter(is_active=True).order_by('-start_date')


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_create_form.html'

    def get_success_url(self):
        return reverse('project:detail',
                       kwargs={'pk': self.object.id})


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_update_form.html'

    def get_success_url(self):
        return reverse('issue:project_detail',
                       kwargs={'pk': self.object.id})


class ProjectDeleteView(DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('project:index')

    def delete(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['pk'])

        project.is_active = False
        project.save()
        return HttpResponseRedirect(
            reverse('project:index'))


# sprint views
class SprintDetailView(DetailView):
    model = Sprint
    template_name = 'project/sprint.html'
    query_pk_and_slug = True
    pk_url_kwarg = 'sprint_id'
    slug_field = 'project'
    slug_url_kwarg = 'project_id'

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        cur_proj = self.kwargs['project_id']
        cur_spr = self.kwargs['sprint_id']

        issues_from_this_sprint = Issue.objects.filter(project_id=cur_proj,
                                                       sprint_id=cur_spr)
        context['project'] = get_object_or_404(Project, pk=cur_proj)
        context['new_issues'] = issues_from_this_sprint.filter(status="new")
        context['in_progress_issues'] = \
            issues_from_this_sprint.filter(status="in progress")
        context['resolved_issues'] = \
            issues_from_this_sprint.filter(status="resolved")
        return context


def sprints_list_view(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        sprints = Sprint.objects.filter(project=project_id) \
            .exclude(status=Sprint.ACTIVE)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    except Sprint.DoesNotExist:
        raise Http404("Sprint does not exist")

    return render(request, 'project/sprints_list.html',
                  {'project': project, 'sprints': sprints})


# issue views
def issue_detail_view(request, project_id, issue_id):
    current_issue = get_object_or_404(Issue, pk=issue_id, project=project_id)
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/issue.html', {
        'issue': current_issue, 'project': project, 'issue_id': issue_id
    })


def issue_create_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/create_issue.html',
                  {'project': project})


def issue_edit_view(request, project_id, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/edit_issue.html',
                  {'project': project, 'issue': issue})


# team views
def team(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    team_list = get_list_or_404(ProjectTeam, project=project)
    return render(request, 'project/team.html',
                  {'team_list': team_list, 'project': project})


# backlog views
def backlog(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        issues = Issue.objects.filter(project=project_id).filter(
            sprint__isnull=True)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    except Issue.DoesNotExist:
        raise Http404("Issue does not exist")

    return render(request, 'project/backlog.html',
                  {'project': project, 'issues': issues})
