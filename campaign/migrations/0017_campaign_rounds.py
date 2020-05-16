# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-16 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0013_auto_20200516_2016'),
        ('campaign', '0016_remove_campaign_rounds'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='rounds',
            field=models.ManyToManyField(to='round.Round'),
        ),
    ]
