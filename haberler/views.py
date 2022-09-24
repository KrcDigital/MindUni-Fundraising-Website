from django.shortcuts import render
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from haberler.models import Haberler,HaberlerImage,guncelhaber,popilerhaber,editorhaber
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from .forms import CommentForm
from datetime import datetime
from django.contrib.auth import get_user_model


# Create your views here.


from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404


def haberler_detail(request,slug):
    haberler = get_object_or_404(Haberler, slug=slug)
    guncel=guncelhaber.objects.filter()
    haber=Haberler.objects.all()
    tekno=Haberler.objects.filter(category="Teknoloji")
    sosyal=Haberler.objects.filter(category="Sosyal")
    gelecek=Haberler.objects.filter(category="Gelecek")
    editor=editorhaber.objects.filter()
    popiler=popilerhaber.objects.filter()


   
    

    comments = haberler.comments.filter()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
                  

        if not request.user.is_authenticated:
         raise Http404()
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.haberler = haberler
            # Save the comment to the database
            new_comment.save()
            
            return redirect ("/haberler/")
    else:
        comment_form = CommentForm()


    context={ 'haber':haber, 'tekno':tekno, 'sosyal':sosyal, 'gelecek':gelecek, 'guncel':guncel,'editor':editor,'haberler':haberler,'comments': comments,
                                           'comment_form': comment_form,'popiler':popiler
    
    }

      
    return render(request,'haberler/detail.html',context)    
    


# Create your views here.
def haberler_index(request):
    guncel=guncelhaber.objects.filter()
    popiler=popilerhaber.objects.filter()
    editor=editorhaber.objects.filter()

    haber=Haberler.objects.all()
    tekno=Haberler.objects.filter(category="Teknoloji")
    sosyal=Haberler.objects.filter(category="Sosyal")
    gelecek=Haberler.objects.filter(category="Gelecek")

    context={ 'haber':haber, 'tekno':tekno, 'sosyal':sosyal, 'gelecek':gelecek, 'guncel':guncel,'editor':editor,'popiler':popiler
    
    }
    return render(request,"haberler/index.html",context)
    return render(request,"base.html",context)
    return render(request,"base.html",context)



def teknoloji_index(request):
    guncel=guncelhaber.objects.filter()
    popiler=popilerhaber.objects.filter()
    editor=editorhaber.objects.filter()

    haber=Haberler.objects.all()
    tekno=Haberler.objects.filter(category="Teknoloji")
    
    context={ 'haber':haber, 'tekno':tekno,'guncel':guncel,'editor':editor,'popiler':popiler
    
    }
    return render(request,"haberler/teknoloji.html",context)
    
    
    
def sosyal_index(request):
    guncel=guncelhaber.objects.filter()
    popiler=popilerhaber.objects.filter()
    editor=editorhaber.objects.filter()

    haber=Haberler.objects.all()
    sosyal=Haberler.objects.filter(category="Sosyal")
    
    context={ 'haber':haber, 'sosyal':sosyal,'guncel':guncel,'editor':editor,'popiler':popiler
    
    }
    return render(request,"haberler/sosyal.html",context)
    





def gelecek_index(request):
    guncel=guncelhaber.objects.filter()
    popiler=popilerhaber.objects.filter()
    editor=editorhaber.objects.filter()

    haber=Haberler.objects.all()
    gelecek=Haberler.objects.filter(category="Gelecek")
    
    context={ 'haber':haber, 'gelecek':gelecek,'guncel':guncel,'editor':editor,'popiler':popiler
    
    }
    return render(request,"haberler/gelecek.html",context)


    