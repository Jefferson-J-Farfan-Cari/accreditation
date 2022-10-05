from rest_framework.routers import DefaultRouter
from apps.course.api.views import DepartmentViewSet, PeriodAcademicViewSet

router = DefaultRouter()

router.register(r'api/department', DepartmentViewSet, basename="department")
router.register(r'api/period_academic', PeriodAcademicViewSet, basename="period_academic")

urlpatterns = router.urls
