from django.contrib import admin

from bookmark.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created')
    list_filter = ('created',)

admin.site.register(Bookmark, BookmarkAdmin)
