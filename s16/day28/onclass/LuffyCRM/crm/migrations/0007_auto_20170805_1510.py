# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 07:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20170805_1223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': (('crm_table_index', '可以查看所有的luffyadmin的app'), ('crm_table_list', '可以查看每张表里所有的数据'), ('crm_table_list_view', '可以访问表里每条数据的修改页'), ('crm_table_list_change', '可以对表里的每条数据进行修改'))},
        ),
    ]
