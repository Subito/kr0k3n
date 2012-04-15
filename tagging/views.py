import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers

from tagging.models import Tag

def query(request):
    if request.GET['q']:
        tags = []
        q = request.GET['q']
        tag_objects = Tag.objects.filter(slug__contains=q)
        for tag in tag_objects:
            this_tag = {}
            this_tag['id'] = tag.pk
            this_tag['name'] = tag.slug
            tags.append(this_tag)
        if not tags:
            tags.append(q)
        return HttpResponse(json.dumps(tags), mimetype='application/json')
    return HttpResponse(json.dumps('no query'), mimetype='application/json')
