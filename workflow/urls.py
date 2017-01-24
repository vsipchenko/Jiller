from django.conf.urls import url

from . import views

app_name = 'workflow'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_form, name='login'),
    url(r'^registration/$', views.registration_form, name='registration'),
]