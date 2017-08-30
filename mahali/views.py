# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.measure import D
from django.shortcuts import render

from django.http import HttpResponse
from models import Position, Parent
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.gis.geos import Point
from utils import send_sms


@csrf_exempt
def mahali(request):
    """
    Function to  receive decoded SMS data, query the database for parents within 500 M 
    from the extracted x,y and send them the SMS
    """
    if request.method == 'POST':
        data = json.loads(request.body) # Obtain the postion and speed from the POST data
        position = data['position']
        speed = data['speed']
        point = Point(position)
        mahali = Position(position=point, speed=speed)
        mahali.save() # Save the position to db

        # then do the actual spatial query using the  POSTGIS ST_Distance Function
        parents = Parent.objects.filter(location__distance_lte=(mahali.position, D(m=300)))

        # send the actual sms if parents within the area are found
        if parents:
            for parent in parents:
                print parent.name
                message = "Hello {0}. K school here. Please come pick/drop your child".format(parent.name)
                result = send_sms(parent.mobile_number, message)
                print result
            return HttpResponse("Messages Sent Successfully")
        else:
            return HttpResponse("No parents found within the specified distance.")
    return HttpResponse('GET not allowed')


def home(request):
    return render(request,'index.html')
