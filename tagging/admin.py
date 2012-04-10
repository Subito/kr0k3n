from django.contrib import admin

from tagging.models import Tag, TaggedItem

class TagAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created',)
    list_filter = ('created',)

class TaggedItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tag', 'created',)
    list_filter = ('created', 'tag',)

admin.site.register(Tag, TagAdmin)
admin.site.register(TaggedItem, TaggedItemAdmin)
