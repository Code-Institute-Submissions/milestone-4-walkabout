# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-18 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20200418_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_base_product',
            field=models.BooleanField(default=False, verbose_name='Is a base product?'),
        ),
    ]