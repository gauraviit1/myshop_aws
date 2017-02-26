# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_auto_20170223_0611'),
        ('orders', '0002_remove_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.ModifiedProduct'),
        ),
    ]
