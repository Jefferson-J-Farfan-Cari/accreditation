from rest_framework import serializers
from apps.portafolio.models import *
from apps.user.api.serializer import UserSerializer
from apps.course.api.serializer import PeriodAcademicSerializer, CourseSerializer


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['user'] = UserSerializer(obj, many=False)
            self.fields['period'] = PeriodAcademicSerializer(obj, many=False)
            self.fields['courses'] = CourseSerializer(obj, many=True)
        return super(ProfessorSerializer, self).to_representation(obj)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['user'] = UserSerializer(obj, many=False)
        return super(TaskSerializer, self).to_representation(obj)
