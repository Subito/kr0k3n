from django.contrib import admin

from collection.models import Collection, Collection_Items

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created',)
    list_filter = ('created',)

class CollectionItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'collection', 'item', 'created',)
    list_filter = ('collection', 'created',)

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Collection_Items, CollectionItemAdmin)
