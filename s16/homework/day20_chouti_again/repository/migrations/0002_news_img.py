# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-12 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.CharField(default='/static/images/1.jpg', max_length=32),
        ),
    ]
