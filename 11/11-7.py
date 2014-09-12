#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年06月07日 星期六 03时31分06秒

def my_zip(*args1):
	print zip(args1[0], args1[1])

if __name__ == '__main__':
	my_zip([1,2,3,4], ['a','b','c','d'])
