# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-10 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20170610_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favor',
            name='ctime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]