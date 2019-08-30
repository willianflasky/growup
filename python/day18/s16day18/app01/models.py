from django.db import models

# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    ut = models.ForeignKey('UserType', default=2)

    def __str__(self):
        return self.username



