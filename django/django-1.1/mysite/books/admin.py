#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-09-29 21:36
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

from django.contrib import admin
from mysite.books.models import Publisher, Author, Book

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
