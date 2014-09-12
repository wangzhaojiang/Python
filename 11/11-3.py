#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年06月07日 星期六 02时22分41秒

def my_max(*args):
	print args
	try:
		for num in args[0]:
			print num
			if not (int(num) or float(num)):
				print "Invaild Input...."
	except Exception, e:	
		print e
	try:
		args[0].reverse()
		print args[0][0]
	except Exception, e:
		print e
	

if __name__ == '__main__' :
	args = list(raw_input('Enter the nums : '))
	print args
	count = 0
	try:
		while count < len(args):
			args.remove(',')
	except ValueError, e:
		print e
	print args
	my_max(args)

