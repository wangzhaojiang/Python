from django.conf.urls import patterns, include, url
from myfirstsite.views import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        ('^hello$', hello),
        ('^time$', current_datetime),
        (r'^time/plus/(\d+)$', hours_ahead),
        (r'^mypage$', mypage),
    # Examples:
    # url(r'^$', 'myfirstsite.views.home', name='home'),
    # url(r'^myfirstsite/', include('myfirstsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #r'^admin/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
