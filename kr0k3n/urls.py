from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kr0k3n.views.home', name='home'),
    # url(r'^kr0k3n/', include('kr0k3n.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
