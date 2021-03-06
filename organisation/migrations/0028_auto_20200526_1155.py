# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-26 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0027_auto_20200522_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='address_2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='mobile_number',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='town_or_city',
            field=models.CharField(max_length=40),
        ),
    ]
