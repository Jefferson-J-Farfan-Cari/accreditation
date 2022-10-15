from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.course.api.serializer import DepartmentSerializer, PeriodAcademicSerializer, CourseSerializer, \
    StudyPlanSerializer, ComponentSerializer, FileUploadSerializer
from apps.course.api.upload_csv import read_csv_courses
from apps.course.models import Department, PeriodAcademic, Course, StudyPlan, Component


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


class StudyPlanViewSet(ModelViewSet):
    model = StudyPlan
    serializer_class = StudyPlanSerializer
    queryset = StudyPlan.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]


class ComponentViewSet(ModelViewSet):
    model = Component
    serializer_class = ComponentSerializer
    queryset = Component.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]


class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.filter(state=True)
    serializer_class = CourseSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(CourseListView, self).get_serializer(*args, **kwargs)



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
