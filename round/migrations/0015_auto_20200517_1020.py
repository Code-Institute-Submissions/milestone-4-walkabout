# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-17 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0014_auto_20200516_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='street',
            options={'ordering': ['name']},
        ),
    ]