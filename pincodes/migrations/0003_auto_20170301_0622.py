# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pincodes', '0002_auto_20170301_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pincode',
            name='stateName',
            field=models.CharField(max_length=30),
        ),
    ]
