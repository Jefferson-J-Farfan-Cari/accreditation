from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

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


class StageViewSet(ModelViewSet):
    model = Stage
    serializer_class = StageSerializer
    queryset = Stage.objects.filter()
    filter_backends = [DjangoFilterBackend]


class PortfolioViewSet(ModelViewSet):
    model = Portfolio
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.filter()
    filter_backends = [DjangoFilterBackend]


class CoursesByProfessorAPIView(generics.ListAPIView):
    serializer_class = CoursesByProfessorSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        period_id = self.kwargs['period_academic_id']
        data = Professor.objects.filter(user_id=user_id, period_id=period_id)
        if data.exists():
            return data.first().courses.all()
        return []


class FormViewSet(ModelViewSet):
    model = Form
    serializer_class = FormSerializer
    queryset = Form.objects.filter()
    filter_backends = [DjangoFilterBackend]