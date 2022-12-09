from django.db import models

from apps.base.models import BaseAuditingModel
from apps.course.models import Course
from apps.portafolio.models import Form


class SyllabusAbetForm(BaseAuditingModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text_book = models.CharField(max_length=1024, blank=True, null=True)
    supplementary_materials = models.CharField(max_length=1024, blank=True, null=True)
    subarea = models.CharField(max_length=1024, blank=True, null=True)
    brief_description = models.CharField(max_length=1024, blank=True, null=True)
    issues = models.CharField(max_length=1024, blank=True, null=True)
    lab_practical_experiences = models.CharField(max_length=1024, blank=True, null=True)
    methodology = models.CharField(max_length=1024, blank=True, null=True)
    final_note_formula = models.CharField(max_length=1024, blank=True, null=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        db_table = 'syllabus_abet_form'
        abstract = False
        verbose_name = 'Syllabus Abet Form'
        verbose_name_plural = 'Syllabus Abet Forms'

    def __str__(self):
        return str(self.pk)
