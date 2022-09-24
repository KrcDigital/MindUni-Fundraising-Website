from django.urls import path,re_path
from .views import *

app_name="tanitim"

urlpatterns = [
    
    path('',tanitim,name="tanitim"),
    
    
]