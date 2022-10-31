from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.base.models import BaseAuditingModel


class PeriodAcademic(BaseAuditingModel):
    year = models.CharField(max_length=4)
    period = models.CharField(max_length=1)
    status = models.BooleanField(default=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

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


class StudyPlan(BaseAuditingModel):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    description = models.CharField(max_length=200, unique=False, blank=True, null=True)

    class Meta:
        db_table = 'study_plan'
        abstract = False
        verbose_name = 'Study_Plan'
        verbose_name_plural = 'Study_Plans'

    def __str__(self):
        return self.name


class Component(BaseAuditingModel):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=1)
    description = models.CharField(max_length=200, unique=False, blank=True, null=True)

    class Meta:
        db_table = 'component'
        abstract = False
        verbose_name = 'Component'
        verbose_name_plural = 'Components'

    def __str__(self):
        return self.name


class Course(BaseAuditingModel):
    code = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    pre_requisite = models.ManyToManyField('self', blank=True, symmetrical=False)
    semester = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    elective = models.BooleanField(default=False)
    credits = models.PositiveSmallIntegerField(default=0)
    hours_theory = models.PositiveSmallIntegerField(default=0)
    hours_seminar = models.PositiveSmallIntegerField(default=0)
    hours_theopractice = models.PositiveSmallIntegerField(default=0)
    hours_practice = models.PositiveSmallIntegerField(default=0)
    hours_laboratory = models.PositiveSmallIntegerField(default=0)
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True, blank=True)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ManyToManyField(Department, blank=True, symmetrical=False)

    class Meta:
        db_table = 'course'
        abstract = False
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name
