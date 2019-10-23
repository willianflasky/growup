# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-10 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '评论表'},
        ),
        migrations.AlterModelOptions(
            name='favor',
            options={'verbose_name_plural': '点赞记录'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': '新闻'},
        ),
        migrations.AlterModelOptions(
            name='newstype',
            options={'verbose_name_plural': '新闻类型'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name_plural': '用户表'},
        ),
        migrations.AddField(
            model_name='news',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='favor_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='favor',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor_users', to='repository.News'),
        ),
    ]