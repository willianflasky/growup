from django.db import models

# Create your models here.

class UserInfo(models.Model):

    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True)
# UserInfo.objects.crate(username=x,pwd=12)
class News(models.Model):
    title = models.CharField(max_length=64)
    img = models.CharField(max_length=128)