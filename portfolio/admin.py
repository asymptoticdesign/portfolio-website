from portfolio.models import Category, Project
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Project,ProjectAdmin)
#admin.site.register(Client)
admin.site.register(Category)
