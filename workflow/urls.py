from django.conf.urls import url

from . import views

app_name = 'workflow'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<pr_id>[0-9]+)/sprint/$', views.sprints_list, name='sprints_list'),

]