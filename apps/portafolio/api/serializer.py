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


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        #if 'branches' not in self.fields:
            #self.fields['stage'] = StageSerializer(obj, many=False)
        return super(FolderSerializer, self).to_representation(obj)


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['period_academic'] = PeriodAcademicSerializer(obj, many=False)
            self.fields['course'] = CourseSerializer(obj, many=False)
            self.fields['follder'] = FolderSerializer(obj, many=False)
        return super(ResourceSerializer, self).to_representation(obj)


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['period_academic'] = PeriodAcademicSerializer(obj, many= False)
        return super(StageSerializer, self).to_representation(obj)