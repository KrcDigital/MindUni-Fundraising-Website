from django.urls import path,re_path
from .views import *

app_name="odeme"

urlpatterns = [
    
    path('',odeme,name="odeme"),
    
    
]