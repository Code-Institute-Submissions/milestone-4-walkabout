# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-24 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200420_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_4',
            new_name='town_or_city',
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile_number',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name of your organisation or your full name if not an organisation.'),
        ),
    ]
