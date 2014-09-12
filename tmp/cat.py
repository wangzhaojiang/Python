#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年05月02日 星期五 09时07分36秒

import os
#get filename

while True:
	try :
		filename = raw_input('Enter filename: ')
		fobj = open(filename, 'r')
		break
	except IOError, e:
		print e


#display the contents
print fobj.read(-1)
fobj.close()
