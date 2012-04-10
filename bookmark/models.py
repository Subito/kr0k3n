from django.db import models

class Bookmark(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<Bookmark %s>' % self.url
