#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-08-27 17:47
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import sys, urllib2

req = urllib2.Request(sys.argv[1])

fd = urllib2.urlopen(req)

print 'Retrieved', fd.geturl()

info = fd.info()

for key, value in info.items():
    print "%s = %s" % (key, value)
