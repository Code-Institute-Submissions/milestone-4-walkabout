# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-24 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200424_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='landline_number',
        ),
    ]
