# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-14 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_userinfo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='ctime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
