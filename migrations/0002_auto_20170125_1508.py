# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elementy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementy',
            name='nr',
            field=models.BigIntegerField(),
        ),
    ]
