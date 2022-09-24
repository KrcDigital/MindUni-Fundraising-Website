from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm,TextInput

# Create your models here.





class Gonderiler(models.Model):
    user = models.ForeignKey('auth.User',verbose_name="User",on_delete = models.CASCADE)
  


    content=RichTextField(verbose_name="Gönderinizi Giriniz")
    date=models.DateTimeField(verbose_name="Tarih",auto_now_add=True)
    image= models.ImageField(null=True,blank=True,verbose_name="Gönderinize Resim Ekleyebilirsiniz")
    
    


    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-date']


   
        








        
class Comment(models.Model):

    STATUS=(
        ('New','Yeni'),
        ('True','Evet'),
        ('Falsa','Hayır'),
    )

    gonderi=models.ForeignKey(Gonderiler,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120,blank=True)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip=models.CharField(blank=True,max_length=20)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

class CommentForm(ModelForm):
    class Meta:
            model=Comment
            fields=['comment']   
    




