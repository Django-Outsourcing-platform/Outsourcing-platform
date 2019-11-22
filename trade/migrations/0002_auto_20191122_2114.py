# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-22 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='项目名称')),
                ('tag', models.CharField(max_length=20, verbose_name='标签')),
                ('content', models.CharField(max_length=200, verbose_name='项目介绍')),
                ('collection', models.IntegerField(verbose_name='收藏')),
                ('comments', models.CharField(max_length=200, verbose_name='评论')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '项目交易',
                'verbose_name_plural': '项目交易',
            },
        ),
        migrations.DeleteModel(
            name='CourseType',
        ),
    ]
