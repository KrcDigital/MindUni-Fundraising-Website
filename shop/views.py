from django.shortcuts import render
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from products.models import Category,Product
from haberler.models import *


# Create your views here.
def shop_index(request):
    category=Category.objects.all()
    products=Product.objects.all()
    popiler=popilerhaber.objects.filter()

    context={'category': category, 'products':products,"popiler":popiler,
    
    }
    return render(request,"shop/index.html",context)

def shop_detail(request):

    return render(request,"shop/detail.html")    


    
def product(request):

        
    return render(request,"shop/product.html")   


def odeme(request):

        
    return render(request,"shop/odeme.html")   


        
        