from django.contrib import admin
from .models import Category,Product,ProductImage
from django.contrib.admin import *
# Register your models here.

admin.site.site_header="MindUni Kontrol Paneli"


class ImageInline(admin.TabularInline):
    model=ProductImage
    extra=3

class ProductAdmin(admin.ModelAdmin):
    
    list_display=('title','category','status')
    inlines=[ImageInline]
    list_filter=('category','status')
    


class ProductImageAdmin(admin.ModelAdmin):
    list_display=('product','image','create_at')
    

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage,ProductImageAdmin)


