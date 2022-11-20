from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.portafolio.api.serializer import *


class ProfessorViewSet(ModelViewSet):
    model = Professor
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.filter()
    filter_backends = [DjangoFilterBackend]


class TaskViewSet(ModelViewSet):
    model = Task
    serializer_class = TaskSerializer
    queryset = Task.objects.filter()
    filter_backends = [DjangoFilterBackend]


class FolderViewSet(ModelViewSet):
    model = Folder
    serializer_class = FolderSerializer
    queryset = Folder.objects.filter()
    filter_backends = [DjangoFilterBackend]


class ResourceViewSet(ModelViewSet):
    model = Resource
    serializer_class = ResourceSerializer
    queryset = Resource.objects.filter()
    filter_backends = [DjangoFilterBackend]