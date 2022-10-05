from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from apps.course.api.serializer import DepartmentSerializer, PeriodAcademicSerializer, CourseSerializer, \
    CurriculumSerializer, ComponentSerializer
from apps.course.models import Department, PeriodAcademic, Course, Curriculum, Component


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


class CourseViewSet(ModelViewSet):
    model = Course
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department']


class CurriculumViewSet(ModelViewSet):
    model = Curriculum
    serializer_class = CurriculumSerializer
    queryset = Curriculum.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]


class ComponentViewSet(ModelViewSet):
    model = Component
    serializer_class = ComponentSerializer
    queryset = Component.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]
