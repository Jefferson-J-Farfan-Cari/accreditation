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
from apps.course.models import StudyPlan, Department, Course, Component, PeriodAcademic
from apps.student.models import StudentResult, Level, Competencies
from apps.portafolio.models import Stage, Folder, Form, Professor
from apps.forms.models import SyllabusAbetForm


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
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_id='Dashboard',
        operation_description='Get Dashboard information',
        manual_parameters=[
            openapi.Parameter('period_id', openapi.IN_FORM, type=openapi.TYPE_INTEGER,
                              description='Period academic'),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'summary_period': openapi.Schema(type=openapi.TYPE_NUMBER, description='Porcentaje general'),
                    'academic_config': openapi.Schema(type=openapi.TYPE_NUMBER, description='Conf. académica'),
                    'portfolio_config': openapi.Schema(type=openapi.TYPE_NUMBER, description='Conf. portafolio'),
                    'portfolio': openapi.Schema(type=openapi.TYPE_NUMBER, description='Portafolio')
                })
            )
        }
    )
    def post(self, request):
        period = request.data['period_id']

        # Configuración Académica
        count = 0
        count += 1 if Competencies.objects.all().count() >= 1 else 0
        count += 1 if StudyPlan.objects.all().count() >= 1 else 0
        count += 1 if Department.objects.all().count() >= 1 else 0
        count += 1 if Component.objects.all().count() >= 1 else 0
        count += 1 if Course.objects.all().count() >= 1 else 0

        count += 1 if Level.objects.all().count() >= 1 else 0
        count += 1 if StudentResult.objects.all().count() >= 1 else 0

        academic_config = int((100 * count) / 7)

        # Portafolio Config
        counter, aux1, aux2 = 0, 0, 0

        counter += 1 if PeriodAcademic.objects.all().count() >= 1 else 0
        counter += 1 if Stage.objects.filter(period_academic=period).count() >= 1 else 0

        aux1 = Folder.objects.raw('SELECT * FROM folder '
                                  'INNER JOIN stage s on folder.stage_id = s.id '
                                  'WHERE s.period_academic_id = %s', period)
        aux2 = Form.objects.raw('SELECT * FROM form '
                                'INNER JOIN folder f on f.id = form.folder_id '
                                'INNER JOIN stage s on f.stage_id = s.id '
                                'WHERE s.period_academic_id = %s', period)

        counter += 1 if Professor.objects.filter(period=period).count() >= 1 else 0
        counter += 1 if len(aux1) >= 1 else 0
        counter += 1 if len(aux2) >= 1 else 0

        portfolio_config = int((100 * counter) / 5)

        forms1, forms2, course_count = 0, 0, 0

        forms1 = SyllabusAbetForm.objects.raw('SELECT * FROM syllabus_abet_form '
                                              'inner join course c on c.code = syllabus_abet_form.course_id '
                                              'inner join professor_courses pc on c.code = pc.course_id '
                                              'inner join professor p on pc.professor_id = p.id '
                                              'where p.period_id = %s', period)

        course_count = Course.objects.raw('SELECT * FROM course '
                                          'INNER JOIN professor_courses pc on course.code = pc.course_id '
                                          'INNER JOIN professor p on pc.professor_id = p.id '
                                          'WHERE p.period_id = %s', period)

        portafolio = ((len(forms1) + forms2) * 100) / (len(course_count) * 2) if len(course_count) >= 1 else 0

        return Response({
            'summary_period': int((academic_config + portfolio_config + portafolio) / 3),
            'academic_config': academic_config,
            'portfolio_config': portfolio_config,
            'portfolio': portafolio
        }, status=status.HTTP_200_OK)
