#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年06月07日 星期六 07时56分23秒

def RunYear(year):
	try:
		if not (int(year) % 4) and  not (int(year) % 100):
			return True
	except Exception, e:
		print e
	 	return False

if __name__ == '__main__':
	while True:
		try:
			year = (raw_input("Enter the Year : "))
			print year
			for i in year:
				if i == ',':
					year.remove(',')
		except Exception, e:
			print e
			continue
		else:
			print filter(RunYear, year)
			break
