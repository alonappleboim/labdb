# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0002_auto_20160807_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='data_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generating_protocols', to='data.DataType'),
        ),
        migrations.AlterField(
            model_name='protocolmodifiervalue',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='assays.ProtocolModifier'),
        ),
    ]
