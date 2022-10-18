from django.shortcuts import render
from django.views import generic
from .models import Post

"""
Class-based Views
In order to make views that are reusable,
which can inherit from each other
"""


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # Limit number of Posts that can appear:
    paginate_by = 6
