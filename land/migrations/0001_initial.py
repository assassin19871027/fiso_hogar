# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_key', models.CharField(max_length=31)),
                ('location', models.CharField(max_length=255)),
                ('land_area', models.DecimalField(decimal_places=0, max_digits=3)),
                ('building_area', models.DecimalField(decimal_places=0, max_digits=3)),
                ('living_room', models.DecimalField(decimal_places=0, max_digits=2)),
                ('bathroom', models.DecimalField(decimal_places=0, max_digits=2)),
                ('parking_lot', models.DecimalField(decimal_places=0, max_digits=2)),
                ('antiquity', models.DecimalField(decimal_places=0, max_digits=2)),
                ('provision', models.DecimalField(decimal_places=0, max_digits=2)),
                ('ambientes', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=511)),
                ('rent_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('tag_line', models.CharField(max_length=127)),
                ('image_url', models.CharField(max_length=63)),
            ],
            options={
                'ordering': ['-unique_key'],
            },
        ),
    ]
