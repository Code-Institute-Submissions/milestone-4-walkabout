# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-29 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_auto_20200429_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'ordering': ['active_date', 'campaign_type', 'name']},
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='start_date',
            new_name='active_date',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='end_date',
        ),
        migrations.AddField(
            model_name='campaign',
            name='inactive_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]