# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 17:20
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('mobile_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('speed', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
