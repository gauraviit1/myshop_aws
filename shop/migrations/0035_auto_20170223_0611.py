# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 00:41
from __future__ import unicode_literals

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_auto_20170223_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modifiedproduct',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
    ]
