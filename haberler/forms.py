from django import forms
from .models import Comment,Haberler






class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('isim', 'email', 'yorum')
