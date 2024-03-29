from rest_framework import serializers
from apps.student.models import *
from apps.course.api.serializer import CourseSerializer


class CompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencies
        exclude = ('create_date', 'modified_date')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        exclude = ('create_date', 'modified_date')


class LevelDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelDescription
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['level'] = LevelSerializer(obj, many=False)
            self.fields['criteria'] = CriteriaSerializer(obj, many=False)
        return super(LevelDescriptionSerializer, self).to_representation(obj)


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        exclude = ('create_date', 'modified_date')


class StudentResultSerializer(serializers.ModelSerializer):
    criteria = CriteriaSerializer(many=True)

    class Meta:
        model = StudentResult
        exclude = ('create_date', 'modified_date')

    def create(self, validated_data):
        criteria_data = validated_data.pop('criteria')
        student_result = StudentResult.objects.create(**validated_data)
        for track_data in criteria_data:
            Criteria.objects.create(student_result=student_result, **track_data)
        return student_result


class MatchSRCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchStudentResultCompetencies
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['competences'] = CompetenciesSerializer(obj, many=False)
        return super(MatchSRCSerializer, self).to_representation(obj)


class MatchCourseCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchCourseCompetence
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['course'] = CourseSerializer(obj, many=False)
            self.fields['competencies'] = CompetenciesSerializer(obj, many=False)
        return super(MatchCourseCompetenceSerializer, self).to_representation(obj)
