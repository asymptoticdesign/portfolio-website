from django.conf.urls.defaults import *
from django.views.generic.simple import *
from django.contrib import admin
from portfolio.models import Project

admin.autodiscover()

portfolio_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = patterns('',
    ('^admin/', include(admin.site.urls)),
    ('^$', direct_to_template, {'template': 'index.html'}),
    ('^about/$', direct_to_template, {'template': 'about.html'}),
    ('^blog/$', direct_to_template, {'template': 'blog.html'}),
    ('^science/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/science.html")),
    ('^art/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/art.html")),
    ('^technology/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/technology.html")),
)
