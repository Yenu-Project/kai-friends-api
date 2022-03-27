from django.db import models

class Needs(models.Model):
    category = models.CharField(
        max_length=64,
        verbose_name='카테고리'
    )
    text = models.CharField(
        max_length=64,
        verbose_name='카테고리 텍스트'
    )
