from django.db import models
from django.conf import settings

class FriendPreference(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        db_index=True,
        related_name='preferences',
        on_delete=models.CASCADE,
        verbose_name='사용자',
    )
    needs = models.ForeignKey(
        to='app.Needs',
        verbose_name='사용자 니즈',
        on_delete=models.CASCADE,
    )
