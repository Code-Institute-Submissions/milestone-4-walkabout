# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-20 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0017_auto_20200418_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='contact',
            new_name='contact_name',
        ),
    ]
