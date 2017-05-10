from django.db import models

# Create your models here.
#   python class ---> db.table
#   python class instance ---> db.table.record
#   python class attr ---> db.table.failds


class Books(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    price = models.FloatField()
    pub_date = models.DateField()

