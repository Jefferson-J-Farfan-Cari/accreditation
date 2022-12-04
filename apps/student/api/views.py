from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ViewSet

from apps.student.api.serializer import *


class CompetenciesViewSet(ModelViewSet):
    model = Competencies
    serializer_class = CompetenciesSerializer
    queryset = Competencies.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['study_plan', 'name', 'state']


class StudentResultViewSet(ModelViewSet):
    model = StudentResult
    serializer_class = StudentResultSerializer
    queryset = StudentResult.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['study_plan', 'name', 'state']


class LevelViewSet(ModelViewSet):
    model = Level
    serializer_class = LevelSerializer
    queryset = Level.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['study_plan', 'name', 'state']


class LevelDescriptionViewSet(ModelViewSet):
    model = LevelDescription
    serializer_class = LevelDescriptionSerializer
    queryset = LevelDescription.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['level', 'criteria']


class CriteriaViewSet(ModelViewSet):
    model = Criteria
    serializer_class = CriteriaSerializer
    queryset = Criteria.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_result']


class MatchSRCViewSet(ModelViewSet):
    model = MatchStudentResultCompetencies
    serializer_class = MatchSRCSerializer
    queryset = MatchStudentResultCompetencies.objects.filter()
    filter_backends = [DjangoFilterBackend]


class MatchCourseCompetenceViewSet(ModelViewSet):
    model = MatchCourseCompetence
    serializer_class = MatchCourseCompetenceSerializer
    queryset = MatchCourseCompetence.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['study_plan', 'course']
