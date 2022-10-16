from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# Adds decorator to register Post model & PostAdmin class to site
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # To add filtering panel based on selected fields:
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
