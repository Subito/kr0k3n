from django.db import models

from stream.models import StreamItem

class Collection(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(StreamItem, through='Collection_Items')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<Collection %s>' % self.name

class Collection_Items(models.Model):
    collection = models.ForeignKey(Collection)
    item = models.ForeignKey(StreamItem)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<CollectionItem %s>' % self.pk
