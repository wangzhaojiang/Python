#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月23日 星期三 14时39分33秒

import sys, time, os

pid = os.fork()

if pid:
	print 'parent'
	time.sleep(10)

else:
	print 'child'
	print 'hehehe'
	print os.getpid()
	exit(1)
