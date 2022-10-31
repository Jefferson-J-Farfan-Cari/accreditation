from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.api.serializer import (
    UserSerializer, RoleSerializer, PermissionSerializer, CurriculumVitaeSerializer, CustomTokenObtainPairSerializer
)
from apps.user.models import User, Role, Permission, CurriculumVitae


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
    filterset_fields = ['sonPermissions', 'role']


# CurriculumVitae CRUD
class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    model = CurriculumVitae
    serializer_class = CurriculumVitaeSerializer
    queryset = CurriculumVitae.objects.filter()
    filter_backends = [DjangoFilterBackend]
