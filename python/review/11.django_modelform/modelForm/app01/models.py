from django.db import models


# Create your models here.


class UserType(models.Model):
    caption = models.CharField(max_length=32)

    def __str__(self):
        return self.caption


class UserGroup(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey('UserType')
    u2g = models.ManyToManyField(UserGroup)

    def __str__(self):
        return self.username
