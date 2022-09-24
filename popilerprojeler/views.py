from django.shortcuts import render
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from popilerprojeler.models import Category,pp


# Create your views here.





# Create your views here.
def pp_index(request):
    category=Category.objects.all()
    pps=pp.objects.all()

    context={'category': category, 'pps':pps
    
    }
    
    return render(request,"home.html",context,)
    

