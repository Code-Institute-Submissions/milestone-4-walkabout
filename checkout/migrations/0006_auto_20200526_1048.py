# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-26 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20200425_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_2',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
