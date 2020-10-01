from django import forms
from .models import Comment , Post
from django.core import validators


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writer', 'comment')



class updateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
       