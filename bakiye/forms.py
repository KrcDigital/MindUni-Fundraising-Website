from django import forms
from .models import Kupon,odemebilgi
from django import forms


class KuponForm(forms.ModelForm):
  
    class Meta:
        model=Kupon
        fields=[
            
            "kupon",
            
        
        ]



class odemeForm(forms.ModelForm):
  
    class Meta:
        model=odemebilgi
        fields=[
            
            "numara",
            
        
        ]

