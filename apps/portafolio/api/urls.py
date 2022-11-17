from rest_framework.routers import DefaultRouter

from apps.portafolio.api.views import *

router = DefaultRouter()

router.register(r'api/professor', ProfessorViewSet, basename="professor")
router.register(r'api/task', TaskViewSet, basename="task")

urlpatterns = router.urls
