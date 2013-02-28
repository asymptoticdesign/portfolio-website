from portfolio.models import Project
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

#class CategoryAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Project,ProjectAdmin)
