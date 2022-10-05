from rest_framework.routers import DefaultRouter
from apps.course.api.views import DepartmentViewSet, PeriodAcademicViewSet, CourseViewSet, CurriculumViewSet, ComponentViewSet

router = DefaultRouter()

router.register(r'api/department', DepartmentViewSet, basename="department")
router.register(r'api/period_academic', PeriodAcademicViewSet, basename="period_academic")
router.register(r'api/course', CourseViewSet, basename="course")
router.register(r'api/curriculum', CurriculumViewSet, basename="curriculum")
router.register(r'api/component', ComponentViewSet, basename="component")

urlpatterns = router.urls