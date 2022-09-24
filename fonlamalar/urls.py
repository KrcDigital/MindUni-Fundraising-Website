from django.urls import path,re_path
from .views import fon_index,fon_detail,detay


app_name="fonlamalar"

urlpatterns = [
    
   
    path('', fon_index , name='fon'),
    path('detay/',detay, name="detay"),
    path('<int:fon_id>/', fon_detail, name='detail'),


]
    
