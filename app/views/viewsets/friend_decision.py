from rest_framework import viewsets
from django.utils import timezone

from app.models import FriendDecision
from app.serializers.friend_decision import FriendDecisionCreateActionSerializer, FriendDecisionSerializer, \
    FriendDecisionUpdateActionSerializer
from django.contrib.auth.models import User


class FriendDecisionViewSet(viewsets.ModelViewSet):
    queryset = FriendDecision.objects.all()
    serializer_class = FriendDecisionSerializer
    action_serializer_class = {
        'create': FriendDecisionCreateActionSerializer,
        'update': FriendDecisionUpdateActionSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user,
                        receiver=User.objects.get(pk=self.request.data['receiver']),
                        sender_decision=bool(self.request.data.get('sender_decision', False)),
                        )

    def perform_update(self, serializer):
        serializer.save(
            receiver_decision=bool(self.request.data.get('receiver_decision', False)),
            finalized_at=timezone.now(),  # replace with MetaDataModel
        )

        return super().perform_update(serializer)
