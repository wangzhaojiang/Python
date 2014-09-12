#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-08-30 11:34
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render_to_response
#from django.template import Context
#from django.template.loader import get_template

def hello(HttpRequest):

    return HttpResponse("hello world..")

#def current_datetime(HttpRequest):
#
#    now = datetime.datetime.now()
#
#    html = "<html><body>It is now %s. </body></html>" % now
#
#    return HttpResponse(html)

def hours_ahead(HttpRequest, offset):

    try:
        offset = int(offset)
        
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() - datetime.timedelta(hours = offset)

    return render_to_response("hours_ahead.html", locals())

def current_datetime(request):
    current_datetime = datetime.datetime.now()

    #return render_to_response('current_datetime.html', {'current_datetime' : now})

    return render_to_response('current_datetime.html', locals())

def mypage(request):
    current_datetime = datetime.datetime.now()

    title = 'mypage'

    return render_to_response('mypage.html', locals())
