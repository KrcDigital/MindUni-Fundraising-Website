from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.contrib.auth import *
from django.conf import settings

app_name = "auths"

urlpatterns = [
    path('profile/',postlar, name="postlar"),

    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('settings/',view=user_settings, name="user-settings"),
    path('donate/',view=donate, name="donate"),
    path('donateyap/',view=donateyap, name="donateyap"),
    path('banka/',view=banka, name="banka"),
    path('papara/',view=papara, name="papara"),
    path('kart/',view=kart, name="kart"),
    path('password/',view=change_password, name="change_password"),
 
 
    

    path('<username>',view=user_profile, name='user-profile'),
    
    

    
    ]