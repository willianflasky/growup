from django.db import models

# Create your models here.

# artical <-- user 一对多
# artical <--> author 多对多


class Artical(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField()

    user = models.ForeignKey('User')
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    sex = models.CharField(max_length=2)

    def __str__(self):
        return self.username


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=3)
    city = models.CharField(max_length=32)

    def __str__(self):
        return self.name

