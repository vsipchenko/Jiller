from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
    pass


class Sprint(models.Model):
    pass


class Issue(models.Model):
    pass


class ProjectTeam(models.Model):
    pass


class Employee(AbstractUser):
    role = models.CharField(max_length=255)


class IssueLog(models.Model):
    pass

