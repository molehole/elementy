# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elementy', '0003_auto_20170126_0755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elementy',
            old_name='koprus',
            new_name='korpus',
        ),
        migrations.RenameField(
            model_name='elementy',
            old_name='pinaka',
            new_name='pianka',
        ),
    ]
