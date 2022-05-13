from django.core.paginator import Paginator

from app.models import FriendDecision
from rest_framework import viewsets, permissions, mixins

from app.models.user_profile import UserProfile
from app.serializers.user_profile import UserProfileSerializer


class MatchingViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # user proflie의 사용자 중 decisions table을 조회해서 내가 sender도 receiver도 아닌 사용자들 찾아옴
    # user id가 FriendDecision의 sender와 receiver에 없는 경우
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def filter_queryset(self, queryset):
        received_friend = FriendDecision.objects.filter(receiver_id=self.request.user.id).values_list('sender_id', flat=True)
        sent_friend = FriendDecision.objects.filter(sender_id=self.request.user.id).values_list('receiver_id', flat=True)

        excludes = [self.request.user.id, *received_friend, *sent_friend]
        queryset = queryset.exclude(user_id__in=excludes)
        return queryset
