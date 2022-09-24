from django.urls import path,re_path
from django.conf.urls import url
from .views import add_fallow_or_delete
from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.contrib.auth import *
from django.conf import settings
from django.http import HttpResponse

app_name = 'takip'

urlpatterns = [
        path('add-or-delete-fallow/',add_fallow_or_delete,name="add-or-delete-fallow",),
    
]
