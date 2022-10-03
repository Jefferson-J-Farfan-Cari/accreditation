from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from apps.user.models import User, Role, Permission
from apps.user.api.serializer import (
    UserSerializer, UserListSerializer, UpdateUserSerializer,
    RoleSerializer, PermissionSerializer
)


# User CRUD
class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        filter_val = self.request.GET.get('email', '')
        if self.queryset is None:
            self.queryset = self.model.objects \
                .filter(is_active=True) \
                .values('id', 'username', 'email', 'name', 'last_name', 'image_user', 'role')
        if filter_val:
            return self.queryset.filter(email=filter_val)
        else:
            return self.queryset

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        if users.count() != 1:
            return Response(users_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Este email ya ha sido registrado.'}, status=status.HTTP_409_CONFLICT)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)


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
