from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .forms import GonderiForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Gonderiler,CommentForm,Comment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from haberler.models import *
# Create your views here.
def gonderiler_index(request):
    gonderi_list=Gonderiler.objects.all()
    paginator = Paginator(gonderi_list, 25) # Show 25 contacts per page
    popiler=popilerhaber.objects.filter()

    page = request.GET.get('page')
    try:
        gonderiler = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gonderiler = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gonderiler = paginator.page(paginator.num_pages)

    comments=Comment.objects.all()   
    context={
        "comments":comments,
        "gonderiler":gonderiler,
        "popiler":popiler,
    }
    
    return render(request,"gonderi/index.html",context)
    

def gonderi_create(request):
     
    if not request.user.is_authenticated:
         raise Http404()
    
    
    
  #( title=request.POST.get("title")
   # content=request.POST.get("content"
    #Post.objects.create(title=title, content=content) )

    
        #FORMU KAYDET
    form=GonderiForm(request.POST or None, request.FILES or None)
    if form.is_valid():
         
          gonderi=  form.save(commit=False)
          gonderi.user=request.user
          gonderi.save()
          messages.success(request,"Gönderi Gönderildi...")
          return HttpResponseRedirect('/gonderi/')
    
    context={
        "form": form,}
    return render(request,'gonderi/form.html',context)



@login_required(login_url='/login')
def addcomment(request,id):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user

            data=Comment()
            data.user_id=current_user.id
            data.gonderi_id=id
            data.comment=form.cleaned_data['comment']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Yorumunuz Gönderildi")
            url=request.META.get('HTTP_REFERER')
            return render(request,'gonderi/yorumlar.html')


    return HttpResponse("Yorum Gönderilemedi")
    
    




   


