from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': '', #Add class to reduce the area of the body field
        'placeholder': 'Comment here',
        'rows': 4,
        'cols': 50,
    }))
    class Meta:
        model = Comment
        fields = ['body']