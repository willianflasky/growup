from django.db import models

# Create your models here.

#ORM：对象关系映射      python的类------------数据表
#                      python的类实例------------表的记录
#                      python的类属性------------表的字段



class Books(models.Model):

    title=models.CharField(max_length=32)
    author=models.CharField(max_length=32)
    price=models.FloatField(null=True)
    pub_date=models.DateField(null=True)



