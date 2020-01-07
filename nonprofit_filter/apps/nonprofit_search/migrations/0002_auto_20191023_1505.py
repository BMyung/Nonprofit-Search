# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-23 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonprofit',
            name='mission',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='nonprofit',
            name='state',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nonprofit',
            name='website',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
