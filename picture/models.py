from django.db import models
from django.contrib.contenttypes import generic

class Image(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<Image %s>' % self.image.name
    
    def get_absolute_url(self):
        return '%s' % self.image.url
