from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.user.api.views import UserViewSet, RoleViewSet, PermissionViewSet

router = DefaultRouter()

router.register(r'api/user', UserViewSet, basename="user")
router.register(r'api/role', RoleViewSet, basename="role")
router.register(r'api/permission', PermissionViewSet, basename="permission")

urlpatterns = router.urls
# JWT Authentication Token
urlpatterns += [
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
