# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-18 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20161218_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='size',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='waist_size',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]