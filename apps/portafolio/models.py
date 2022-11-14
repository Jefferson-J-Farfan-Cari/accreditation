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
        return self.user_id


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
        return self.description
