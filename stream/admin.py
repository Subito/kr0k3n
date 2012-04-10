from django.contrib import admin

from stream.models import StreamItem

class StreamItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'content_type', 'created',)
    list_filter = ('content_type', 'created',)

admin.site.register(StreamItem, StreamItemAdmin)
