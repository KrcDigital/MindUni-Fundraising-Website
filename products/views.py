from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
#from products.models import Product,ProductImage
from haberler.models import *


def detail(request,product_id):
   # productimage=ProductImage.objects.filter(product=product_id)
    popiler=popilerhaber.objects.filter()

   # try:
       # product= Product.objects.get(pk=product_id)
    #except Product.DoesNotExist:
        #raise Http404("Product does not exist") 

    context={'product':"product",
    'productimage':"productimage",
    "popiler":popiler,
    }   
    return render(request,'detail.html',context)    
    