from django.conf.urls import url

from . import views

app_name = 'workflow'
urlpatterns = [
<<<<<<< HEAD
    #url(r'^$', views.IndexView.as_view(), name='index'),
=======
    url(r'^', views.index, name='index'),
>>>>>>> 3712ee18b35117eab69b4709571c7170abea19b6

]