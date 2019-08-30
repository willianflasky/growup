from django.db import models

# Create your models here.

# 抽屉表结构


# 新闻条目
class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    brief = models.CharField(max_length=200)                         # 简介
    text = models.TextField(max_length=65535)                        # 文章内容
    date_time = models.DateTimeField(default="0000-00-00 00-00-00")  # 发布时间
    img = models.CharField(default="/static/img/somebody.img")       # 配图
    be_glad = models.IntegerField(default=0)                         # 点赞
    system_type = models.CharField(max_length=32)                    # 客户端系统类型
    publish = models.ForeignKey('Users')                             # 发布用户
    title = models.ForeignKey('Title')                               # 属于新闻类型


# 42区,段子表
class Title(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


# 用户表
class Users(models.Model):
    SEX_CHOICES = ((0, 'Female'), (1, 'Male'))
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(max_length=2, choices=SEX_CHOICES)


# 聊天和私藏没想明白

