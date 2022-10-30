from django.db import models
from apps.base.models import BaseAuditingModel
from apps.course.models import StudyPlan


class Competencies(BaseAuditingModel):
    type = models.IntegerField(unique=False, blank=False, null=False, default=1)
    name = models.CharField(max_length=60, unique=True, blank=False, null=False)
    description = models.CharField(max_length=380, unique=False, blank=False, null=False)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'competencies'
        abstract = False
        verbose_name = 'Competencies'
        verbose_name_plural = 'Competencies'

    def __str__(self):
        return self.name


class StudentResult(BaseAuditingModel):
    competencies = models.ForeignKey(Competencies, on_delete=models.CASCADE, blank=False)
    description = models.CharField(max_length=260, unique=False, blank=False, null=False)

    class Meta:
        db_table = 'student_result'
        abstract = False
        verbose_name = 'Student Result'
        verbose_name_plural = 'Student Results'

    def __str__(self):
        return self.description


class Level(BaseAuditingModel):
    name = models.CharField(max_length=100, unique=False, blank=False, null=False)
    value = models.FloatField(blank=False, null=False)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'level'
        abstract = False
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'

    def __str__(self):
        return self.name


class LevelDescription(BaseAuditingModel):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=False, null=False)
    description = models.CharField(max_length=380, unique=False, blank=False, null=False)

    class Meta:
        db_table = 'level_description'
        abstract = False
        verbose_name = 'Level Description'
        verbose_name_plural = 'Levels Descriptions'

    def __str__(self):
        return self.description


class Criteria(BaseAuditingModel):
    name = models.CharField(max_length=32, unique=False, blank=False, null=False)
    student_result = models.ForeignKey(StudentResult, on_delete=models.CASCADE, blank=False, null=False)
    levelDescription = models.ManyToManyField(LevelDescription, blank=True)
    description = models.CharField(max_length=380, unique=False, blank=False, null=False)
    levelSuggest = models.CharField(max_length=32, unique=False, blank=True)

    class Meta:
        db_table = 'criteria'
        abstract = False
        verbose_name = 'Criterion'
        verbose_name_plural = 'Criteria'

    def __str__(self):
        return self.description
