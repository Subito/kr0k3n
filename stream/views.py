from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.forms.models import modelform_factory

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

def add_item(request, item_type=None, template_name='stream/add.html'):
    type = get_object_or_404(ContentType, model=item_type)
    formset = modelform_factory(type.model_class())
    if request.method == 'POST':
        form = formset(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sv_home'))
        return render_to_response(template_name,
                                  locals(),
                                  context_instance=RequestContext(request))
    form = formset()
    return render_to_response(template_name,
                              locals(),
                              context_instance=RequestContext(request))

def edit_item(request, item_type=None, item_id=None, template_name='stream/add.html'):
    type = get_object_or_404(ContentType, model=item_type)
    formset = modelform_factory(type.model_class())
    if request.method == 'POST':
        form = formset(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sv_home'))
    item = StreamItem.objects.get(pk=item_id)
    object = item.content_object
    form = formset(instance=object)
    return render_to_response(template_name,
                              locals(),
                              context_instance=RequestContext(request))
