from django import forms
from .models import Post
from .models import Comment,Category
from django import forms


class PostForm(forms.ModelForm):
  
    class Meta:
        model=Post
        fields=[
            "title",
            "content",
            "image",
            "image2",

            "image3",
            "image4",


            "category",
            "category2",
            "category3",
        
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
