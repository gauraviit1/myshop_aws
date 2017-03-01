# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pincodes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pincode',
            name='deliveryStatus',
            field=models.CharField(default='a', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='districtName',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='officeName',
            field=models.CharField(default='a', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='stateName',
            field=models.CharField(default='a', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='taluk',
            field=models.CharField(default='a', max_length=40),
            preserve_default=False,
        ),
    ]
