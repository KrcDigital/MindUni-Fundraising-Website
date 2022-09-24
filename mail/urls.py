from django.urls import path,re_path,include
from .views import *

app_name="mail"

urlpatterns = [
    
    path('',mail,name="mail"),
    

]