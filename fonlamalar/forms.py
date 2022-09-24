from django import forms
from .models import Comment,Fon






class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('isim', 'email', 'yorum')
