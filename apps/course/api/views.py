from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from apps.course.api.serializer import DepartmentSerializer, PeriodAcademicSerializer
from apps.course.models import Department, PeriodAcademic


class DepartmentViewSet(ModelViewSet):
    model = Department
    serializer_class = DepartmentSerializer
    queryset = Department.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]


class PeriodAcademicViewSet(ModelViewSet):
    model = PeriodAcademic
    serializer_class = PeriodAcademicSerializer
    queryset = PeriodAcademic.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]
