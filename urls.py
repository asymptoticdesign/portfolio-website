import blog.views
from django.conf.urls.defaults import *
from django.views.generic.simple import *
from django.views.generic.date_based import *
from django.contrib import admin
from portfolio.models import Project
from blog.models import Entry, Link
from blog.feeds import LatestEntries, LatestLinks
from tagging.models import Tag

admin.autodiscover()

portfolio_dict = {
    'queryset': Project.objects.filter(status=Project.LIVE_STATUS),
}

entry_info_dict = {
    'queryset': Entry.objects.filter(status=Entry.LIVE_STATUS),
    'date_field': 'publish_date',
    }

entry_info_year_dict = {
    'queryset': Entry.objects.filter(status=Entry.LIVE_STATUS),
    'date_field': 'publish_date',
    'make_object_list': True,
    }

link_info_dict = {
    'queryset': Link.objects.filter(status=Link.LIVE_STATUS),
    'date_field': 'publish_date',
    }

link_info_year_dict = {
    'queryset': Link.objects.filter(status=Link.LIVE_STATUS),
    'date_field': 'publish_date',
    'make_object_list': True,
    }

feeds = {
    'posts': LatestEntries,
    'links': LatestLinks,
      }

#blog urls patterns
urlpatterns = patterns('',
    ('^admin/', include(admin.site.urls)),
    ('^$', direct_to_template, {'template': 'index.html'}),
    ('^about/$', direct_to_template, {'template': 'about.html'}),
    ('^blog/$', 'django.views.generic.date_based.archive_index', entry_info_dict),
    ('^blog/(?P<year>\d{4})/$','django.views.generic.date_based.archive_year',entry_info_year_dict),
    ('^blog/(?P<year>\d{4})/(?P<month>\w{3})/$','django.views.generic.date_based.archive_month',entry_info_dict),
    ('^blog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','django.views.generic.date_based.archive_day',entry_info_dict),
    ('^blog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','django.views.generic.date_based.object_detail',entry_info_dict),
    )

#art blog patterns
urlpatterns += patterns('',
    ('^art-blog/$', 'django.views.generic.date_based.archive_index', link_info_dict),
    ('^art-blog/(?P<year>\d{4})/$','django.views.generic.date_based.archive_year',link_info_year_dict),
    ('^art-blog/(?P<year>\d{4})/(?P<month>\w{3})/$','django.views.generic.date_based.archive_month',link_info_dict),
    ('^art-blog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','django.views.generic.date_based.archive_day',link_info_dict),
    ('^art-blog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','django.views.generic.date_based.object_detail',link_info_dict),
    )

#portfolio patterns
urlpatterns += patterns('',
    ('^projects/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/project_list.html")),
    ('^projects/science/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/science.html")),
    ('^projects/art/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/art.html")),
    ('^projects/technology/$', 'django.views.generic.list_detail.object_list', dict(portfolio_dict, template_name="portfolio/technology.html")),
    )

#tag related patterns
urlpatterns += patterns('',
    (r'^tags/$','django.views.generic.list_detail.object_list',{'queryset': Tag.objects.all()}),
    (r'^tags/entries/(?P<tag>[-\w]+)/$','tagging.views.tagged_object_list',{'queryset_or_model': Entry,'template_name': 'tagged_entries.html'}),
    (r'^tags/links/(?P<tag>[-\w]+)/$','tagging.views.tagged_object_list',{'queryset_or_model': Link,'template_name': 'tagged_links.html'}),
    )

#rss feed patterns
urlpatterns += patterns('django.contrib.syndication.views',
    (r'^feeds/(?P<url>.*)/$', 'feed', {'feed_dict': feeds})
    )
