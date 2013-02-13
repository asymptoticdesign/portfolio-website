from django.contrib.syndication.feeds import Feed
from blog.models import Entry, Link

class LatestEntries(Feed):
    title = "AsymptoticDesign -- Blog"
    link = "http://www.asymptoticdesign.org/blog/"
    description = "Updates on projects by AsymptoticDesign"

    def items(self):
        return Entry.objects.all().filter(status=Entry.LIVE_STATUS).order_by('-publish_date')[:5]

class LatestLinks(Feed):
    title = "AsymptoticDesign -- Links"
    link = "http://www.asymptoticdesign.org/art-blog/"
    description = "Latest inspirations, compiled by AsymptoticDesign"

    def items(self):
        return Link.objects.all().filter(status=Link.LIVE_STATUS).order_by('-publish_date')[:5]
