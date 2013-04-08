import datetime
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from django.conf import settings

class Entry(models.Model):
    #constants
    DRAFT_STATUS = 0
    HIDDEN_STATUS = 1
    LIVE_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
        (LIVE_STATUS, 'Live')
        )

    #required fields
    title = models.CharField(max_length=250,help_text="Maximum 250 characters")
    slug = models.SlugField(help_text="Suggested value automatically generated from title. Must be unique.")
    author = models.ForeignKey(User)
    summary = models.TextField()
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    overview_image = models.URLField(verify_exists=False)
    body = models.TextField()

    tags = TagField()
    
    #options
    enable_comments = models.BooleanField(default=True)
    post_twitter = models.BooleanField('Post to Twitter', default=False, help_text='If checked, this will be posted both to your blog and to your twitter account. (Currently disabled)')
    twitter_text = models.CharField(blank=True,max_length=144,help_text="This is the text that will be sent as a twitter status.")

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            None
            if self.post_twitter:
                import twitter
                api = twitter.Api(consumer_key=settings.TWITTER_KEY,
                                  consumer_secret=settings.TWITTER_SECRET,
                                  access_token_key=settings.TWITTER_TOKEN,
                                  access_token_secret=settings.TWITTER_TOKEN_SECRET)
                api.PostUpdate(twitter_text)
        super(Entry, self).save()

    def get_tags(self):
        return Tag.objects.get_for_object(self) 

    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.publish_date.strftime("%Y/%b/%d").lower(), self.slug)

class Link(models.Model):
    DRAFT_STATUS = 0
    HIDDEN_STATUS = 1
    LIVE_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
        (LIVE_STATUS, 'Live')
        )
    
    #Required link info
    title = models.CharField(max_length=250,help_text="Maximum 250 characters")
    slug = models.SlugField(unique_for_date='publish_date',help_text="Suggested value automatically generated from title. Must be unique.")
    url = models.URLField('URL', unique=True)
    summary = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    author = models.ForeignKey(User)
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    
    #metadata 
    tags = TagField()
    via_name = models.CharField('Via', max_length=250, blank=True, help_text='The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField('Via URL', blank=True, help_text='The URL of the site where you spotted the link. Optional.')

    # in-depth view
    overview_image = models.URLField(blank=True)
    body = models.TextField(blank=True)
    
    #options
    enable_comments = models.BooleanField(default=True)
    post_delicious = models.BooleanField('Post to Delicious', default=True, help_text='If checked, this will be posted both to your blog and to your delicious.com account. (Currently disabled)')
    post_twitter = models.BooleanField('Post to Twitter', default=False, help_text='If checked, this will be posted both to your blog and to your twitter account. (Currently disabled)')
    twitter_text = models.CharField(blank=True,max_length=140,help_text="This is the text that will be sent as a twitter status.")

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
                import twitter
                api = twitter.Api(consumer_key=settings.TWITTER_KEY,
                                  consumer_secret=settings.TWITTER_SECRET,
                                  access_token_key=settings.TWITTER_TOKEN,
                                  access_token_secret=settings.TWITTER_TOKEN_SECRET)
                api.PostUpdate(twitter_text)
            super(Link, self).save()

    def get_tags(self):
        return Tag.objects.get_for_object(self) 

    def get_absolute_url(self):
        return "/links/%s/%s/" % (self.publish_date.strftime("%Y/%b/%d").lower(), self.slug)
    
