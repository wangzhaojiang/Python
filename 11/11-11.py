#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年06月07日 星期六 08时43分14秒

if __name__ == '__main__':
	dir = raw_input("Enter the Path : ").strip()
	try:
		file = open(dir, 'r')
		content = file.readlines()
		print map(lambda x:x.strip(), content)
	except IOError, e:
		print e
