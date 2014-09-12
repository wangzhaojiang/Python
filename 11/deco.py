#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年06月06日 星期五 17时49分51秒

from time import ctime, sleep

def tsfunc(fun):
	def wrappedfunc():
		print '[%s] %s() called' % (ctime(), fun.__name__)
		return fun()
	return wrappedfunc

@tsfunc
def foo():
	print 'doing...'
	pass

foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()
