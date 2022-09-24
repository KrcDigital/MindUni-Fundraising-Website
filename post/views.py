from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Post,UserProfile,FavoriteBlog
from .forms import PostForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post,Category,Category2,Category3,Category4,Category5
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
def project_index(request):
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
    
    
    return render(request,"post/index.html",{"posts":posts})
    return render(request,"post/detail.html",{"posts":posts})
    

def project_create(request):
     
    if not request.user.is_authenticated:
         raise Http404()
    
    
    
  #( title=request.POST.get("title")
   # content=request.POST.get("content"
    #Post.objects.create(title=title, content=content) )

    
        #FORMU KAYDET
    form=PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
         
          post=  form.save(commit=False)
          post.user=request.user
          post.save()
          messages.success(request,"Proje Gönderildi...")
          return HttpResponseRedirect(post.get_absolute_url())
    
    context={
        "form": form,}
    return render(request,'post/form.html',context)



def project_update(request,slug):
    if not request.user.is_authenticated:
         raise Http404()
    post=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,"Proje Güncellendi...")
        return HttpResponseRedirect(post.get_absolute_url())
    context={
        "form": form,}
    return render(request, "post/form.html",context,renderer=None)

def project_delete(request,slug):
    if not request.user.is_authenticated:
         raise Http404()
    post=get_object_or_404(Post,slug=slug)
    post.delete()
    return redirect("post:index")
    
    
def add_or_remove_favorite(request,slug):
    url = request.GET.get('url',None)
    post=get_object_or_404(Post,slug=slug)
    favori_blog= FavoriteBlog.objects.filter(post=post,user=request.user)
    if favori_blog.exists():
        favori_blog.delete()
    else:
        FavoriteBlog.objects.create(post=post,user=request.user)    
    if not url:
        url = reversed('project_detail')
    return HttpResponseRedirect(url)    



def project_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    
    comments = post.comments.filter()
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
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            
            return redirect ("/project/index")
    else:
        comment_form = CommentForm()

    return render(request, "post/detail.html", {'post': post,
                                           'comments': comments,
                                           'comment_form': comment_form})    


