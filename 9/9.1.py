#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年05月29日 星期四 18时06分56秒

import os

while True:
	filename = raw_input("Enter the filename :")
	if not (os.path.exists(filename)):
		print "Error : the filename does no exists, please input again."
		continue
	else:
		f = open(filename, 'r')
		for line in f:
			if not (line[0] == '#'):
				print line,
	break

f.close()


