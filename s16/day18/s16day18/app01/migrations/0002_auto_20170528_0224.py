# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-28 02:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='UserInfo',
        ),
    ]
