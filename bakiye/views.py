from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .forms import KuponForm,odemeForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Kupon,odemebilgi
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
# Create your views here.

    

def kupon(request):
     
    if not request.user.is_authenticated:
         raise Http404()
    
    
    
  #( title=request.POST.get("title")
   # content=request.POST.get("content"
    #Post.objects.create(title=title, content=content) )

    
        #FORMU KAYDET
    form=KuponForm(request.POST or None, request.FILES or None)
    if form.is_valid():
         
          kupon=  form.save(commit=False)
          kupon.user=request.user
          kupon.save()
          messages.success(request,"Kodunuz Kontrol Edildikten Sonra Bakiyenize Yansıyacaktır...")
          return HttpResponseRedirect('/auths/profile/')
    
    context={
        "form": form,}
    return render(request,'auth/kupon.html',context)



def odemebilgi(request):
     
    if not request.user.is_authenticated:
         raise Http404()
    
    
    
  #( title=request.POST.get("title")
   # content=request.POST.get("content"
    #Post.objects.create(title=title, content=content) )

    
        #FORMU KAYDET
    form=odemeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
         
          odeme=  form.save(commit=False)
          odeme.user=request.user
          odeme.save()
          messages.success(request,"Ödeme Numaranız Kontrol Edildikten Sonra Bakiyenize Yansıyacaktır...")
          return HttpResponseRedirect('/auths/profile/')
    
    context={
        "form": form,}
    return render(request,'auth/odeme_bildirimi.html',context)







def bakiye_ekle(request):
     
    if not request.user.is_authenticated:
         raise Http404()
    
    
    
  

    
       
    
    return render(request,'auth/bakiye_ekle.html')





    




