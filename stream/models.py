from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from kr0k3n.utils.decorators import receiver_subclasses

'''
Base models I use to handle the connections between Objects (Items).
If I later plan to add another feature, which requires an own model, I
can simply inherit from "StreamItem" and I get full comment/tagging
functionality.
'''

class Comment(models.Model):
    comment = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type',
                                               'object_id')

class Tag(models.Model):
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type',
                                               'object_id')

class StreamItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type',
                                               'object_id')
    
    def __unicode__(self):
        return '<StreamItem %s>' % self.pk

@receiver_subclasses(post_save, Item, 'item_post_save')
def create_stream_item(sender, instance, created, **kwargs):
    if created:
        new_item = StreamItem(content_object=instance)
        new_item.save()

class Item(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=True)
    children = models.ManyToManyField('self', blank=True, null=True)
    comment = generic.GenericRelation(Comment)
    tags = generic.GenericRelation(TaggedItem)

    class Meta:
        abstract = True

'''
The following models implement the various forms of data I like to
store
'''

class Note(Item):
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.content[:25] + ' [...]'
        super(Note, self).save(*args, **kwargs)

    def __unicode__(self):
        return '<Note %s>' % self.title

class Bookmark(Item):
    url = models.URLField()

    def __unicode__(self):
        return '<Bookmark %s>' % self.url

class Image(Item):
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __unicode__(self):
        return '<Image %s>' % self.title
