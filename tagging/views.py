import json

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from stream.models import StreamItem
from tagging.models import Tag, TaggedItem

def query(request):
    if request.GET['q']:
        tags = []
        q = request.GET['q']
        tag_objects = Tag.objects.filter(slug__contains=q)
        for tag in tag_objects:
            this_tag = {
                'id': tag.pk,
                'name': tag.slug
                }
            tags.append(this_tag)
        if not tags:
            new_tag = {'id': None, 'name': q}
            tags.append(new_tag)
        return HttpResponse(json.dumps(tags), mimetype='application/json')
    return HttpResponse(json.dumps('no query'), mimetype='application/json')

@csrf_exempt
def get_tags(request):
    if request.method == 'POST':
        item = get_object_or_404(pk=request.POST['item'])
        tagged_items = TaggedItem.objects.filter(item=item)
        tags = []
        for tag in tagged_items:
            tags.append({'id': tag.pk, 'name': tag.slug})
        return HttpResponse(json.dumps(tags), mimetype='application/json')

@csrf_exempt
def add_tag(request):
    if request.method == 'POST':
        item = get_object_or_404(StreamItem, pk=request.POST['item'])
        tag, created = Tag.objects.get_or_create(slug=request.POST['slug'])
        tagged_item = TaggedItem(tag=tag, item=item)
        tagged_item.save()
        return HttpResponse(json.dumps(tagged_item.pk), mimetype='application/json')

@csrf_exempt
def delete_tag(request):
    if request.method == 'POST':
        item = get_object_or_404(StreamItem, pk=request.POST['item'])
        tag = Tag.objects.get(slug=request.POST['slug'])
        tagged_item = TaggedItem.objects.get(tag=tag, item=item)
        tagged_item.delete()
        return HttpResponse(json.dumps('SUCCESS'), mimetype='application/json')
