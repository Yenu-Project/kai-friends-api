from django.db import models


class Major(models.Model):
    name_en = models.CharField(max_length=64, default='')
    name_ko = models.CharField(max_length=64, default='')
    abbreviation_ko = models.CharField(max_length=64, default='')
    acronym_en = models.CharField(max_length=16, default='')

    def __str__(self) -> str:
        return self.name_ko
