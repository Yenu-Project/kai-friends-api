from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'user']


class UserSerializer(serializers.ModelSerializer):
    userprofiles = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'userprofiles']
