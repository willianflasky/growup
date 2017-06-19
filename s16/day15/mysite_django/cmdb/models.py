from django.db import models

# Create your models here.


# class UserInfo(models.Model):
#     user = models.CharField(max_length=32)
#     email = models.CharField(max_length=32)

class usertype(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name

class userinfo(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default="")
    email=models.EmailField()
    memo=models.TextField(default="")
    img=models.ImageField(default="")
    user_type=models.ForeignKey(usertype,null=True,blank=True)



# class B2G(models.Model):
#     boy=models.ForeignKey('Boy')
#     girl=models.ForeignKey('Girl')

class Boy(models.Model):
    name = models.CharField(max_length=32)

class Girl(models.Model):
    name = models.CharField(max_length=32)
    f=models.ManyToManyField(Boy)

