from django.urls import path,re_path
from .views import *


app_name="haberler"

urlpatterns = [
    
   
    path('', haberler_index , name='haber'),
    path('<slug>', haberler_detail, name='detail'),
    path('kategori_teknoloji/', teknoloji_index , name='teknoloji'),
    path('kategori_gelecek/', gelecek_index , name='gelecek'),

    path('kategori_sosyal/', sosyal_index , name='sosyal'),

]
    
