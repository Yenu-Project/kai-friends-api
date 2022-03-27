from django.db import models

from django.conf import settings


class ProfileImage(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                primary_key=True)

    picture = models.ImageField(
        null=True,
        blank=True,
        default=None,
        upload_to='user_profiles/pictures',
        verbose_name='프로필',
    )
