from rest_framework import viewsets

from app.models.user_profile import UserProfile
from app.serializers.user_profile import UserProfileSerializer, UserProfileCreateActionSerializer, \
    UserProfileUpdateActionSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    This viewsets automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    action_serializer_class = {
        'create': UserProfileCreateActionSerializer,
        'update': UserProfileUpdateActionSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
