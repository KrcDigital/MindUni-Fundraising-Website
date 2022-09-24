from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.contrib.auth import *
from django.conf import settings
#from products import *
#from products.views import *
#from products.models import Product

from .views import *
#from orders.models import *

app_name="orders"

urlpatterns = [
    path('shopcart/',shopcart, name="shopcart"),
    path('',index, name="index"),
    path('addtocart/<int:id>',addtocart, name="addtocart"),
    path('deletefromcart/<int:id>',deletefromcart, name="deletefromcart"),
    path('checkout/',checkout, name="checkout"),
    path('detail/<int:id>',order_detail, name="orderdetail"),

] 