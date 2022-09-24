from django.db import models
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )


    parentid=models.IntegerField()
    title= models.CharField(max_length=150)
    keywords= models.CharField(max_length=255,blank=True)
    description= models.CharField(max_length=255,blank=True)
    image= models.ImageField()
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



class Fon(models.Model):


      
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )


    user = models.ForeignKey('auth.User',verbose_name="User",on_delete = models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title= models.CharField(max_length=150)
    keywords= models.CharField(max_length=255,blank=True)
    description= models.CharField(max_length=255,blank=True)
    image= models.ImageField()
    dislike=models.IntegerField()
    like=models.IntegerField()
    güncelfon=models.IntegerField()
    hedef=models.IntegerField()
    oran=models.IntegerField()
    detail=models.TextField()
    seller=models.TextField(blank=True)
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    satilan=models.IntegerField()
    slug=models.SlugField(unique=False,editable=False,max_length=130)


    def __str__(self):
        return self.title        

class FonImage(models.Model):
    fon=models.ForeignKey(Fon,on_delete=models.CASCADE)
    image= models.ImageField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

       
       

class Comment(models.Model):
    fon = models.ForeignKey(Fon,on_delete=models.CASCADE,related_name='comments')
    isim = models.CharField(max_length=80)

    email= models.EmailField()
    yorum = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Yorum {} Tarafından {}'.format(self.yorum, self.isim)