# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-13 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200410_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_unique_product',
            field=models.BooleanField(default=False, verbose_name='Is a unique product?'),
        ),
    ]
