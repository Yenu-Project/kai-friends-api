from django.contrib.auth.models import User
from rest_framework import serializers

from app.models.user_profile import UserProfile


class UserSerializer(serializers.ModelSerializer):
    userprofiles = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'userprofiles']
