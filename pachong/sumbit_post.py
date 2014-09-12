#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-08-27 21:34
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import sys
import urllib2
import urllib

zipcode = sys.argv[1]

url = 'http://www.baidu.com'

data = urllib.urlencode([('query', zipcode)])

req = urllib2.Request(url)

fd = urllib2.urlopen(req, data)

print fd.readline()
