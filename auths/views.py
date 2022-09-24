from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404,reverse,Http404
from .forms import LoginForm, RegisterForm,UserProfileUpdateForm
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404,reverse
from .forms import LoginForm, RegisterForm,UserProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.utils.text import slugify
from post.models import UserProfile,Post
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from takip.models import Fallowing
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from .models import Donate
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
from haberler.models import *

UserModel = get_user_model()










def postlar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login_view'))
    
    postlar=Post.objects.filter(user=request.user)
    context={
        "postlar":postlar

    }
    return render(request,"auth/profile/profile.html",context)

def login_view(request):
    if  request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/')

    return render(request, "auth/form.html", {"form": form, 'title': 'Giriş Yap'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        email=form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        userprofile=UserProfile.objects.create(user=user)
        new_user = authenticate(username=user.username, password=password,email=email)
        login(request,new_user)
        current_site = get_current_site(request)

        htmly     = get_template('auth/acc_active_email.html')
        html_content = htmly.render()
        to_email = form.cleaned_data.get('email')
        
        subject, from_email = 'Tebrikler MindUni Hesabınız Oluşturuldu.', 'krc@minduni.org'

        email = EmailMultiAlternatives(subject,  from_email, to=[to_email])
        email.attach_alternative(html_content, "text/html")
        email.send()



            






        return redirect('/')     

    return render(request, "auth/form.html", {"form": form, 'title': 'Üye Ol'})
    
    
def logout_view(request):
    logout(request)
    return redirect('/')

def user_settings(request):
    foto=request.user.userprofile.foto
    bio=request.user.userprofile.bio
    

    initial={'foto':foto,'bio':bio}
    form=UserProfileUpdateForm(initial=initial,instance=request.user,data=request.POST or None,files=request.FILES or None)

    if form.is_valid():
        user=form.save(commit=True)
        bio=form.cleaned_data.get('bio',None)
        foto=form.cleaned_data.get('foto',None)

        user.userprofile.bio=bio
        user.userprofile.foto=foto
        user.userprofile.save()
        messages.success(request,"Profiliniz Güncellendi",extra_tags='success')
        return redirect("/auths/profile/")


    return render(request,"auth/profile/settings.html",context={"form":form})        

def donate(request):

        
    return render(request,"auth/profile/donate.html",)    




def user_profile(request,username):
    user=get_object_or_404(User,username=username)
    postlars=Post.objects.filter(user=user)
    popiler=popilerhaber.objects.filter()

    donate=Donate.objects.filter(alan=user)
    x=Fallowing.objects.filter(fallow=user)
    print(x)
    fallow_ship=Fallowing.objects.filter(fallowed=user,fallow=request.user)
    takip_durum=False
    if fallow_ship.exists():
        takip_durum=True

    return render(request,'auth/profile/profile.html',context={'user':user,'takip_durum':takip_durum,'postlars':postlars,"popiler":popiler,'donate':donate})
   


@login_required(login_url="/auth/login/")
def user_fallowers(request,username):
    user=get_object_or_404(User,username=username)
    fallowers=user.fallowed.all
    data={}
    if request.is_ajax():
        data['is_valid']=True
        context={'user':user,'fallowers':fallowers}
        data['html_fallowers_list']=render_to_string('auth/profile/takiplist.html',context,request)
        return JsonResponse(data)
    return HttpResponseRedirect(reverse('auths:user_profile',kwargs={'username':user.username}))    



def donateyap(request):

    return render(request,"auth/profile/donateyap.html")


def banka(request):

    return render(request,"auth/profile/banka.html")
    

def papara(request):

    return render(request,"auth/profile/papara.html")


def kart(request):

    return render(request,"auth/profile/kart.html")

def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Al İşte Deiştirdin")
            return redirect("/auths/login/")
        else:
            messages.error(request,'Hop bilader aha hata aldın'+str(form.errors))
            return HttpResponseRedirect('/auths/password/')
    else:
        userprofile=UserProfile.objects.all()
        form=PasswordChangeForm(request.user)
        return render(request,'change_password.html',{
            'form':form,'userprofile':userprofile
        })            






         
