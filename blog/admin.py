from django.contrib import admin
from models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    unique_for_date='publish_date'
    

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
