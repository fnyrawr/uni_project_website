from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'creator': forms.HiddenInput(),
            'timestamp': forms.HiddenInput(),
        }


class SearchForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'creator', 'timestamp']
