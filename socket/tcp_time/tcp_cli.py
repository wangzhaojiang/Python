#  File : tcp_cli.py
# -*-coding:utf-8-*-
# Author: wangzhaojiang
#  Modified date: 2014-08-25 19:49

from socket import *

HOST = 'localhost'
PORT = 10000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)


while True:
	data = raw_input('>')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data

tcpCliSock.close()
