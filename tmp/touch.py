#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年05月02日 星期五 02时36分13秒

import os

ls = os.linesep
#get filename

while True:
	filename = raw_input('Input the filename: ')
	if os.path.exists(filename):
		print 'ERROR: file: %s EXISTS' % filename
	else:
		break

#write the contents to the file
all = []
print 'EOF means to finish the input'

while True:
	entry = raw_input('>')
	if entry == 'EOF':
		break
	else:
		all.append(entry)

fobj = open(filename, 'w')
fobj.writelines(['%s%s' % (contents, ls) for contents in all])
fobj.close()
print 'DONE!'
