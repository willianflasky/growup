from django.db import models

# Create your models here.
from django.db import models


class DePart(models.Model):
    title = models.CharField(max_length=16)


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    dp = models.ForeignKey(to="DePart", to_field="id")


class UserGroup(models.Model):
    caption = models.CharField(max_length=32)
    m = models.ManyToManyField("UserInfo")
