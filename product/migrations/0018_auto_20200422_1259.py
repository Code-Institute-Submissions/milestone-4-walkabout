# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-22 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='percent',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
