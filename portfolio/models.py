import datetime
from django.db import models
from tagging.fields import TagField
from tagging.models import Tag

class Project(models.Model):
    #constants
    DRAFT_STATUS = 0
    HIDDEN_STATUS = 1
    LIVE_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
        (LIVE_STATUS, 'Live')
        )

    SCI_CAT = 0
    ART_CAT = 1
    TECH_CAT = 2
    PROJECT_CATEGORY = (
        (SCI_CAT,'science'),
        (ART_CAT,'art'),
        (TECH_CAT,'technology')
        )

    #preview
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    summary = models.TextField(help_text="Place the summary (preview) text here.")
    overview_image = models.URLField()
    start_date = models.DateField()
    completion_date = models.DateField(blank=True)

    #in-depth information
    source = models.URLField(blank=True,help_text='URL for source materials (github, zip file, etc.')
    description = models.TextField(blank=True,help_text='Place the main body text here')

    #meta_data
    status = models.IntegerField(choices=STATUS_CHOICES)
    project_type = models.IntegerField(choices=PROJECT_CATEGORY)
    tags = TagField()

    class Meta:
        ordering = ['-completion_date']

    class Admin:
        pass

    def __str__(self):
        return self.title

    def get_tags(self):
        return Tag.objects.get_for_object(self) 

    def get_absolute_url(self):
        return "/projects/%s/%s/" % (self.PROJECT_CATEGORY[self.project_type][1], self.slug)
