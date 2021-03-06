# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_auto_20160808_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('STR', 'string'), ('INT', 'integer'), ('FLT', 'float')], default='STR', max_length=3)),
                ('units', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='DimensionValue',
            new_name='AspectValue',
        ),
        migrations.RemoveField(
            model_name='experimentaldimension',
            name='samples',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='exp_dims',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='exp_dims',
        ),
        migrations.AlterField(
            model_name='aspectvalue',
            name='expdim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dim_values', to='experiments.Aspect'),
        ),
        migrations.DeleteModel(
            name='ExperimentalDimension',
        ),
        migrations.AddField(
            model_name='aspect',
            name='samples',
            field=models.ManyToManyField(through='experiments.AspectValue', to='experiments.Sample'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='aspects',
            field=models.ManyToManyField(to='experiments.Aspect', verbose_name='aspects'),
        ),
    ]
