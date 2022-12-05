from rest_framework import serializers
from apps.forms.models import SyllabusAbetForm
from apps.course.api.serializer import CourseSerializer


class SyllabusAbetFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyllabusAbetForm
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['course'] = CourseSerializer(obj, many=False)
        return super(SyllabusAbetFormSerializer, self).to_representation(obj)
