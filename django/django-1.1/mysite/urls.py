from django.conf.urls.defaults import *
from mysite.views import *
from django.contrib import admin
from mysite.books.views import *
from mysite.contact.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d+)/$', hours_ahead),
    (r'^display/$', display_meta),
    #(r'^search-form/$', views.search_form),
    (r'^search/$', search),
    (r'^contact/$', contact)
)
