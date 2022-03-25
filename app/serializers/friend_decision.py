from rest_framework import serializers

from app.models.user_profile import UserProfile


class FriendDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['receiver_id', 'sender_id', 'receiver_decision', 'sender_decision']

