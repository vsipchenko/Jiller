from django.conf.urls import url

from . import views

app_name = 'workflow'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<project_id>\w+)/issue/create/$', views.create_issue, name='create_issue'),
    url(r'^project/(?P<project_id>\w+)/issue/(?P<issue_id>\w+)/edit/$', views.edit_issue, name='edit_issue'),
    url(r'^project/(?P<project_id>\w+)/team/$', views.team, name='team'),
]