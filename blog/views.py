import datetime, time
from django.shortcuts import *
from models import Entry

def entry_list(request):
    return render_to_response('blog/entry_listing.html',
                              { 'entry_list': Entry.objects.all() },
                              context_instance=RequestContext(request))

def entry_detail(request, year, month, day, slug):
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    publish_date = datetime.date(*date_stamp[:3])
    entry = get_object_or_404(Entry, publish_date__year=publish_date.year,
                              publish_date__month=publish_date.month,
                              publish_date__day=publish_date.day,
                              slug=slug)
    return render_to_response('blog/entry_detail.html',
                              { 'entry': entry },
                              context_instance=RequestContext(request))