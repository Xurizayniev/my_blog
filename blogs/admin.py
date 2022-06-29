from django.contrib import admin
from .models import BlogModel, CategoryModel
# Register your models here.

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']