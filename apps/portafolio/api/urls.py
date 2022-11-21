from rest_framework.routers import DefaultRouter

from apps.portafolio.api.views import *

router = DefaultRouter()

router.register(r'api/professor', ProfessorViewSet, basename="professor")
router.register(r'api/task', TaskViewSet, basename="task")
router.register(r'api/folder', FolderViewSet, basename="folder")
router.register(r'api/resource', ResourceViewSet, basename="resource")
router.register(r'api/stage', StageViewSet, basename="stage")
router.register(r'api/portfolio', PortfolioViewSet, basename="portfolio")

urlpatterns = router.urls
