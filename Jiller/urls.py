from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('general.urls', namespace='general')),
    url(r'^employee/', include('employee.urls', namespace='employee')),
    url(r'^project/', include('project.urls', namespace='project'))
]
