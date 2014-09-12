#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-08-27 18:31
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import sys
import urllib2
import getpass

class TerminalPassword(urllib2.HTTPPasswordMgr):

    def find_user_password(self, realm, authuri):
        retval = urllib2.HTTPPasswordMgr.find_user_password(self, realm, authuri)

        if retval[0] == None and retval[1] == None:
            sys.stdout.write("Login requred for %s at %s \n" %s (realm, authuri))

            sys.stdout.write("Username: ")

            username = sys.stdin.readline().rstrip()

            password = getpass.getpass().rstrip()

            return (username, password)
        else:
            return retval

req = urllib2.Request(sys.argv[1])

opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPassword()))

fd = opener.open(req)

print "Retrieved", fd.geturl()

info = fd.info()

for key, value in info.items():
    
    print "%s = %s" % (key, value)

