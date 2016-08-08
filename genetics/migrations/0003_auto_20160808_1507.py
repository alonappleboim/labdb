# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genetics', '0002_auto_20160808_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genotypemetafile',
            name='description',
        ),
        migrations.AddField(
            model_name='genotypemetafile',
            name='desc',
            field=models.TextField(blank=True, max_length=2000, verbose_name='description'),
        ),
    ]
