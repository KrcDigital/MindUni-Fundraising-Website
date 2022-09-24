from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Fallowing(models.Model):
    fallow=models.ForeignKey(User,related_name="fallow",verbose_name="Takip Eden Kullanıcı",on_delete = models.CASCADE)
    fallowed=models.ForeignKey(User,related_name="fallowed",verbose_name="Takip Edilen Kullanıcı",on_delete = models.CASCADE)


    class Meta:
        verbose_name_plural="Fallowing"

    def save(self,*args,**kwargs):
        if (self.fallow!=self.fallowed):
           return super(Fallowing,self).save(*args,**kwargs)
        print("Kendinizi Takip Edemezsiniz")   

    def __str__(self):
        return "Fallow{} - Fallowed{}".format(self.fallow,self.fallowed)
 


    @staticmethod

    def add_or_delete_fallowed(fallowed,fallow):
        data={}
        value=Fallowing.objects.filter(fallowed=fallowed,fallow=fallow)
        if value.exists():
            value.delete()
            count=Fallowing.get_fallowed_count(user=fallowed) 
            data={'msg':'Takip Et ✚','count':count}
            return data
        Fallowing.objects.create(fallowed=fallowed,fallow=fallow)
        count=Fallowing.get_fallowed_count(user=fallowed)
        data={'msg':"Takibi Bırak ✘",'count':count} 
        return data 

    @staticmethod
    def get_fallowed(user):
        takipciler=Fallowing.objects.filter(fallowed=user)
        return takipciler

    @staticmethod    
    def get_fallowed_count(user):
        takipciler_sayisi= Fallowing.objects.filter(fallowed=user).count()
        return takipciler_sayisi



    @staticmethod
    def get_fallow(user):
        takip_edilenler=Fallowing.objects.filter(fallow=user)   
        return takip_edilenler


    @staticmethod
    def get_fallow_count(user):
        takip_edilen_sayisi=Fallowing.objects.filter(fallow=user).count()    
        return takip_edilen_sayisi
   


   