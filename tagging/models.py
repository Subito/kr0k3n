from django.db import models
from stream.models import StreamItem

class Tag(models.Model):
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<Tag %s>' % self.slug

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag)
    item = models.ForeignKey(StreamItem)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<TaggedItem %s>' % self.pk
