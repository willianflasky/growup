# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20170807_0538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': (('luffyadmin_table_index', '可以查看所有的luffyadmin的APP'), ('luffyadmin_table_list', '查看每张表的数据'), ('luffyadmin_table_list_view', '查看每条数据的修改页'), ('luffyadmin_table_list_change', '修改每条数据'))},
        ),
    ]
