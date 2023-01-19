from rest_framework import serializers
from apps.forms.models import *
from apps.portafolio.api.serializer import ProfessorSerializer, FormSerializer
from apps.course.api.serializer import CourseSerializer, StudyPlanSerializer
from apps.student.api.serializer import StudentResultSerializer, CriteriaSerializer, LevelSerializer


class SyllabusAbetFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyllabusAbetForm
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['course'] = CourseSerializer(obj, many=False)
        return super(SyllabusAbetFormSerializer, self).to_representation(obj)


class SyllabusDufaAnnexFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyllabusDufaAnnexForm
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['course'] = CourseSerializer(obj, many=False)
            self.fields['professors'] = ProfessorSerializer(obj, many=True)
            self.fields['form'] = FormSerializer(obj, many=False)
        return super(SyllabusDufaAnnexFormSerializer, self).to_representation(obj)


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['study_plan'] = StudyPlanSerializer(obj, many=False)
        return super(EvaluationSerializer, self).to_representation(obj)


class CustomCompetencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomCompetencie
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['syllabus_annex'] = SyllabusDufaAnnexFormSerializer(obj, many=False)
            self.fields['evaluation'] = EvaluationSerializer(obj, many=False)
            self.fields['ref_student_result'] = StudentResultSerializer(obj, many=False)
            self.fields['criterias'] = CriteriaSerializer(obj, many=True)
        return super(CustomCompetencieSerializer, self).to_representation(obj)


class StudenResultMesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResultMesure
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['criteria'] = CriteriaSerializer(obj, many=False)
            self.fields['syllabus_annex'] = SyllabusDufaAnnexFormSerializer(obj, many=False)
        return super(StudenResultMesureSerializer, self).to_representation(obj)


class RubricTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubricTable
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['evaluation'] = EvaluationSerializer(obj, many=False)
            self.fields['syllabus_annex'] = SyllabusDufaAnnexFormSerializer(obj, many=False)
        return super(RubricTableSerializer, self).to_representation(obj)


class RubricDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubricDetail
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['rubric_table'] = RubricTableSerializer(obj, many=False)
        return super(RubricDetailSerializer, self).to_representation(obj)


class LevelRubricDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelRubricDetail
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['rubric_detail'] = RubricDetailSerializer(obj, many=False)
            self.fields['level'] = LevelSerializer(obj, many=False)
        return super(LevelRubricDetailSerializer, self).to_representation(obj)