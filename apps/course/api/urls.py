from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.course.api.views import DepartmentViewSet, PeriodAcademicViewSet, CourseViewSet, StudyPlanViewSet, \
    ComponentViewSet, FileUploadView, CourseListView

router = DefaultRouter()

router.register(r'api/department', DepartmentViewSet, basename="department")
router.register(r'api/period_academic', PeriodAcademicViewSet, basename="period_academic")
router.register(r'api/course', CourseViewSet, basename="course")
router.register(r'api/study_plan', StudyPlanViewSet, basename="study_plan")
router.register(r'api/component', ComponentViewSet, basename="component")

urlpatterns = router.urls

urlpatterns += [
    path('api/course/file/upload_csv/', FileUploadView.as_view()),
    path('api/course/all/create/', CourseListView.as_view())
]
