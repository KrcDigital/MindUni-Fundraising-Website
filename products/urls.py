




from django.urls import path,re_path
from .views import *

app_name="products"

urlpatterns = [
    
path('<int:product_id>/', detail, name='detail'),
]