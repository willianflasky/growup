from django.db import models

# Create your models here.

class UserType(models.Model):
    catption=models.CharField(max_length=32)

class UserInfo(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    user_type=models.ForeignKey('UserType')

