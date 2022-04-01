from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=16, default='')
    name_en = models.CharField(max_length=64, default='')
    name_ko = models.CharField(max_length=64, default='')
