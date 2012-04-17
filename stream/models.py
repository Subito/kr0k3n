from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from picture.models import Image
from bookmark.models import Bookmark
from note.models import Note

STREAM_MODELS = (Image,
                 Bookmark,
                 Note,
                 )

class StreamItem(models.Model):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    display = models.BooleanField(default=True)

    def __unicode__(self):
        return '<Item %s>' % self.pk

@receiver(post_save)
def created_stream_item(sender, instance, created, **kwargs):
    if created and sender in STREAM_MODELS:
        new_item = StreamItem(content_object=instance)
        new_item.save()
