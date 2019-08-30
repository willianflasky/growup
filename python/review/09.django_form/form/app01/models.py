from django.db import models


# Create your models here.

class hosts(models.Model):
    ip = models.CharField(max_length=16)
    port = models.CharField(max_length=6)
