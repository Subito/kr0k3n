from django.conf.urls import patterns, include, url

urlpatterns = patterns('tagging.views',
                       url(r'query/', 'query', name='tv_query'),
                       url(r'add/', 'add_tag', name='tv_add'),
                       url(r'delete/', 'delete_tag', name='tv_delete'),
                       url(r'get/', 'get_tags', name='tv_get_tags'),
)
