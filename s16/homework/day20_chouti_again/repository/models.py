from django.db import models

# Create your models here.


class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField()
    img = models.CharField(max_length=32, default="/static/images/1.jpg")

    class Meta:
        verbose_name_plural = '用户表'    # 在django中显示表名称

    def __str__(self):
        return self.username
        # 显示字段对象名称


class NewsType(models.Model):
    nid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "新闻类型"

    def __str__(self):
        return self.caption


class News(models.Model):
    nid = models.AutoField(primary_key=True)
    user_info = models.ForeignKey('UserInfo')
    news_type = models.ForeignKey('NewsType')
    title = models.CharField(max_length=32, db_index=True)
    url = models.CharField(max_length=128, null=True, blank=True)
    content = models.CharField(max_length=50)
    favor_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    ctime = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=32, default="/static/images/1.jpg")

    class Meta:
        verbose_name_plural = '新闻'

    def __str__(self):
        return self.title


class Favor(models.Model):
    nid = models.AutoField(primary_key=True)
    user_info = models.ForeignKey('UserInfo')
    news = models.ForeignKey('News')
    ctime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}<{1}>".format(self.news.title, self.user_info.username)

    class Meta:
        verbose_name_plural = '点赞记录'
        unique_together = (
            ("user_info", "news"),
        )


class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    user_info = models.ForeignKey('UserInfo')
    news = models.ForeignKey('News')
    ctime = models.DateTimeField()
    device = models.CharField(max_length=16, null=True, blank=True)
    content = models.CharField(max_length=150)
    reply_id = models.ForeignKey('Comment', related_name='b', null=True, blank=True)

    class Meta:
        verbose_name_plural = '评论表'

