from django.conf.urls import patterns, include, url
from myfirstsite.views import *
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib import admin
=======
>>>>>>> 268c6503470402bdc5bdd2fc5645391954d7004a
=======
>>>>>>> 268c6503470402bdc5bdd2fc5645391954d7004a

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        ('^hello$', hello),
        ('^time$', current_datetime),
        (r'^time/plus/(\d+)$', hours_ahead),
<<<<<<< HEAD
<<<<<<< HEAD
        (r'^mypage$', mypage),
=======
        (r'^mypage$', mypage)
>>>>>>> 268c6503470402bdc5bdd2fc5645391954d7004a
=======
        (r'^mypage$', mypage)
>>>>>>> 268c6503470402bdc5bdd2fc5645391954d7004a
    # Examples:
    # url(r'^$', 'myfirstsite.views.home', name='home'),
    # url(r'^myfirstsite/', include('myfirstsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
<<<<<<< HEAD
<<<<<<< HEAD
     #r'^admin/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
=======
=======
>>>>>>> 268c6503470402bdc5bdd2fc5645391954d7004a
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
>>>>>>> 268c6503470402bdc5bdd2fc5645391954d7004a
=======
>>>>>>> 268c6503470402bdc5bdd2fc5645391954d7004a
)
