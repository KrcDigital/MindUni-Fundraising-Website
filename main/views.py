from django.shortcuts import render,HttpResponse
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from post.models import Post,UserProfile
from post.forms import PostForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from popilerprojeler.models import Category,pp
from haberler.models import *

# Create your views here.



def main(request):


    category=Category.objects.all()
    pps=pp.objects.all()
    popiler=popilerhaber.objects.filter()


    post_list=Post.objects.all()

    
    paginator = Paginator(post_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)


    context={'category': category, 'pps':pps ,"posts":posts,"popiler":popiler,}    


    return render(request,"home.html",context,)






        