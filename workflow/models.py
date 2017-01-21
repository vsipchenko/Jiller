from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator

from django.db import models


class Project(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    start_date = models.DateField(verbose_name=_('Start date'), auto_now_add=True)
    end_date = models.DateField(verbose_name=_('End date'), null=True, blank=True)

    def __str__(self):
        return self.title


class Sprint(models.Model):
    NEW = 'new'
    ACTIVE = 'active'
    FINISHED = 'finished'
    SPRINT_STATUS_CHOICES = (
        (NEW, _('New')),
        (ACTIVE, _('Active')),
        (FINISHED, _('Finished'))
    )
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    project = models.ForeignKey(Project)
    team = models.ForeignKey(ProjectTeam)
    start_date = models.DateField(verbose_name=_('Start date'), null=True, blank=True)
    end_date = models.DateField(verbose_name=_('End date'), null=True, blank=True)
    order = models.PositiveIntegerField(verbose_name=_('Order'), null=True, blank=True)
    status = models.CharField(verbose_name=_('Status'), choices=SPRINT_STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title


class Issue(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'in progress'
    RESOLVED = 'resolved'
    ISSUE_STATUS_CHOICES = (
        (NEW, _('New')),
        (IN_PROGRESS, _('In Progress')),
        (RESOLVED, _('Resolved'))
    )
    root = models.ForeignKey('self', null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    sprint = models.ForeignKey(Sprint, verbose_name=_('Sprint'))
    author = models.ForeignKey(User, verbose_name=_('Author'))
    employee = models.ForeignKey(User, verbose_name=_('Employee'))
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    status = models.CharField(verbose_name=_('Status'), choices=ISSUE_STATUS_CHOICES, default=NEW, null=True,
                              blank=True)
    estimation = models.PositiveIntegerField(verbose_name=_('Estimation'), validators=[MaxValueValidator(240)],
                                             null=True, blank=True)

    def __str__(self):
        return self.title


class ProjectTeam(models.Model):
    pass


class IssueLog(models.Model):
    pass
