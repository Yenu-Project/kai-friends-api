from rest_framework import routers

from app.views.viewsets import UserViewSet, UserProfileViewSet
from app.views.viewsets.friend_decision import FriendDecisionViewSet

router = routers.DefaultRouter()

router.register(
    prefix=r'users',
    viewset=UserViewSet,
)

router.register(
    prefix=r'user_profiles',
    viewset=UserProfileViewSet,
)

router.register(
    prefix=r'friend_decisions',
    viewset=FriendDecisionViewSet,
)
