from django.db import models

# Create your models here.

class UserInfo(models.Model):

    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)