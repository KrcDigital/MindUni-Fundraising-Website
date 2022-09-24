from django.contrib import admin
from .models import Category,pp,ppImage
from django.contrib.admin import *
# Register your models here.

admin.site.site_header="MindUni Kontrol Paneli"


class ImageInline(admin.TabularInline):
    model=ppImage
    extra=3

class ppAdmin(admin.ModelAdmin):
    
    list_display=('title','category','status')
    inlines=[ImageInline]
    list_filter=('category','status')
    


class ppImageAdmin(admin.ModelAdmin):
    list_display=('pp','image','create_at')
    

admin.site.register(Category)
admin.site.register(pp,ppAdmin)
admin.site.register(ppImage,ppImageAdmin)