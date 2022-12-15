from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.forms.api.serializer import *
from apps.forms.models import *


class SyllabusAbetFormViewSet(ModelViewSet):
    model = SyllabusAbetForm
    serializer_class = SyllabusAbetFormSerializer
    queryset = SyllabusAbetForm.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']


class SyllabusDufaAnnexFormViewSet(ModelViewSet):
    model = SyllabusDufaAnnexForm
    serializer_class = SyllabusDufaAnnexFormSerializer
    queryset = SyllabusDufaAnnexForm.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'professors', 'form']


class EvaluationViewSet(ModelViewSet):
    model = Evaluation
    serializer_class = EvaluationSerializer
    queryset = Evaluation.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['study_plan']


class CustomCompetencieViewSet(ModelViewSet):
    model = CustomCompetencie
    serializer_class = CustomCompetencieSerializer
    queryset = CustomCompetencie.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['syllabus_annex', 'evaluation', 'ref_student_result', 'criterias']


class StudentResultMesureViewSet(ModelViewSet):
    model = StudentResultMesure
    serializer_class = StudenResultMesureSerializer
    queryset = StudentResultMesure.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['criteria', 'syllabus_annex']


class RubricTableViewSet(ModelViewSet):
    model = RubricTable
    serializer_class = RubricTableSerializer
    queryset = RubricTable.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evaluation', 'syllabus_annex']


class RubricDetailViewSet(ModelViewSet):
    model = RubricDetail
    serializer_class = RubricDetailSerializer
    queryset = RubricDetail.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rubric_table']


class LevelRubricDetailViewSet(ModelViewSet):
    model = LevelRubricDetail
    serializer_class = LevelRubricDetailSerializer
    queryset = LevelRubricDetail.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rubric_detail', 'level']