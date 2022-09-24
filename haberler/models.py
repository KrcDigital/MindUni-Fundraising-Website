from django.db import models
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.




class Haberler(models.Model):


      
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )


    user = models.ForeignKey('auth.User',verbose_name="User",on_delete = models.CASCADE)
    category=models.CharField(max_length=150)
    title= models.CharField(max_length=150)
    keywords= models.CharField(max_length=255,blank=True)
    ozet= models.CharField(max_length=255,blank=True)
    image= models.ImageField()
    dislike=models.IntegerField()
    like=models.IntegerField()
    detail=RichTextField()

    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    slug=models.SlugField(unique=True,editable=False,max_length=130)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
      # return "/haberler/{}".format(self.id)
       return reverse("haberler:detail", kwargs={"slug":self.slug})


    def get_unique_slug(self):
        slug=slugify(self.title.replace("ı","i"))
        unique_slug=slug
        counter= 1
        while Haberler.objects.filter(slug=unique_slug).exists():
            unique_slug='{}-{}'.format(slug,counter)
            counter +=1
        return unique_slug    


    def save(self, *args, **kwargs):
        if not self.slug:
            
            self.slug=self.get_unique_slug()
        return super(Haberler,self).save(*args, **kwargs) 




    def __str__(self):
        return self.title        



    class Meta:
        ordering = ['-create_at']



   




class HaberlerImage(models.Model):
    haberler=models.ForeignKey(Haberler,on_delete=models.CASCADE)
    image= models.ImageField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

       
       

class Comment(models.Model):
    haberler = models.ForeignKey(Haberler,on_delete=models.CASCADE,related_name='comments')
    isim = models.CharField(max_length=80)

    email= models.EmailField()
    yorum = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Yorum {} Tarafından {}'.format(self.yorum, self.isim)





class guncelhaber(models.Model):


      
    


    haber=models.ForeignKey(Haberler,on_delete=models.CASCADE)


class popilerhaber(models.Model):


      
    


    haber=models.ForeignKey(Haberler,on_delete=models.CASCADE)


class editorhaber(models.Model):


      
    


    haber=models.ForeignKey(Haberler,on_delete=models.CASCADE)