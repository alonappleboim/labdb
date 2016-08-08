# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 20:56
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performed_on', models.DateField(help_text='the date on which assay was perfomed', verbose_name='on')),
            ],
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=2000)),
                ('pub_url', models.URLField(blank=True, help_text='if published, link to protocol', verbose_name='publication url')),
            ],
        ),
        migrations.CreateModel(
            name='ProtocolMetaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateField(auto_now=True)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/Users/user/Dropbox/workspace/labdb/files/'), upload_to='meta/protocol/')),
                ('description', models.TextField(blank=True, max_length=2000)),
                ('attached_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_files', to='assays.Protocol')),
            ],
        ),
        migrations.CreateModel(
            name='ProtocolModifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('STR', 'string'), ('INT', 'integer'), ('FLT', 'float')], default='STR', max_length=3)),
                ('units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProtocolModifierValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string_value', models.CharField(max_length=100)),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protocol_modifier_values', to='assays.Assay')),
                ('modifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assays.ProtocolModifier')),
            ],
        ),
    ]
