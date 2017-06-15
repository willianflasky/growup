from django.db import models


class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField()

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username
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
    url = models.CharField(max_length=128, null=True,blank=True)
    content = models.CharField(max_length=50)
    favor_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    ctime = models.DateTimeField()
    class Meta:
        verbose_name_plural = '新闻'

    def __str__(self):
        return self.title

class Favor(models.Model):
    nid = models.AutoField(primary_key=True)

    user_info = models.ForeignKey('UserInfo')
    news = models.ForeignKey('News',related_name='favor_users')

    ctime = models.DateTimeField(null=True,blank=True)

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
    device = models.CharField(max_length=16,null=True,blank=True)
    content = models.CharField(max_length=150)

    reply_id = models.ForeignKey('Comment', related_name='b', null=True, blank=True)

    class Meta:
        verbose_name_plural = '评论表'


"""
comment_list = Comment.objects.filter(news_id=1)
ID      新闻ID    用户ID       评论给内容
1         1        10           写的什么玩意呀
2         1        11           还真不是玩意
3         1        12           写的真好
4         1        11           我总算看明白了，原来是我智商低
"""



"""
ID      新闻ID    用户ID       评论给内容                             reply_id
1         1        10           写的什么玩意呀                          null
2         1        11           还真不是玩意                             1
3         1        12           写的真好                                 1
4         1        11           我总算看明白了，原来是我智商低            3
"""



# 写的什么玩意呀
#     - 还真不是玩意
#     - 写的真好
#         - 我总算看明白了，原来是我智商低
#     - sdf













