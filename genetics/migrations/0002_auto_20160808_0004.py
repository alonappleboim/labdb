# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 21:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genetics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genotype',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genotypes_added', to=settings.AUTH_USER_MODEL),
        ),
    ]