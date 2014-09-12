#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年06月06日 星期五 20时20分24秒

from urllib import urlretrieve

def firstNonBlank(lines):
	for eachline in lines:
		if not eachline.strip():
			continue
		else:
			return eachline

def firstLast(webpage):
	f = open(webpage)
	lines = f.readlines()
	f.close()
	print firstNonBlank(lines)
	lines.reverse()
	print firstNonBlank(lines)

def download(url = 'http://www.baidu.com', process = firstLast):
	try:
		retval = urlretrieve(url)[0]
	except IOError:
		retval = None
	if retval:
		process(retval)

if __name__ == '__main__':
	download()
