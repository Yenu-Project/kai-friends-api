from rest_framework import routers

from app.views.viewsets import UserViewSet, UserProfileViewSet

router = routers.DefaultRouter()

router.register(
    prefix=r'users',
    viewset=UserViewSet,
)

router.register(
    prefix=r'user_profiles',
    viewset=UserProfileViewSet,
)
