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

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%sf:</td><td>%s</td></tr>' % (k, v))

    return HttpResponse('<tables>%s</tables>' % '\n'.join(html))

def search_form(request):
    return render_to_response('search_form_.html')
