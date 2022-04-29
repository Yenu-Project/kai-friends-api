from django.db import models
from django.utils import timezone
from django.conf import settings


class FriendDecision(models.Model):
    sender = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        db_index=True,
        related_name='sent_decisions',
        on_delete=models.CASCADE,
        verbose_name='보낸 사람',
    )

    receiver = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        db_index=True,
        related_name='received_decisions',
        on_delete=models.CASCADE,
        verbose_name='받은 사람',
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='생성 시간',
    )

    finalized_at = models.DateTimeField(
        default=timezone.datetime.min.replace(tzinfo=timezone.utc),
        verbose_name='신청 받은 사람의 결정 시간',
    )

    receiver_decision = models.BooleanField(
        verbose_name='친구 신청 수락 여부',
        default=False,
    )

    sender_decision = models.BooleanField(
        verbose_name='친구 신청 여부',
        default=False,
    )
