from rest_framework.routers import DefaultRouter

from apps.user.api.views import UserViewSet, RoleViewSet, PermissionViewSet

router = DefaultRouter()

router.register(r'api/user', UserViewSet, basename="user")
router.register(r'api/role', RoleViewSet, basename="role")
router.register(r'api/permission', PermissionViewSet, basename="permission")

urlpatterns = router.urls
