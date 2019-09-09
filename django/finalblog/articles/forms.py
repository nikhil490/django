from .models import Article, Comment
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('Author', 'Title', 'Content', 'thumb', 'types')
        widgets = {
            'title': forms.Textarea(attrs={'cols': 50, 'rows': 2}),
            'body': forms.Textarea(attrs={'cols': 130, 'rows': 10}),
            'author': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 120, 'rows': 2}),
        }


class AnonymousCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        author = 'Anonymous'
        fields = ('text',)

        widgets = {

            'text': forms.Textarea(attrs={'cols': 120, 'rows': 2}),
        }