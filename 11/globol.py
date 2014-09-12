#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年06月07日 星期六 00时53分02秒

j, k = 1, 2

def proc1():
	j, k = 3, 4
	print "j == %d and k == %d " % (j, k)
	k = 5

def proc2():
	j = 6
	proc1()
	print "j == %d and k == %d" % (j, k)

k = 7
proc1()
print "j == %d and k == %d" % (j, k)

j = 8 
proc2()
print "j == %d and k == %d" % (j, k)

