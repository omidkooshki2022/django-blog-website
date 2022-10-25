from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title', 'description', 'text', 'author', 'status']