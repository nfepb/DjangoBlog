from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm

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
        comments = post.comments.filter(approved=True).order_by('-created_on')
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
                "commented": False,
                "liked": liked,
                # Adding new key
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get all the data from the form and assign to variable
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            # Calling on the save method:
            comment = comment_form.save(commit=False)
            # Assign comment to a post
            comment.post = post
            # Commit save only after associating with post
            comment.save()

        else:
            # If form is not valid, return empty form instance
            comment_form = CommentForm()

        # Return all information with the 'render' method
        return render(
            request,
            "post_detail.html",
            # Dictionnary supplying context:
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                # Adding new key
                "comment_form": CommentForm()
            }
        )
