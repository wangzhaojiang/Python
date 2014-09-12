#!/usr/bin/env python
#coding:utf-8


import urllib2
import urllib
import re

key = raw_input('Input The KeyWord : ')

key = urllib.quote(key) #转码

url = 'http://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word='
url = url + key


header = {'GET':url, 'HOST':'sug.so.360.cn', 
'Referer':'http://www.so.com/', 
'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36'
}

req = urllib2.Request(url)

#data = urllib.urlencode(header)
#print data

#req.add_header(data)
for key in header:
    req.add_header(key, header[key])

html = urllib2.urlopen(req).read()

print html

data = re.findall(":\"(.*?)\"", html)
for item in data:
    print item
