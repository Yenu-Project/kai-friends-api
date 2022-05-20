from django.core.paginator import Paginator

from app.models import FriendDecision
from rest_framework import viewsets, permissions, mixins

from app.models.user_profile import UserProfile
from app.serializers.user_profile import UserProfileSerializer


class FriendViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def filter_queryset(self, queryset):
        friends = FriendDecision.get_friends(self.request.user)
        # TODO: ordering (recent friends first. 현재 상태에서 하려면 join이 과도하게 필요해서 생략)
        # TODO: ordering 하기 위해서는 friend table 따로 만드는 것이 좋을 듯
        return UserProfile.get_profiles(friends).order_by('user')
