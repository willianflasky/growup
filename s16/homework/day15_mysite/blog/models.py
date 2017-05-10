from django.db import models

# Create your models here.


class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    price = models.FloatField(null=True)
    pub_date = models.CharField(max_length=32)
