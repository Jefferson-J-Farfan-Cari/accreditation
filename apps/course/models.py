from django.db import models
from apps.base.models import BaseAuditingModel


class PeriodAcademic(BaseAuditingModel):
    year = models.CharField(max_length=4)
    period = models.CharField(max_length=1)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'period_academic'
        abstract = False
        verbose_name = 'Period_Academic'
        verbose_name_plural = 'Periods_Academic'

    def __str__(self):
        return f'{self.year} {self.period}'


class Department(BaseAuditingModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'department'
        abstract = False
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name
