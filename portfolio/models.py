from django.db import models

PROJECT_CATEGORY = (('S','Science'),
                    ('A','Art'),
                    ('T','Technology'))

class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True,help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ['title']

    class Admin:
        pass
    
    def __str__(self):
        return self.title
    
class Project(models.Model):
    #constants
    DRAFT_STATUS = 0
    HIDDEN_STATUS = 1
    LIVE_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
        (LIVE_STATUS, 'Live'))

    SCI_CAT = 0
    ART_CAT = 1
    TECH_CAT = 2
    PROJECT_CATEGORY = (
        (SCI_CAT,'Science'),
        (ART_CAT,'Art'),
        (TECH_CAT,'Technology'))
    
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    summary = models.CharField(max_length=512)
    overview_image = models.URLField()
    description = models.TextField(blank=True)
    start_date = models.DateField()
    completion_date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    project_type = models.IntegerField(choices=PROJECT_CATEGORY)
    categories = models.ManyToManyField(Category)
    
    class Meta:
        ordering = ['-completion_date']
     
    class Admin:
        pass
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/work/%s/%s/" % (self.PROJECT_CATEGORY[status][1], self.slug)
