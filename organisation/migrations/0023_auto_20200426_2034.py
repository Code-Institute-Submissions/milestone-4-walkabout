# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-26 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0022_organisation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='town_and_city',
            new_name='town_or_city',
        ),
    ]
