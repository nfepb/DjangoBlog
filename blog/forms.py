from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        # Telling our class what model to use
        model = Comment
        # Define which fields to use. ',' is crucial
        # Otherwise Python will read as string instead of tuple --> error
        fields = ('body',)
