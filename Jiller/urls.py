"""Jiller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

<<<<<<< HEAD
from . import views

urlpatterns = [
    url(r'^client/', include('client.urls')),
    url(r'^employee/', include('employee.urls')),
    url(r'^workflow/', include('workflow.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
=======

urlpatterns = [
    url(r'^', include('workflow.urls')),
    url(r'^admin/', admin.site.urls),
>>>>>>> 3712ee18b35117eab69b4709571c7170abea19b6
]
