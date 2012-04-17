from django.db import models
from django.contrib.contenttypes import generic

class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<Bookmark %s>' % self.url
