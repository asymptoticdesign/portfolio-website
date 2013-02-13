from django.contrib import admin
from models import Category, Entry, Link

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    unique_for_date='publish_date'

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    unique_for_date='publish_date'
    
admin.site.register(Link, LinkAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
