from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from apps.student.models import *
from apps.student.api.serializer import *


class StudentResultViewSet(ModelViewSet):
    model = StudentResult
    serializer_class = StudentResultSerializer
    queryset = StudentResult.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]


class LevelViewSet(ModelViewSet):
    model = Level
    serializer_class = LevelSerializer
    queryset = Level.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]


class LevelDescriptionViewSet(ModelViewSet):
    model = LevelDescription
    serializer_class = LevelDescriptionSerializer
    queryset = LevelDescription.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['level']


class CriteriaViewSet(ModelViewSet):
    model = Criteria
    serializer_class = CriteriaSerializer
    queryset = Criteria.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]
