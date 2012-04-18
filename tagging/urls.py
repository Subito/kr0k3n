from django.conf.urls import patterns, include, url

urlpatterns = patterns('tagging.views',
                       url(r'query/', 'query', name='tv_query'),
                       url(r'add/', 'add', name='tv_add'),
)
