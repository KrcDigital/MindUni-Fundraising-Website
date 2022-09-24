from django.contrib import admin
from .models import Haberler,HaberlerImage,Comment,guncelhaber,popilerhaber,editorhaber
from django.contrib.admin import *
# Register your models here.

admin.site.site_header="MindUni Kontrol Paneli"


class ImageInline(admin.TabularInline):
    model=HaberlerImage
    extra=3

class HaberlerAdmin(admin.ModelAdmin):
    
    list_display=('title','status')
    inlines=[ImageInline]
    list_filter=('category','status')
    
class guncelhaberAdmin(admin.ModelAdmin):
    
    list_display=('haber',)

class editorhaberAdmin(admin.ModelAdmin):
    
    list_display=('haber',)
    
class popilerhaberAdmin(admin.ModelAdmin):
    
    list_display=('haber',)

class HaberlerImageAdmin(admin.ModelAdmin):
    list_display=('haberler','image','create_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']



admin.site.register(Haberler,HaberlerAdmin)
admin.site.register(HaberlerImage,HaberlerImageAdmin)
admin.site.register(Comment)
admin.site.register(guncelhaber,guncelhaberAdmin)
admin.site.register(editorhaber,editorhaberAdmin)

admin.site.register(popilerhaber,popilerhaberAdmin)