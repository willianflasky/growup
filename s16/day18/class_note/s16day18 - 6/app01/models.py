from django.db import models


class UserType(models.Model):
    name = models.CharField(max_length=32)


class UserInfo(models.Model):

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=32)
    ut = models.ForeignKey("UserType",default=2)
