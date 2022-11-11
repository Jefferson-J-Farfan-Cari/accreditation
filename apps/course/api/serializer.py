from rest_framework import serializers
from apps.course.models import Department, PeriodAcademic, Course, StudyPlan, Component


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ('create_date', 'modified_date')


class PeriodAcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodAcademic
        exclude = ('create_date', 'modified_date')


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
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['component'] = ComponentSerializer(obj, many=False)
            self.fields['study_plan'] = StudyPlanSerializer(obj, many=False)
        return super(CourseSerializer, self).to_representation(obj)


class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        exclude = ('create_date', 'modified_date')


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        exclude = ('create_date', 'modified_date')


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(use_url=False)
