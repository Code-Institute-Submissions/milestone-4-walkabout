# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-22 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20200422_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='percent',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]