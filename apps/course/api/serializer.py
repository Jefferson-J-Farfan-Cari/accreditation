from rest_framework import serializers
from apps.course.models import Department, PeriodAcademic


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ('create_date', 'modified_date', 'state')


class PeriodAcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodAcademic
        exclude = ('create_date', 'modified_date', 'state')
