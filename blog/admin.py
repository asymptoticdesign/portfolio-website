from django.contrib import admin
from models import Entry, Link

class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    unique_for_date='publish_date'

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    unique_for_date='publish_date'
    
admin.site.register(Link, LinkAdmin)
admin.site.register(Entry, EntryAdmin)
