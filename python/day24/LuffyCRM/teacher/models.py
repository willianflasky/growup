from django.db import models

# Create your models here.


class TeacherTest(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name