from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import viewsets, views, status
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.api.serializer import (
    UserSerializer, RoleSerializer, PermissionSerializer, CurriculumVitaeSerializer, CustomTokenObtainPairSerializer
)
from apps.user.models import User, Role, Permission, CurriculumVitae
from apps.course.models import StudyPlan, Department, Course, Component
from apps.student.models import StudentResult, Level


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# User CRUD
class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend]


# Role CRUD
class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'user']


# Permission CRUD
class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['isFather', 'role']


# CurriculumVitae CRUD
class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    model = CurriculumVitae
    serializer_class = CurriculumVitaeSerializer
    queryset = CurriculumVitae.objects.filter()
    filter_backends = [DjangoFilterBackend]


# Dashboard
class DashboardViewSet(views.APIView):
    # Configuración Académica
    courses = Course.objects.all().count()
    study = StudyPlan.objects.all().count()
    department = Department.objects.all().count()
    component = Component.objects.all().count()

    result = StudentResult.objects.all().count()
    level = Level.objects.all().count()

    # print(courses, study, department, component, result, level)
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_id='Dashboard',
        operation_description='Get Dashboard information',
        manual_parameters=[
            openapi.Parameter('plan_study_id', openapi.IN_FORM, type=openapi.TYPE_NUMBER,
                              description='Id of plan study'),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'plan_study_id': openapi.Schema(type=openapi.TYPE_NUMBER, description='ID of Study Plan')
                })
            )
        }
    )
    def post(self, request):
        plan_id = request.data['plan_study_id']
        return Response({
            'summary_period': '50',
            'academic_config': '60',
            'portfolio_config': '40',
            'portfolio': '20'
        }, status=status.HTTP_200_OK)
