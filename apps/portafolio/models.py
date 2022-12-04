from django.db import models
from apps.base.models import BaseAuditingModel
from apps.user.models import User
from apps.course.models import PeriodAcademic, Course


class Professor(BaseAuditingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    period = models.ForeignKey(PeriodAcademic, on_delete=models.CASCADE, blank=False, null=False)
    courses = models.ManyToManyField(Course, blank=True, symmetrical=False)

    class Meta:
        db_table = 'professor'
        abstract = False
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        return str(self.user_id)


class Task(BaseAuditingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    description = models.CharField(max_length=300, unique=False, blank=True, null=True)
    init_date = models.DateField('Initial Date')
    limit_date = models.DateField('Limit Date')

    class Meta:
        db_table = 'task'
        abstract = False
        verbose_name = 'Task'
        verbose_name_plural = 'Task'

    def __str__(self):
        return str(self.description)


class Stage(BaseAuditingModel):
    name = models.CharField(max_length=120, unique=False, blank=False, null=False)
    period_academic = models.ForeignKey(PeriodAcademic, on_delete=models.CASCADE, blank=False, null=False)
    initial_date = models.DateField('Initial Date')
    limit_date = models.DateField('Limit Date')
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'stage'
        abstract = False
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'

    def __str__(self):
        return str(self.name)


class Folder(BaseAuditingModel):
    name = models.CharField(max_length=120, unique=False, blank=False, null=False)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        db_table = 'folder'
        abstract = False
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'

    def __str__(self):
        return str(self.name)


class Resource(BaseAuditingModel):
    period_academic = models.ForeignKey(PeriodAcademic, on_delete=models.CASCADE, blank=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=False, null=False)
    type = models.BooleanField(default=True)

    class Meta:
        db_table = 'resource'
        abstract = False
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return str(self.pk)


class Portfolio(BaseAuditingModel):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'portfolio'
        abstract = False
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return str(self.pk)


class Form(BaseAuditingModel):
    name = models.CharField(max_length=120, unique=False, blank=False, null=False)
    path = models.CharField(max_length=200, unique=True, blank=False, null=False)
    state = models.BooleanField(default=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        db_table = 'form'
        abstract = False
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'

    def __str__(self):
        return self.name
