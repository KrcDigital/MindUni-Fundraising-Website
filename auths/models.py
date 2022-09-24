from django.db import models
from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404,reverse
from django.contrib.auth.models import User

# Create your models here.
def get_user_profile(self):
    url=reverse('user_profile')
    return url

class Donate(models.Model):


      
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )

    veren=models.ForeignKey(User,related_name="veren",verbose_name="Veren",on_delete = models.CASCADE)
    alan=models.ForeignKey(User,related_name="alan",verbose_name="Alan",on_delete = models.CASCADE)
    miktar=models.IntegerField()
    proje=models.CharField(max_length=150)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.proje        
