from django.contrib import admin
from .models import *

@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email']
    list_filter = ['created_at']