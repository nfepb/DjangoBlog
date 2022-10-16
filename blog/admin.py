from django.contrib import admin
from .models import Post

# Register your models here.
# Adds Post model to admin panel to allow moderation
admin.site.register(Post)
