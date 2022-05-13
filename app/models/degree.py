from django.db import models


class Degree(models.Model):
    degree_en = models.CharField(max_length=64, default='')
    degree_ko = models.CharField(max_length=64, default='')

    def __str__(self) -> str:
        return self.degree_ko
