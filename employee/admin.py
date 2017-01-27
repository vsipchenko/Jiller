from django.contrib import admin

from .models import Employee, IssueLog

admin.site.register(Employee)
admin.site.register(IssueLog)
