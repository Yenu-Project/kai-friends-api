from rest_framework import serializers

from app.models.user_profile import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = ['user_id', 'username', 'email', 'user']
