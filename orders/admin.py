from django.contrib import admin
from django.contrib.admin import *
# Register your models here.
from .models import ShopCart,Order,OrderDetail

class ShopCartAdmin(admin.ModelAdmin):
    list_display=['user','product','price','quantity','amount']
    list_filter=['user']



class OrderAdmin(admin.ModelAdmin):
    list_display=['user','create_at','code']
    list_filter=['user']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display=['user','product','order','create_at',]
    list_filter=['user']



admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)
