# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-18 11:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaign', '0021_auto_20200517_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='assigned_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]