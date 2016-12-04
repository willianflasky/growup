# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='img',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='memo',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='nid',
            field=models.AutoField(default='', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
