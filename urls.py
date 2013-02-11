from django.conf.urls.defaults import *
from django.views.generic.simple import *
from django.views.generic.date_based import *
from django.contrib import admin
from portfolio.models import Project
from blog.models import Entry
import blog.views

admin.autodiscover()

portfolio_dict = {
    'queryset': Project.objects.all(),
}

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'publish_date',
    }

urlpatterns = patterns('',
    ('^admin/', include(admin.site.urls)),
    ('^$', direct_to_template, {'template': 'index.html'}),
    ('^about/$', direct_to_template, {'template': 'about.html'}),
   ('^blog/$', 'blog.views.entry_list'),
    #('^blog/$', 'django.views.generic.date_based.archive_index', entry_info_dict),
    ('^blog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','django.views.generic.date_based.object_detail',entry_info_dict),

    ('^science/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/science.html")),
    ('^art/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/art.html")),
    ('^technology/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/technology.html")),
)
