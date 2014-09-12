#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月23日 星期三 21时00分52秒

import threading, time

aaa = 100

def sleepandprint():
	time.sleep(1)
	print "hello from both of us"

def threadcode():
	global aaa
	a = 10000
	print aaa
	print "hello from the new thread. My name is %s \n" % threading.currentThread().getName()
	sleepandprint()
	time.sleep(2)
	print 'child thread done'
	print aaa
	aaa += 50
	print aaa

print "Before starting a new thread, my name is ", threading.currentThread().getName()

t = threading.Thread(target = threadcode, name = "ChildThread")

#t.setDaemon(1)
t.start()
print "hello from the main thread. My name is %s\n" % threading.currentThread().getName()
print a
aaa += 50
time.sleep(1)
sleepandprint()

#t.join()
