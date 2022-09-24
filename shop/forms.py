from django import forms
from .models import shop,Comment



class shopForm(forms.ModelForm):
  
    class Meta:
        model=shop
        fields=[
            "Ürün",
            "Açıklama",
            "Fiyat",
            "image",
        
        ]


