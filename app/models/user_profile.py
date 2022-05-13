from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        db_index=True,
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='사용자',
        primary_key=True,
    )
    gender = models.BooleanField(
        default=None,
        verbose_name='성별'
    )
    age = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='나이'
    )
    major = models.ForeignKey(
        to='app.Major',
        default=None,
        verbose_name='전공',
        on_delete=models.CASCADE,
    )
    degree = models.ForeignKey(
        to='app.Degree',
        default=None,
        verbose_name='학위과정',
        on_delete=models.CASCADE,
    )
    dormitory = models.ForeignKey(
        to='app.Dormitory',
        default=None,
        verbose_name='기숙사',
        on_delete=models.CASCADE,
    )
    # TODO: enable s3 storage and uncomment image
    # image = models.ImageField(
    #     null=True,
    #     blank=True,
    #     default=None,
    #     upload_to='TODO',
    #     verbose_name='프로필 이미지'
    # )
    introduction = models.CharField(
        blank=True,
        default='',
        max_length=256,
        verbose_name='자기소개'
    )
    kakao_url = models.CharField(
        blank=True,
        default='',
        max_length=256,
        verbose_name='카카오 오픈채팅 링크'
    )

    @classmethod
    def get_profiles(cls, users):
        return cls.objects.filter(user__in=list(users))
