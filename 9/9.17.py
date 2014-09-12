#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年05月29日 星期四 21时00分45秒

import os

def create():
	while True:
		filename = raw_input('Enter the filename : ')
		if os.path.exists(filename):
			print 'File : %s exists...' % filename
		else:
			file = open(filename, 'w')
			while True:
				contents = raw_input('>')
				if contents != '.':
					file.write('%s%s' % (contents, os.linesep))
				else:
					break
			file.close()
		break


def show():
	while True:
		filename = raw_input('Enter the filename : ')
		if not os.path.exists(filename):
			print 'The file does not exists'
			continue
		else:
			try:
				file = open(filename, 'r')
				break
			except IOError, e:
				print e
	for line in file:
		print line,

			



#def modify():
#	while True:
#		filename = raw_input('Input the filename : ').strip()
#		if not os.path.exists(filename):
#			continue
#		else:
#			file = open(filename, 'r+')
#			contents = file.readlines()
#			print len(contents)
#			while True:
#				line = int(raw_input('Input the line you want to modify : '))
#				if line <= int(len(contents)):
#					print contents[(line - 1)]
#					contents[(line - 1)] = raw_input('<')
#					print contents
#					file.writelines(contents)
#					file.close()
#					break
#				else:
#					print 'Invail Para'
#					continue





CMDS = {'c': create, 's': show, 'm': modify}


def showment():
	ment = """
	Creat File
	Show File
	Modify File
	Save File
	Exit

	Enter choice : """

	while True:
		while True:
			try:
				choice = raw_input(ment).strip()[0].lower()
			except(EOFError, KeyboardInterrupt, IndexError):
				choice = 'e'
			print ' '* 6 + "your choice is %s" % choice

			if choice not in 'csmse':
				print ' '* 6 + "Invalid option, try again"
			else:
				break
				
		if choice == 'e':
			break
		CMDS[choice]()



	

if __name__ == '__main__':
	showment()
