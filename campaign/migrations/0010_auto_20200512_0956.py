# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-12 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0009_auto_20200511_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_type',
            field=models.CharField(choices=[('LEAFLET', 'Leafleting'), ('CANVASS', 'Canvassing'), ('SURVEY', 'Surveying')], default='LEAF', max_length=20),
        ),
    ]
