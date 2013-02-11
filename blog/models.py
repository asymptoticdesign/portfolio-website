import datetime
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField

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
    tags = TagField()

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.publish_date.strftime("%Y/%b/%d").lower(), self.slug)
