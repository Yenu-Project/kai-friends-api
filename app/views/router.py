from rest_framework import routers

from app.views.viewsets import UserViewSet, UserProfileViewSet
from app.views.viewsets.matching import MatchingViewSet

router = routers.DefaultRouter()

router.register(
    prefix=r'users',
    viewset=UserViewSet,
    basename='users',
)

router.register(
    prefix=r'user_profiles',
    viewset=UserProfileViewSet,
    basename='user_profiles',
)

router.register(
    prefix=r'matching',
    viewset=MatchingViewSet,
    basename='matching',
)
