from django.contrib import admin

# Register your models here.
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'creation_date', 'is_published', 'views_count']
    list_filter = ['is_published', ]
