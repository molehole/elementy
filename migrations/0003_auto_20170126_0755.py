# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elementy', '0002_auto_20170125_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sapimport',
            name='ackDate',
            field=models.DateField(null=True),
        ),
    ]
