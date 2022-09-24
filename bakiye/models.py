from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm,TextInput

# Create your models here.





class Kupon(models.Model):
    user = models.ForeignKey('auth.User',verbose_name="User",on_delete = models.CASCADE)
    


    kupon=models.CharField(max_length=120, verbose_name="Kuponunuzu Giriniz")
    date=models.DateTimeField(verbose_name="Tarih",auto_now_add=True)
    
    def __str__(self):
        return self.kupon


class odemebilgi(models.Model):
    user = models.ForeignKey('auth.User',verbose_name="User",on_delete = models.CASCADE)
    


    numara=models.CharField(max_length=120, verbose_name="Ödeme Numaranızı Giriniz")
    date=models.DateTimeField(verbose_name="Tarih",auto_now_add=True)
    
    def __str__(self):
        return self.numara

   
        












