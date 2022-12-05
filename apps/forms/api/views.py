from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.forms.api.serializer import SyllabusAbetFormSerializer
from apps.forms.models import SyllabusAbetForm


class SyllabusAbetFormViewSet(ModelViewSet):
    model = SyllabusAbetForm
    serializer_class = SyllabusAbetFormSerializer
    queryset = SyllabusAbetForm.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']
