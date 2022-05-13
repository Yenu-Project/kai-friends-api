from rest_framework import routers

from app.views.viewsets import UserViewSet, UserProfileViewSet
from app.views.viewsets.friends import FriendViewSet
from app.views.viewsets.matching import MatchingViewSet
from app.views.viewsets.friend_decision import FriendDecisionViewSet

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

router.register(
    prefix=r'friend_decisions',
    viewset=FriendDecisionViewSet,
    basename='friend_decisions'
)

router.register(
    prefix=r'friends',
    viewset=FriendViewSet,
    basename='friends'
)
