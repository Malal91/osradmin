# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-06 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osradmin', '0004_auto_20170806_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membre',
            name='newsletter',
        ),
    ]
