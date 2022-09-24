from django import forms
from .models import Gonderiler
from .models import Comment
from django import forms


class GonderiForm(forms.ModelForm):
  
    class Meta:
        model=Gonderiler
        fields=[
            "content",
            "image",
        
        ]


