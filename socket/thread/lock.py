#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月24日 星期四 10时24分05秒

import threading, time

b = 50

l = threading.Lock()

def threadcode():
	global b
	print "thread %s invoked" % threading.currentThread().getName()
	l.acquire()
	try:
		print "thread %s running" % threading.currentThread().getName()
		time.sleep(1)
		b = b+ 50
		print "Thread %s set b to %d" % (threading.currentThread().getName(), b)

	finally:
		#l.release()
		print 'test\n'

print 'Value of b at start of program : ', b
childthread = []

for i in range(1,5):
	t = threading.Thread(target = threadcode, name = "Thread-%d " % i)
	t.setDaemon(1)

	t.start()

	childthread.append(t)

for t in childthread:
	t.join()

print "new value of b: ",b
