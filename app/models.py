from django.db import models


# TODO: need to replace with Django auth user
class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', related_name='userprofiles', on_delete=models.CASCADE)
    username = models.CharField(max_length=128, default='')
    email = models.CharField(max_length=128, default='')
