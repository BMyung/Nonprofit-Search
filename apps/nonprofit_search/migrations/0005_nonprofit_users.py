# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-24 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit_login', '0002_auto_20191023_1737'),
        ('nonprofit_search', '0004_auto_20191023_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonprofit',
            name='users',
            field=models.ManyToManyField(related_name='nonprofits', to='nonprofit_login.User'),
        ),
    ]
