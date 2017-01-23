from django.conf.urls import url

from . import views
from workflow.views import ProjectDetail, ProjectCreate

app_name = 'workflow'
urlpatterns = [
    url(r'^', views.index, name='index'),

    #/project/[pr_id]/
    url(r'^/project/(?P<project_id>[0-9]+)/$', ProjectDetail.as_view(), name='project_detail'),

    # /project/create/
    url(r'^/project/create/$', ProjectCreate.as_view(), name='project_create'),

    # /project/update/[pr_id]/
    #url(r'^/project/update/(?P<project_id>[0-9]+)/$', views.project_update, name='project_update'),

]
