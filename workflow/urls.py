from django.conf.urls import url

from . import views

app_name = 'workflow'
urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^project/(?P<pr_id>[0-9]+)/backlog/$', views.backlog, name='backlog'),

]