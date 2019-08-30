from django.db import models

# Create your models here.


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256)
    href = models.CharField(max_length=64, default=None)
    text = models.TextField(max_length=65535, default=None)
    news_type = [(1, '42区'), (2, "段子"), (3, '图片'), (4, "挨踢1024"), (5, "你问我答")]
    zone = models.IntegerField(choices=news_type)
    user = models.ForeignKey('UserInfo', related_name='u')
    ctime = models.DateTimeField(auto_now_add=True)
    favor = models.ManyToManyField('UserInfo', related_name='f')
    img = models.CharField(max_length=32, default="/static/images/1.jpg")
    source = models.CharField(max_length=32, default='unkonow')

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=128)
    user = models.ForeignKey('UserInfo', related_name='q1')
    new = models.ForeignKey('News', related_name='q2')
    ctime = models.DateTimeField(auto_now_add=True)
    parent_id = models.ForeignKey('Comment', related_name='q3')

    def __str__(self):
        return self.id
