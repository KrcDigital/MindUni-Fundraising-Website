from django.contrib import admin
from .models import Category,Fon,FonImage,Comment
from django.contrib.admin import *
# Register your models here.

admin.site.site_header="MindUni Kontrol Paneli"


class ImageInline(admin.TabularInline):
    model=FonImage
    extra=3

class FonAdmin(admin.ModelAdmin):
    
    list_display=('title','category','status')
    inlines=[ImageInline]
    list_filter=('category','status')
    


class FonImageAdmin(admin.ModelAdmin):
    list_display=('fon','image','create_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']



admin.site.register(Category)
admin.site.register(Fon,FonAdmin)
admin.site.register(FonImage,FonImageAdmin)
admin.site.register(Comment)