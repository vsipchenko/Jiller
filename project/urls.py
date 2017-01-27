from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
    # project urls
    url(r'^$', views.ProjectListView.as_view(), name='index'),
    url(r'^create/$', views.ProjectCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', views.ProjectUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.ProjectDeleteView.as_view(), name='delete'),

    # issue urls
    url(r'^(?P<project_id>\w+)/issue/create/$',
        views.issue_create_view, name='issue_create'),
    url(r'^(?P<project_id>\w+)/issue/(?P<issue_id>\w+)/edit/$',
        views.issue_edit_view, name='issue_edit'),
    url(r'^(?P<project_id>[0-9]+)/issue/(?P<issue_id>[0-9]+)/$',
        views.issue_detail_view, name='issue_detail'),

    # team urls
    url(r'^(?P<project_id>\w+)/team/$', views.team, name='team'),

    # backlog urls
    url(r'^(?P<project_id>[0-9]+)/backlog/$', views.backlog,
        name='backlog'),

    # sprint urls
    url(r'^(?P<project_id>[0-9]+)/sprint/$',
        views.sprints_list_view, name='sprints_list'),
    url(r'^(?P<project_id>[0-9]+)/sprint/(?P<sprint_id>[0-9]+)/$',
        views.SprintDetailView.as_view(), name='sprint_detail'),

]