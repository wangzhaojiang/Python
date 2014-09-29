#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-09-25 18:59
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("hello world")

def current_datetime(request):
    current_date = datetime.datetime.now()
    
    #return render_to_response('current_datetime.html', {'current_date': now})
    return render_to_response('current_datetime.html', locals())
    

def hours_ahead(request, offset):
    try:

        hour_offset = int(offset)
        
    except ValueError:
 
        raise Http404()

    next_time = datetime.datetime.now() #+ datetime.timedelta(hours = offset)

    return render_to_response('hours_ahead.html', locals())
