from django.db import models

class DePart(models.Model):
    title = models.CharField(max_length=16)

class UserInfo(models.Model):

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    dp = models.ForeignKey(to="DePart",to_field="id") # dp_id
    # m = models.ManyToManyField("UserGroup")

class UserGroup(models.Model):
    caption = models.CharField(max_length=32)
    m = models.ManyToManyField("UserInfo")



# class U2G(models.Model):
#     ui = models.ForeignKey("UserInfo")
#     ug = models.ForeignKey('UserGroup')
    # count = models.IntegerField()

# 3. 创建多对多关系
# U2G.objects.create(ui_id=1,ug_id=2)
# U2G.objects.create(ui_id=2,ug_id=2)
# U2G.objects.create(ui_id=3,ug_id=1)
# q = U2G.objects.all()
# for row in q:
#     row.ui.username
#     row.ug.caption



# 1. 获取用户所有信息,部门名称
# q = UserInfo.objects.all()
# [obj(username,password,obj(id,title),dp_id),]
# for row in q:
#     print(row.username,row.password,row.dp_id,row.dp.id,row.dp.title)
# 2. 获取用户所有信息,部门名称, values
# q = UserInfo.objects.values('username','password',"dp_id","dp__title")
