from django.db import models


class Dormitory(models.Model):
    dorm_en = models.CharField(max_length=64, default='')
    dorm_ko = models.CharField(max_length=64, default='')
    boy = models.BooleanField(default=False)
    girl = models.BooleanField(default=False)  # 남녀 공동 기숙사 존재 (세종관)
    undergraduate = models.BooleanField(default=False)
    graduate = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.dorm_ko
