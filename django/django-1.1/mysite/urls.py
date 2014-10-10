from django.conf.urls.defaults import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mysite.views',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', 'hello'),
    (r'^time/$', 'current_datetime'),
    (r'^time/plus/(?P<offset>\d+)/$', 'hours_ahead'),
)
#
#urlpatterns = patterns('mysite.books.views',
#    (r'^display/$', 'display_meta'),
#    (r'^search/$', 'search'),
#        )
#
#urlpatterns = patterns('mysite.contact.views',
#    (r'^contact/$', 'contact'),
#        )
