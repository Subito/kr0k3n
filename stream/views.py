from django.shortcuts import render_to_response
from django.template import RequestContext

from stream.models import StreamItem

def home(request, template_name='stream/stream.html'):
    items = StreamItem.objects.order_by('-created')[:20]
    return render_to_response(template_name, 
                              locals(), 
                              context_instance=RequestContext(request))
