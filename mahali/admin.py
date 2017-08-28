# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Position,Parent

class PositionAdmin(LeafletGeoAdmin):
    readonly_fields = ('time',)

admin.site.register(Position,PositionAdmin)
admin.site.register(Parent,LeafletGeoAdmin)