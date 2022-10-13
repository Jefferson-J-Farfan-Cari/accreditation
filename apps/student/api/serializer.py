from rest_framework import serializers
from apps.student.models import *


class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        exclude = ('create_date', 'modified_date', 'state')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        exclude = ('create_date', 'modified_date', 'state')


class LevelDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelDescription
        exclude = ('create_date', 'modified_date', 'state')


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        exclude = ('create_date', 'modified_date', 'state')
