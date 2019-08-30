from django.db import models

# Create your models here.


class Hosts(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=32)
    port = models.CharField(max_length=6, default=22,)
    hostuser = models.CharField(max_length=16, default='root')
    hostpass = models.CharField(max_length=16, default='123456')
    bussiness = models.ForeignKey('Bussiness')
    user = models.ManyToManyField('Users')

    def __str__(self):
        return self.ip


class Bussiness(models.Model):
    bussline = models.CharField(max_length=32)

    def __str__(self):
        return self.bussline


class Users(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.username


