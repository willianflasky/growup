# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpserver', '0006_remove_task_bind_hosts'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='timeout',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterUniqueTogether(
            name='tasklog',
            unique_together=set([('task', 'bind_host')]),
        ),
    ]
