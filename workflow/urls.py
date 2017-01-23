from django.conf.urls import url

from . import views

app_name = 'workflow'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registration/$',views.registration, name='registration')
]
