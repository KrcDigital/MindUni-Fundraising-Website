from django.contrib import admin
from .models import Kupon,odemebilgi
from django.contrib import admin
from django.contrib.admin import *

# Register your models here.




class KuponAdmin(admin.ModelAdmin):
    
    list_display=["user","date","kupon"]
    list_display_links=["date"]
    list_filter=["date"]
    search_fields=["user"]
    
   

    class Meta:
        model=Kupon

class odemeAdmin(admin.ModelAdmin):
    
    list_display=["user","date","numara"]
    list_display_links=["date"]
    list_filter=["date"]
    search_fields=["user"]
    
   

    class Meta:
        model=odemebilgi



admin.site.register(Kupon,KuponAdmin)

admin.site.register(odemebilgi,odemeAdmin)
