from rest_framework.routers import DefaultRouter

from apps.student.api.views import *

router = DefaultRouter()

router.register(r'api/competencies', CompetenciesViewSet, basename="competencies")
router.register(r'api/student_result', StudentResultViewSet, basename="student_result")
router.register(r'api/level', LevelViewSet, basename="level")
router.register(r'api/level_description', LevelDescriptionViewSet, basename="level_description")
router.register(r'api/criteria', CriteriaViewSet, basename="criteria")
router.register(r'api/match', MatchSRCViewSet, basename="match")
router.register(r'api/match_course_competence', MatchCourseCompetenceViewSet, basename="match_course_competence")

urlpatterns = router.urls
