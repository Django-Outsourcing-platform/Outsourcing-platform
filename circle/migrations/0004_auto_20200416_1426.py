# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-16 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0003_auto_20200225_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-created_time'], 'verbose_name': '帖子评论', 'verbose_name_plural': '帖子评论'},
        ),
    ]
