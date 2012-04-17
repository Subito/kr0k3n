from django.db import models
from django.contrib.contenttypes import generic

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<Note %s>' % self.title
