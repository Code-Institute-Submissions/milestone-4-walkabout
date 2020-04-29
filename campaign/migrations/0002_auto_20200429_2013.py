# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-29 19:13
from __future__ import unicode_literals

import campaign.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_type',
            field=models.CharField(choices=[(campaign.models.CampaignChoice('Leafleting'), 'Leafleting'), (campaign.models.CampaignChoice('Canvassing'), 'Canvassing'), (campaign.models.CampaignChoice('Surveying'), 'Surveying')], default='LE', max_length=15),
        ),
    ]