from rest_framework.routers import DefaultRouter

from apps.forms.api.views import *

router = DefaultRouter()

router.register(r'api/syllabus_abet_form', SyllabusAbetFormViewSet, basename="syllabus abet form")
router.register(r'api/syllabus_dufa_annex_form', SyllabusDufaAnnexFormViewSet, basename="syllabus annex form")
router.register(r'api/evaluation', EvaluationViewSet, basename="evaluation")
router.register(r'api/custom_competencie', CustomCompetencieViewSet, basename="custom competencie")
router.register(r'api/student_result_mesure', StudentResultMesureViewSet, basename="student result mesure")
router.register(r'api/rubric_table', RubricTableViewSet, basename="rubric table")
router.register(r'api/rubric_detail', RubricDetailViewSet, basename="rubric detail")
router.register(r'api/level_rubric_detail', LevelRubricDetailViewSet, basename="level rubric detail")

urlpatterns = router.urls
