from django.urls import path,re_path
from .views import *

app_name="post"

urlpatterns = [
    path('create', project_create,name="create"),
    path('index', project_index,name="index"),

    path('<slug>', project_detail, name='detail'),
    
    
    path('<slug>/update/', project_update,name="update"),
    
    path('<slug>/add-remove-favorite/', add_or_remove_favorite,name="add-remove-favorite"),

    path('<slug>/delete/', project_delete,name="delete"),
]