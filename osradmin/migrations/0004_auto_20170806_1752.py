# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-06 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osradmin', '0003_auto_20170806_1416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAdd',
            new_name='Membre',
        ),
        migrations.RenameField(
            model_name='membre',
            old_name='Biographie',
            new_name='biographie',
        ),
    ]
