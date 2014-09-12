#!/usr/bin/env python
#coding:utf-8


import urllib2
import urllib
import re


url = 'http://www.renren.com/activity/get/data'


header = {'GET':url, 'Host':'www.renren.com', 
'Referer':'http://www.renren.com/370327992', 
'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36'
}

req = urllib2.Request(url)

#data = urllib.urlencode(header)
#print data

#req.add_header(data)
html = urllib2.urlopen(req).read()

print html
