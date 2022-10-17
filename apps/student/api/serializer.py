from rest_framework import serializers
from apps.student.models import *


class CompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencies
        exclude = ('create_date', 'modified_date')


class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        exclude = ('create_date', 'modified_date')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        exclude = ('create_date', 'modified_date')


class LevelDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelDescription
        exclude = ('create_date', 'modified_date')


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        exclude = ('create_date', 'modified_date')
