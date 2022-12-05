from rest_framework.routers import DefaultRouter

from apps.forms.api.views import SyllabusAbetFormViewSet

router = DefaultRouter()

router.register(r'api/syllabus_abet_form', SyllabusAbetFormViewSet, basename="syllabus abet form")

urlpatterns = router.urls
