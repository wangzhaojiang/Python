#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月14日 星期一 01时00分33秒

from socket import *
from time import ctime
import time

HOST = ''
PORT = 10000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print 'waiting for connection...'
	tcpCliSock, addr = tcpSerSock.accept()
	tcpCliSock.settimeout(3)
	print '... connected from :', addr
	break
try:
	while True:
#		data = tcpCliSock.recv(BUFSIZ)
		data = 'test'
		if not data:
			break
		print data
		tcpCliSock.send('[%s]%s' % (ctime(), data))
		time.sleep(1)
	
	tcpSerSock.close()
	tcpCliSock.close()
except (KeyboardInterrupt, EOFError):
	print 'invalid input ...'
