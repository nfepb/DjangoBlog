from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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


class PostDetail(View):
    # *args = other arguments, *kwargs = other key arguments
    def get(self, request, slug, *args, **kwargs):
        # Filter posts to only have active ones:
        queryset = Post.objects.filter(status=1)
        # Get published post with correct slug
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        # Check if user has liked the post
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Return all information with the 'render' method
        return render(
            request,
            "post_detail.html",
            # Dictionnary supplying context:
            {
                "post": post,
                "comments": comments,
                "liked": liked
            }
        )
