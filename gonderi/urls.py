from django.urls import path,re_path
from .views import *


app_name="gonderi"

urlpatterns = [
    
   
    path('', gonderiler_index , name='gonderi'),
    path('addcomment/<int:id>', addcomment , name='addcomment'),

    path('create', gonderi_create,name="create"),


]
    
