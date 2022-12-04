from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser
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
    queryset = Department.objects.filter()
    filter_backends = [DjangoFilterBackend]


class PeriodAcademicViewSet(ModelViewSet):
    model = PeriodAcademic
    serializer_class = PeriodAcademicSerializer
    queryset = PeriodAcademic.objects.filter()
    filter_backends = [DjangoFilterBackend]


class CourseViewSet(ModelViewSet):
    model = Course
    serializer_class = CourseSerializer
    queryset = Course.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'study_plan', 'state', 'name', 'name_en']


class StudyPlanViewSet(ModelViewSet):
    model = StudyPlan
    serializer_class = StudyPlanSerializer
    queryset = StudyPlan.objects.filter()
    filter_backends = [DjangoFilterBackend]


class ComponentViewSet(ModelViewSet):
    model = Component
    serializer_class = ComponentSerializer
    queryset = Component.objects.filter()
    filter_backends = [DjangoFilterBackend]


class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.filter()
    serializer_class = CourseSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(CourseListView, self).get_serializer(*args, **kwargs)


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_id='Upload Courses from a csv file',
        operation_description='Create a list of courses of a study plan (2013, 2017, 2021, ...) from csv file',
        manual_parameters=[
            openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='CSV to be uploaded'),
            openapi.Parameter('plan_study_id', openapi.IN_FORM, type=openapi.TYPE_NUMBER,
                              description='Id of plan study'),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'file': openapi.Schema(type=openapi.TYPE_STRING, description='Name of csv file')
                })
            )
        }
    )
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)

        if request.data['plan_study_id'] is None:
            return Response({
                    'message': 'plan_study_id were not provided'
                }, status=status.HTTP_400_BAD_REQUEST)
        if len(StudyPlan.objects.filter(pk=request.data['plan_study_id'])) == 0:
            return Response({
                    'message': 'plan_study_id not found'
                }, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.is_valid(raise_exception=True)
            file = request.FILES['file']
            study_plan = request.data['plan_study_id']

            read_csv_courses(file, study_plan)

            return Response(
                {
                    'message': 'The file was submitted correctly',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
