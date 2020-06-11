from django import forms
from .models import Comment
from django.core import validators


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writer', 'comment')
