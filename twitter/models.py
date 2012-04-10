from django.db import models

class Tweet(models.Model):
    raw_json = models.TextField()
    
    def __unicode__(self):
        return '<Tweet %s>' % self.pk
