# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-10 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20170610_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favor',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor_users', to='repository.News'),
        ),
    ]
