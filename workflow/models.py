from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator

from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    role = models.CharField(max_length=255, verbose_name=_('Role'))

    def __str__(self):
        return self.username


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
    team = models.ForeignKey('ProjectTeam')
    start_date = models.DateField(verbose_name=_('Start date'), null=True, blank=True)
    end_date = models.DateField(verbose_name=_('End date'), null=True, blank=True)
    order = models.PositiveIntegerField(verbose_name=_('Order'), null=True, blank=True)
    status = models.CharField(verbose_name=_('Status'), choices=SPRINT_STATUS_CHOICES, null=True, blank=True,
                              max_length=255)

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
    author = models.ForeignKey(Employee, verbose_name=_('Author'), related_name='author_user')
    employee = models.ForeignKey(Employee, verbose_name=_('Employee'), related_name='worker_user')
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    status = models.CharField(verbose_name=_('Status'), choices=ISSUE_STATUS_CHOICES, default=NEW, null=True,
                              blank=True, max_length=255)
    estimation = models.PositiveIntegerField(verbose_name=_('Estimation'), validators=[MaxValueValidator(240)],
                                             null=True, blank=True)

    def __str__(self):
        return self.title


class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    employees = models.ManyToManyField(Employee, verbose_name=_('Employees'))

    def __str__(self):
        return self.title


class IssueLog(models.Model):
    CREATED = 'created'
    CHANGED = 'changed'
    RESOLVED = 'resolved'
    ACTION_TYPES_CHOICES = (
        (CREATED, _('Created')),
        (CHANGED, _('Changed')),
        (RESOLVED, _('Resolved'))
    )

    issue = models.ForeignKey(Issue, verbose_name=_('Issue'))
    action = models.CharField(verbose_name=_('Action'), choices=ACTION_TYPES_CHOICES, default=CREATED, max_length=255)
    user = models.ForeignKey(Employee, verbose_name=_('Employee'))
    time = models.DateTimeField(verbose_name=_('Time'), auto_now_add=True)
    data = models.CharField(verbose_name=_('Action data'), max_length=255)

    def __str__(self):
        return "{}:{}".format(self.issue, self.action, self.user)
