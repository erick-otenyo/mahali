# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Position(models.Model):
    position = models.PointField(srid=4326)
    speed = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.time.strftime('%H:%M , %Y-%m-%d ')


class Parent(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    mobile_number = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
