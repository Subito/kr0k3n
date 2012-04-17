from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'add/(?P<item_type>\w+)/', 'stream.views.add_item', name='sv_add_item'),
                       url(r'edit/(?P<item_type>\w+)/(?P<item_id>\d+)/', 'stream.views.edit_item', name='sv_edit_item'),
                       url(r'delete/(?P<item_id>\d+)/', 'stream.views.delete_item', name='sv_delete_item'),
                       url(r'(?P<item_id>\d+)/', 'stream.views.details', name='sv_details'),
)
