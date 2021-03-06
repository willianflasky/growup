# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20170626_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('server', '服务器'), ('networkdevice', '网络设备'), ('storagedevice', '存储设备'), ('securitydevice', '安全设备'), ('idcdevice', '机房设备'), ('accescories', '备件'), ('software', '软件资产')], default='server', max_length=64, verbose_name='资产类型'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='名字'),
        ),
    ]
