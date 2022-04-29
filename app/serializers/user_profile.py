from rest_framework import serializers

from app.models.user_profile import UserProfile


class BaseUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSerializer(BaseUserProfileSerializer):
    class Meta(BaseUserProfileSerializer.Meta):
        pass


class UserProfileCreateActionSerializer(BaseUserProfileSerializer):
    class Meta(BaseUserProfileSerializer.Meta):
        pass


class UserProfileUpdateActionSerializer(BaseUserProfileSerializer):
    class Meta(BaseUserProfileSerializer.Meta):
        pass
