from django.conf.urls import url
from . import views

app_name = 'general'
urlpatterns = [
    url(r'^$', views.home_page_view, name='home_page'),
    url(r'^login/$', views.login_form_view, name='login'),
    url(r'^registration/$', views.registration_form_view, name='registration'),
    url(r'^profile/$', views.profile_view, name='profile'),
]
