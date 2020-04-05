# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-19 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('comments', models.TextField()),
                ('door_number_start', models.SmallIntegerField()),
                ('door_number_end', models.SmallIntegerField()),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='round.Round')),
            ],
        ),
    ]