#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月14日 星期一 14时44分32秒

from socket import	*
from time  import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print 'waiting for messages...'
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	print 'recv from ', addr
	udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)

udpSerSock.close()
