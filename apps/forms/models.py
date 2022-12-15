from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.base.models import BaseAuditingModel
from apps.course.models import Course, StudyPlan
from apps.portafolio.models import Form, Professor
from apps.student.models import Criteria, Level, StudentResult


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


class SyllabusDufaAnnexForm(BaseAuditingModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #semester = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    professors = models.ManyToManyField(Professor, blank=True, symmetrical=False)
    #competencies_studentresults = models.ManyToManyField(MatchStudentResultCompetencies, blank=True, symmetrical=False)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        db_table = 'syllabus_dufa_annex_form'
        abstract = False
        verbose_name = 'Syllabus DUFA Annex Form'
        verbose_name_plural = 'Syllabus DUFA Annex Forms'

    def __str__(self):
        return str(self.pk)


class Evaluation(BaseAuditingModel):
    name = models.CharField(max_length=120, blank=False, null=False)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'evaluation'
        abstract = False
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'

    def __str__(self):
        return self.name


class CustomCompetencie(BaseAuditingModel):
    description = models.CharField(max_length=1024, blank=True, null=True)
    syllabus_annex = models.ForeignKey(SyllabusDufaAnnexForm, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, blank=False, null=False)
    ref_student_result = models.ForeignKey(StudentResult, on_delete=models.CASCADE)
    criterias = models.ManyToManyField(Criteria, blank=True, symmetrical=False)

    class Meta:
        db_table = 'custom_competencie'
        abstract = False
        verbose_name = 'Custom Competencie'
        verbose_name_plural = 'Custom Competencies'
    
    def __str__(self):
        return str(self.pk)


class StudentResultMesure(BaseAuditingModel):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    method = models.CharField(max_length=32, blank=True, null=True)
    instant = models.CharField(max_length=60, blank=True, null=True)
    expected_percentage = models.IntegerField(blank=True, null=True)
    syllabus_annex = models.ForeignKey(SyllabusDufaAnnexForm, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sr_mesure'
        abstract = False
        verbose_name = 'Student Result Mesure'
        verbose_name_plural = 'Student Result Mesures'

    def __str__(self):
        return str(self.pk)


class RubricTable(BaseAuditingModel):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, blank=False, null=False)
    syllabus_annex = models.ForeignKey(SyllabusDufaAnnexForm, on_delete=models.CASCADE)
    evidence = models.CharField(max_length=120, blank=False, null=False)

    class Meta:
        db_table = 'rubric_table'
        abstract = False
        verbose_name = 'Rubric Table'
        verbose_name_plural = 'Rubric Tables'

    def __str__(self):
        return str(self.pk)


class RubricDetail(BaseAuditingModel):
    rubric_table = models.ForeignKey(RubricTable, on_delete=models.CASCADE)
    aspect_to_evaluate = models.CharField(max_length=512, blank=True, null=True)
    general_criteria = models.CharField(max_length=120, blank=True, null=True)
    course_criteria = models.CharField(max_length=512, blank=False, null=False)

    class Meta:
        db_table = 'rubric_detail'
        abstract = False
        verbose_name = 'Rubric Detail'
        verbose_name_plural = 'Rubrics Details'

    def __str__(self):
        return str(self.pk)


class LevelRubricDetail(BaseAuditingModel):
    description = models.CharField(max_length=512, blank=True, null=True)
    rubric_detail = models.ForeignKey(RubricDetail, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    class Meta:
        db_table = 'level_rubric_detail'
        abstract = False
        verbose_name = 'Level Rubric Detail'
        verbose_name_plural = 'Levels Rubrics Details'

    def __str__(self):
        return str(self.pk)