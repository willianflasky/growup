# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jumpserver', '0007_auto_20170819_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='timeout',
        ),
    ]
