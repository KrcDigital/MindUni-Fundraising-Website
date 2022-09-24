from django.urls import path,re_path,include
from .views import *

app_name="shop"

urlpatterns = [
    
    path('',shop_index,name="shop"),
    
    path('',product, name='product'),

]