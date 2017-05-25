from django.db import models

# Create your models here.




class Book(models.Model):

    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)

    publisher=models.ForeignKey("Publisher") # 创建一对多

    author=models.ManyToManyField("Author")  # 创建多对多

    def __str__(self):
        return self.title

#关于一对多关系 外键在哪一张表？

class Publisher(models.Model):

    name = models.CharField(max_length=30, verbose_name="名称")
    city = models.CharField('城市', max_length=60)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):

    name=models.CharField(max_length=32)

    def __str__(self):
        return self.name




