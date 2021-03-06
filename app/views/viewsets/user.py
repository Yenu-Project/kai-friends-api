from django.contrib.auth.models import User
from rest_framework import viewsets

from app.serializers.user import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewsets automatically provides `list` and `retrieve` actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
