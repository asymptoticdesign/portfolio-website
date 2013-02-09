from portfolio.models import Tag, Project
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Project,ProjectAdmin)
#admin.site.register(Client)
admin.site.register(Tag)
