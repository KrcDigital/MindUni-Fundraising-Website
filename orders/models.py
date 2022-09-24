from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput
#from products.models import Product
from django import forms

class ShopCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    #product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()
    

    def __str__(self):
        return 

    @property
    def amount(self):
        return 

    @property
    def price(self):
        return 



class ShopCartForm(ModelForm):
    class Meta:
        model= ShopCart
        fields=['quantity']
    
class Order(models.Model):
    STATUS=(
        ('Yeni','Yeni'),
        ('Yetersiz Bakiye','Yetersiz Bakiye'),
        ('Onaylandı','Onaylandı'),
        ('Hazırlanıyor','Hazırlanıyor'),
        ('Teslimatta','Teslimatta'),
        ('Tamamlandı','Tamamlandı'),
        ('İptal Edildi','İptal Edildi'),
    )

    



    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=5,editable=False)
    name=models.CharField(max_length=10)
    surname=models.CharField(max_length=10)

    address=models.CharField(max_length=250)
    city=models.CharField(max_length=20,blank=True)
    phone=models.CharField(max_length=20)
    total=models.FloatField()
    note=models.TextField(null=True,default="")
    status=models.CharField(choices=STATUS,default='Yeni',max_length=15)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

   

class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
    
class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields=['name','surname','address','city','phone']
        widgets={
            'name':TextInput(attrs={'class':'input'}),
            'surname':TextInput(attrs={'class':'input'}),

            'address':TextInput(attrs={'class':'input'}),
            'phone':TextInput(attrs={'class':'input'}),
        }

        