#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月24日 星期四 14时02分06秒

import threading, time


def thread1():
	global a
	print 'thread1 acquiring lock a'
	alock.acquire()
	a += 5
	print 'from thread1 ', a
	time.sleep(1)
	#alock.release()

def thread2():
	global a
	print 'thead2 acquiring lock a'
	alock.acquire()
	a += 5
	print 'from thread2 ', a

a = 5
alock = threading.Lock()
t1 = threading.Thread(target = thread1)
t2 = threading.Thread(target = thread2)
t1.start()
t2.start()
print 'main'
time.sleep(3)
print 'from main', a
a += 5
print 'from main', a
