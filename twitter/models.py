from django.db import models

class Tweet(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    raw_json = models.TextField()
    
    def __unicode__(self):
        return '<Tweet %s>' % self.pk
