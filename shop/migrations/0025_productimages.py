# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20170125_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='modifiedproducts/images/%Y/%m/%d')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.ModifiedProduct')),
            ],
        ),
    ]