from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.course.api.serializer import DepartmentSerializer, PeriodAcademicSerializer, CourseSerializer, \
    CurriculumSerializer, ComponentSerializer, FileUploadSerializer
from apps.course.api.upload_csv import read_csv_courses
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

class FileUploadView(APIView):

    def post(self, request):
        # set 'data' so that you can use 'is_vaid()' and raise exception
        # if the file fails validation
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_valid(raise_exception=True)
            # once validated, grab the file from the request itself
            file = request.FILES['file']
            print(read_csv_courses(file))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
