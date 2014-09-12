#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月21日 星期一 13时06分22秒

from optparse import OptionParser  
def main():  
    usage = "usage: %prog [options] arg"  
    parser = OptionParser(usage)  
#    parser.add_option("-f", "--file", dest="filename",  
#                      help="read data from FILENAME")  
#    parser.add_option("-v", "--verbose",  
#                      action="store_true", dest="verbose")  
#    parser.add_option("-q", "--quiet",  
#                      action="store_false", dest="verbose")  
#    parser.add_option("-a", "--A",action = "store_true",  dest = "a" )
    (options, args) = parser.parse_args()  
    print args
    if len(args) != 1:  
        parser.error("incorrect number of arguments")  
    if options.verbose:  
        print "reading %s..." % options.filename  
  
if __name__ == "__main__":  
    main()  
