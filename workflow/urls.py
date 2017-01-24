from django.conf.urls import url

from . import views

app_name = 'workflow'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^employee/$', views.employee_index_view, name='employee-index'),
    url(r'^employee/(?P<employee_id>[0-9]+)/$', views.employee_detail_view, name='employee-detail'),
]
