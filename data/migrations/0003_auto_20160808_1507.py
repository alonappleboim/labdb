# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20160808_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatype',
            name='desc',
            field=models.CharField(default='', help_text='A complete and accurate description of the file format.', max_length=2000, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datatype',
            name='s_desc',
            field=models.CharField(default='', help_text='A concise description of the file format, for quick orientation', max_length=200, verbose_name='short_description'),
            preserve_default=False,
        ),
    ]