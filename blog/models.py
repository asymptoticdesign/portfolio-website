import datetime
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=250, help_text="Maximum 250 characters")
    slug = models.SlugField(unique=True,help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

class Entry(models.Model):
    #constants
    DRAFT_STATUS = 0
    HIDDEN_STATUS = 1
    LIVE_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
        (LIVE_STATUS, 'Live'))

    #fields
    title = models.CharField(max_length=250)
    summary = models.TextField(blank=True)
    body = models.TextField()
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField()
#    overview_image = models.URLField(blank=True)
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.publish_date.strftime("%Y/%b/%d").lower(), self.slug)

class Link(models.Model):
    # Metadata.
    enable_comments = models.BooleanField(default=True)
    post_delicious = models.BooleanField('Post to Delicious', default=True, help_text='If checked, this will be posted both to your blog and to your delicious.com account. (Currently disabled)')
    post_twitter = models.BooleanField('Post to Twitter', default=False, help_text='If checked, this will be posted both to your blog and to your twitter account. (Currently disabled)')
    posted_by = models.ForeignKey(User)
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date', help_text='Must be unique for the publication date.')
    title = models.CharField(max_length=250)

    # The actual link bits.
    categories = models.ManyToManyField(Category)
    tags = TagField()
    description = models.TextField(blank=True)
    via_name = models.CharField('Via', max_length=250, blank=True, help_text='The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField('Via URL', blank=True, help_text='The URL of the site where you spotted the link. Optional.')
    url = models.URLField('URL', unique=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            if self.post_delicious:
                import pydelicious
                from django.utils.encoding import smart_str
                pydelicious.add(settings.DELICIOUS_USER,
                                settings.DELICIOUS_PASSWORD,
                                smart_str(self.url),
                                smart_str(self.title),
                                smart_str(self.tags))
            if self.post_twitter:
                #post to twitter
        super(Link, self).save()

    def get_absolute_url(self):
        return "/links/%s/%s/" % (self.publish_date.strftime("%Y/%b/%d").lower(), self.slug)
