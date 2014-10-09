#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-09 18:32
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

from django import forms

class ContactForm(forms.Form):
        subject = forms.CharField(max_length = 100)
        email = forms.EmailField(required=False)
        message = forms.CharField()
