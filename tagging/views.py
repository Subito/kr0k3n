import json

from django.shortcuts import render_to_response

from tagging.models import Tag

def query(request):
    if request.GET['q']:
        tags = Tag.objects.filter(slug__startswith=q)
        return render_to_response(json.dumps(tags), mimetype='application/json')
    return render_to_response(json.dumps('no query'), mimetype='application/json')
