from django import forms
from .models import Post ,Comment, FreePost, FreeComment

class Postform(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    # fields = ['title', 'body']

class Commentform(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']


class FreePostform(forms.ModelForm):
  class Meta:
    model = FreePost
    fields = '__all__'
    # fields = ['title', 'body']

class FreeCommentform(forms.ModelForm):
  class Meta:
    model = FreeComment
    fields = ['comment']