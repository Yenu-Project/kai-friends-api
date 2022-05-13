from app.models import FriendDecision
from rest_framework import viewsets, permissions
from app.models.user_profile import UserProfile
from app.serializers.user_profile import UserProfileSerializer

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def filter_queryset(self, queryset):
        received_friend = FriendDecision.objects.filter(receiver_id=self.request.user.id).values_list('sender_id', flat=True)
        queryset = queryset.filter(user_id__in=received_friend).exclude(user_id=self.request.user.id)
        return queryset
