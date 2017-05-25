from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    publisher = models.ForeignKey("publisher")
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name="名称")
    city = models.CharField("城市", max_length=60)
    country = models.CharField(max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

