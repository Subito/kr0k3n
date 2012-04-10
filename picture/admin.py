from django.contrib import admin

from picture.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created',)
    list_filter = ('created',)

admin.site.register(Image, ImageAdmin)
