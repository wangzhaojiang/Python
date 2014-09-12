#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年05月21日 星期三 18时40分04秒

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test? ')

if len(myInput) > 1:
	if myInput[0] not in alphas:
		print '''invalid : first symbol must be alphabetic'''
	else:
		for otherChar in myInput[1:]:
			print 'char : %s ' % otherChar

			if otherChar not in (alphas + nums):
				print '''invalid : remaining symbols must be alphanumberic'''
				break
		else:
			print "okay as an identifier"
