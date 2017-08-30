# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

# Define model to hold a position from the decoded sms
class Position(models.Model):
    position = models.PointField(srid=4326) # Define a GIS point 
    speed = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.time.strftime('%H:%M , %Y-%m-%d ')

# Define model to hold parents data
class Parent(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326) # Define a GIS point
    mobile_number = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
