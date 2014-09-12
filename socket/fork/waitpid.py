#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月23日 星期三 14时20分54秒

import socket, os, sys

def reap():
		while 1:
			try:
				result = os.waitpid(0, os.WNOHANG)
				print result
				if not result[0]:break
			except:
				break
host = ''
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "Parent at %d listening for conections" % os.getpid()

while 1:
	clisock, cliaddr = s.accept()
	print clisock.getpeername()
	reap()
	pid = os.fork()

	if pid:
		clisock.close()
		continue
	else:
		s.close()
		print 'child from %s being handle by PID %d ' % (clisock.getpeername(), os.getpid())

		#while 1:
		data = clisock.recv(4096)
		if not len(data):
			break
		print data,
		print 'DONE'

		clisock.close()
		sys.exit(0)
