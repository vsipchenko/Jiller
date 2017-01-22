from django.contrib import admin

from workflow.models import Project, Sprint, Employee, Issue, ProjectTeam

admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Employee)
admin.site.register(Issue)
admin.site.register(ProjectTeam)