from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from stream.models import StreamItem

def home(request, template_name='stream/stream.html'):
    items = StreamItem.objects.order_by('-created')[:20]
    return render_to_response(template_name, 
                              locals(), 
                              context_instance=RequestContext(request))

def details(request, item_id=None):
    item = get_object_or_404(StreamItem, pk=item_id)
    template_name = 'stream/item/%s.html' % item.content_type.name
    return render_to_response(template_name, 
                              locals(),
                              context_instance=RequestContext(request))
