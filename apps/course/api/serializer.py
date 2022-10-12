from rest_framework import serializers
from apps.course.models import Department, PeriodAcademic, Course, Curriculum, Component


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ('create_date', 'modified_date', 'state')


class PeriodAcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodAcademic
        exclude = ('create_date', 'modified_date', 'state')


# Course Create/Update list
class CourseListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        instance_hash = {index: instance for index, instance in enumerate(instance)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]

        return result


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('create_date', 'modified_date', 'state')


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        exclude = ('create_date', 'modified_date', 'state')


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        exclude = ('create_date', 'modified_date', 'state')


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(use_url=False)
