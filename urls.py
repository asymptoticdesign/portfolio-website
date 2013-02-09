from django.conf.urls.defaults import *
from django.views.generic.simple import *
from django.contrib import admin
from portfolio.models import Project
import blog.views

admin.autodiscover()

portfolio_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = patterns('',
    ('^admin/', include(admin.site.urls)),
    ('^$', direct_to_template, {'template': 'index.html'}),
    ('^about/$', direct_to_template, {'template': 'about.html'}),
    ('^blog/$', 'blog.views.entry_list'),
    ('^blog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','blog.views.entry_detail'),                  
    ('^science/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/science.html")),
    ('^art/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/art.html")),
    ('^technology/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/technology.html")),
)
