from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from apps.user.models import User, Role, Permission
from apps.user.api.serializer import (
    UserSerializer, RoleSerializer, PermissionSerializer
)


# User CRUD
class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend]


# Role CRUD
class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer

    queryset = Role.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'user']


# Permission CRUD
class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer

    queryset = Permission.objects.filter(state=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['permission_F', 'role']
