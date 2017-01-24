from django.conf.urls import url

from . import views
from workflow.views import ProjectUpdate, ProjectCreate, ProjectDelete, ProjectDetail

app_name = 'workflow'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_form, name='login'),
    url(r'^registration/$', views.registration_form, name='registration'),

    #/project/[pr_id]/
    url(r'^project/(?P<pk>[0-9]+)/$', ProjectDetail.as_view(), name='project_detail'),

    # /project/create/
    url(r'^project/create/$', ProjectCreate.as_view(), name='project_create'),

    # /project/update/[pr_id]/
    url(r'^project/update/(?P<pk>\d+)/$', ProjectUpdate.as_view(), name='project_update'),

    # /project/update/[pr_id]/
    url(r'^project/delete/(?P<pk>\d+)/$', ProjectDelete.as_view(), name='project_delete'),
]