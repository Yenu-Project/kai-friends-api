from rest_framework import serializers

from app.models import FriendDecision


class BaseFriendDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendDecision
        fields = '__all__'


class FriendDecisionSerializer(BaseFriendDecisionSerializer):
    class Meta(BaseFriendDecisionSerializer.Meta):
        fields = ['receiver', 'sender', 'receiver_decision', 'sender_decision']


class FriendDecisionCreateActionSerializer(BaseFriendDecisionSerializer):
    class Meta(BaseFriendDecisionSerializer.Meta):
        read_only_fields = (
            'sender',
            'receiver_decision',
            'finalized_at',
        )


class FriendDecisionUpdateActionSerializer(BaseFriendDecisionSerializer):
    class Meta:
        read_only_fields = (
            'sender',
            'receiver',
            'created_at',
            'sender_decision',
        )
