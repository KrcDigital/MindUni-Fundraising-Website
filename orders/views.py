from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404,reverse,Http404
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404,reverse
from django.contrib.auth import authenticate, login, logout
from django.utils.text import slugify
from post.models import UserProfile,Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.forms import ModelForm
#from products import *
#from products.views import *
#from products.models import Product,Category
from django.utils.crypto import get_random_string

#from products.models import Product,ProductImage
#from orders.models import *

from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail


from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

UserModel = get_user_model()






@login_required(login_url='/auths/login/')     
def index(request):
    current_user=request.user
    orders=Order.objects.all().filter(user_id=current_user.id)

    context={'page':'orders',
             'orders':orders,   
    }

    return render(request,'myorders.html',context)



@login_required(login_url='/auths/login/')
def shop_cart_list(request):
    current_user=request.user
    shopcart=ShopCart.objects.all().filter(user_id=current_user.id)
    carttotal=0
    for rs in shopcart:
        carttotal+=rs.quantity * rs.product.kuponprice

    context={'page':'cart',
             'shopcart':shopcart,
             'carttotal':carttotal,   
    
    }    

    return render(request,'shop_cart_list.html',context)


# Create your views here.

@login_required(login_url='/auths/login/')
def addtocart(request,id):

    url=request.META.get('HTTP_REFERER')
    
    if request.method=='POST':
        form=ShopCartForm(request.POST)
        if form.is_valid():
           current_user=request.user

           data=ShopCart()
           data.user_id=current_user.id 
           data.product_id=id
           data.quantity=form.cleaned_data['quantity']
           data.save()
           
           return HttpResponseRedirect(url)

    if id:
        current_user=request.user
        data=ShopCart()
        data.product_id=id
        data.quantity=1
        data.save()
        return HttpResponseRedirect(url)



@login_required(login_url='/auths/login/')
def deletefromcart(request,id):
    url=request.META.get('HTTP_REFERER')
    ShopCart.objects.filter(id=id).delete()
    messages.success(request,"Ürünü Sepetinizden Kaldırdınız")
    return HttpResponseRedirect(url)


@login_required(login_url='/auths/login/')
def shopcart(request):
    category=Category.objects.all()
    product=Product.objects.all()
    current_user=request.user
    schopcart=ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in schopcart:
        total+=rs.product.kuponprice * rs.quantity

    context={'schopcart':schopcart,
    'category':category,
    'total':total,
    'product':product,
    } 

    return render(request,'cartol.html',context)   


  
@login_required(login_url='/auths/login/')     
def checkout(request):
    current_user=request.user
    shopcart=ShopCart.objects.all().filter(user_id=current_user.id)
    carttotal=0
    for rs in shopcart:
        carttotal+=rs.quantity * rs.product.kuponprice

    form=OrderForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            data=Order()
            data.name=form.cleaned_data['name']
            data.surname=form.cleaned_data['surname'] 
            
            data.address=form.cleaned_data['address']
            data.city=form.cleaned_data['city']   
            data.phone=form.cleaned_data['phone']
            data.to=form.cleaned_data['name']
            data.user_id=current_user.id
            data.total=carttotal
            ordercode=get_random_string(5).upper()
            data.code=ordercode
            data.save()

            for rs in shopcart:
                detail=OrderDetail()
                detail.order_id=data.id
                detail.product_id=rs.product_id
                detail.user_id=current_user.id
                detail.price=rs.product.price
                detail.quantity=rs.quantity
                detail.product=rs.product
                detail.kuponprice=rs.product.kuponprice
                detail.total=rs.amount
                detail.save()

                product=Product.objects.get(id=rs.product_id)
                product.amount -=rs.quantity
                product.save()


            user=request.user
            emaily=user.email   
            htmly     = get_template('mail/siparis.html')
            html_content = htmly.render()
            subject, from_email = 'Siparişiniz Alındı.', 'krc@minduni.org'

            email = EmailMultiAlternatives(subject,  from_email, to=[emaily])
            email.attach_alternative(html_content, "text/html")
            email.send()
            print (emaily)


            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items']=0
            messages.success(request,"Siparişiniz Alınmıştır")
            return HttpResponseRedirect("/order")    

        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order")
    context={'page':'checkout',
             'shopcart':shopcart,
             'carttotal':carttotal,   
    }
    return render(request,'checkout.html',context)



@login_required(login_url='/auths/login/')     
def order_detail(request,id):
    order=Order.objects.get(pk=id)
    items=OrderDetail.objects.all().filter(order=id)


    context={'page':'detail',
             'order':order,
             'items':items,

    }

    return render(request,'orderdetail.html',context)


