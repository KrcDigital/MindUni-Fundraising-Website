from django.urls import path,re_path
from .views import *


app_name="bakiye"

urlpatterns = [
    
   

    path('', bakiye_ekle,name="bakiye"),
    path('kupon/', kupon,name="kupon"),
    path('odeme_bildirimi/', odemebilgi,name="odeme"),


]
    
