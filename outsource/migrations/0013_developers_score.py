# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-16 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0012_confirm_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='developers',
            name='score',
            field=models.CharField(default='', max_length=50, verbose_name='评分'),
        ),
    ]
