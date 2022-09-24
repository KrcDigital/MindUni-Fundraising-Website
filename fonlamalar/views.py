from django.shortcuts import render
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from fonlamalar.models import Category,Fon,FonImage
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from .forms import CommentForm



# Create your views here.


from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404


def fon_detail(request,fon_id):
    fonimage=FonImage.objects.filter(fon=fon_id)

    #try:
    fon= Fon.objects.get(pk=fon_id)
    #except Product.DoesNotExist:
        #raise Http404("Fon does not exist") 

    comments = fon.comments.filter()
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
            new_comment.fon = fon
            # Save the comment to the database
            new_comment.save()
            
            return redirect ("/fonlama")
    else:
        comment_form = CommentForm()



    context={'fon':fon,'fonimage':fonimage,'comments': comments,
                                           'comment_form': comment_form
    }   
    return render(request,'fonlama/fon.html',context)    
    


# Create your views here.
def fon_index(request):
    category=Category.objects.all()
    fons=Fon.objects.all()

    context={'category': category, 'fons':fons
    
    }
    return render(request,"fonlama/index.html",context)
    
    


def detay(request):
        
  
    return render(request,'fonlama/detay.html') 






    