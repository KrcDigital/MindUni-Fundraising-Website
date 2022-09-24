from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.Model):
    
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )


    parentid=models.IntegerField()
    title= models.CharField(max_length=150)
    
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Category2(models.Model):
    
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )


    parentid=models.IntegerField()
    title= models.CharField(max_length=150)
    
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

        

class Category3(models.Model):
    
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )


    parentid=models.IntegerField()
    title= models.CharField(max_length=150)
    
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



class Category4(models.Model):
    
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )


    parentid=models.IntegerField()
    title= models.CharField(max_length=150)
    
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Category5(models.Model):
    
    STATUS=(
        (1, 'True'),
        (0, 'False'),


    )


    parentid=models.IntegerField()
    title= models.CharField(max_length=150)
    
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey('auth.User',verbose_name="User",on_delete = models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Proje Kategorisini Seçiniz")
    category2=models.ForeignKey(Category2,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Proje Kategorisini Seçiniz")
    category3=models.ForeignKey(Category3,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Proje Kategorisini Seçiniz")
    category4=models.ForeignKey(Category4,null=True,blank=True,on_delete=models.CASCADE)
    category5=models.ForeignKey(Category5,null=True,blank=True,on_delete=models.CASCADE)



    title=models.CharField(max_length=120, verbose_name="Proje Başlığınızı Giriniz")
    content=RichTextField(verbose_name="Projenizi Tanıtın")
    date=models.DateTimeField(verbose_name="Tarih",auto_now_add=True)
    image= models.ImageField(null=True,blank=True,verbose_name="Proje Resminizi Seçiniz")
    image2= models.ImageField(null=True,blank=True,verbose_name="Proje Resminizi Seçiniz")
    image3= models.ImageField(null=True,blank=True,verbose_name="Proje Resminizi Seçiniz")
    image4= models.ImageField(null=True,blank=True,verbose_name="Proje Resminizi Seçiniz")


    slug=models.SlugField(unique=True,editable=False,max_length=130)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
      # return "/project/{}".format(self.id)
       return reverse("post:detail", kwargs={"slug":self.slug})


    def get_unique_slug(self):
        slug=slugify(self.title.replace("ı","i"))
        unique_slug=slug
        counter= 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug='{}-{}'.format(slug,counter)
            counter +=1
        return unique_slug    


    def save(self, *args, **kwargs):
        if not self.slug:
            
            self.slug=self.get_unique_slug()
        return super(Post,self).save(*args, **kwargs) 

    class Meta:
           ordering=["-date","id"]
        




class UserProfile(models.Model):
    cins=((None,"Cinsiyet Seçiniz"),("diğer","DİĞER"),("erkek","ERKEK"),("kadın","KADIN"))
    
    bakiye=models.TextField(max_length=1000,verbose_name="bakiye",blank=True,null=True)
    bio=models.TextField(max_length=1000,verbose_name="bio",blank=True,null=True)
    kod=models.CharField(max_length=1000,verbose_name="kod",blank=True,null=True)

    CİNS=models.CharField(choices=cins,max_length=6,verbose_name="Cinsiyet",blank=False,null=True)
    foto=models.ImageField(null=True,blank=True,verbose_name="Profil Fotoğrafı")
    dotarihi=models.DateField(null=True,blank=True,verbose_name="Doğum Tarihi")
    user=models.OneToOneField(User,null=True,blank=False,verbose_name="User",on_delete=models.CASCADE)

    def get_user_profile_url(self):
        path=reverse('profile',kwargs={'username':self.user.username})
        return path

    def get_bakiye(self):
        if self.bio:
            return self.bio
        return "Bio Yeri"  

    

    def get_bio(self):
        if self.bakiye:
            return self.bakiye
        return "0"    

    def get_foto(self):
        if self.foto:
            return self.foto.url    
        return "/static/image/prp.jpg"    

    class Meta:
        verbose_name_plural="User Profile"

    def  get_screen_name(self):
        user=self.user
        if user.get_full_name():
            return user.get_full_name()
        return user.username    

    def __str__(self):
        return "%s Profile" % (self.get_screen_name())


class FavoriteBlog(models.Model):
    user=models.ForeignKey(User,null=True,default=1,related_name='favorite_blog',on_delete=models.CASCADE)
    Post=models.ForeignKey(Post,null=True,related_name='favorite_blog',on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural="Favorilere Eklenen Gönderiler"

    def __str__(self):
        return "%s Profile" % (self.user,self.project)


        
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)





