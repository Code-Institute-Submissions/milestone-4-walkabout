# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-16 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0015_auto_20200516_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='rounds',
        ),
    ]
