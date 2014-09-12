#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年05月28日 星期三 23时08分19秒

import os

filename = raw_input("Enter file name :")
f = open(filename, 'w')


while True:
	aline = raw_input("Enter a line ('.' to quit):")
	if aline != ".":
		f.write('%s%s' % (aline, os.linesep))
	else:
		break

f.close()
