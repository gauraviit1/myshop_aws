# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 08:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_product_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
