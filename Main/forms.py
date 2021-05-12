from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    intro = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))

    class Meta:
        model = Post
        fields = ['title', 'slug', 'intro', 'body']
