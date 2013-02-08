from django.db import models

PROJECT_CATEGORY = (('S','Science'),
                    ('A','Art'),
                    ('T','Technology'))

class Tag(models.Model):
    name = models.CharField(max_length=256)
    
    class Meta:
        db_table = "portfolio_tags"
        verbose_name_plural = "tags"
        ordering = ['name']

    class Admin:
        pass
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField()
    project_type = models.CharField(max_length=1, choices=PROJECT_CATEGORY)
    project_url = models.URLField('Project URL')
    summary = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
#    date_started = models.DateField()
#    date_completed = models.DateField()
    completion_date = models.DateField()
    is_public = models.BooleanField(default=False)
    overview_image = models.URLField()
    
    class Meta:
        db_table = "projects"
        ordering = ['-completion_date']
     
    class Admin:
        pass
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/work/%s/" % self.slug
