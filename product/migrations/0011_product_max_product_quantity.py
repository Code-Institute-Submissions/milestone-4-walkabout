# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-16 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_is_single_use_only'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='max_product_quantity',
            field=models.SmallIntegerField(default=0),
        ),
    ]