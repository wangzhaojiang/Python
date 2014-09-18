from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/{0,1}', include(admin.site.urls)),
    url(r'^polls/{0,1}', include('polls.urls', namespace = "polls")),
)
