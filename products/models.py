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



class Product(models.Model):


      
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )



    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title= models.CharField(max_length=150)
    keywords= models.CharField(max_length=255,blank=True)
    description= models.CharField(max_length=255,blank=True)
    image= models.ImageField()
    price=models.FloatField()
    kuponprice=models.IntegerField()
    amount=models.IntegerField()
    detail=models.TextField()
    seller=models.TextField(blank=True)
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    satilan=models.IntegerField()

    def __str__(self):
        return self.title        

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image= models.ImageField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

       