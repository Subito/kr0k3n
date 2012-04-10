from django.contrib import admin

from note.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created',)
    list_filter = ('created',)

admin.site.register(Note, NoteAdmin)
