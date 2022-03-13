from rest_framework import permissions, viewsets

from app.models.user_profile import UserProfile
from app.permissions import IsOwnerOrReadOnly
from app.serializers.user_profile import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
