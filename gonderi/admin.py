from django.contrib import admin
from .models import Gonderiler
from django.contrib import admin
from .models import Gonderiler,Comment
# Register your models here.

class GonderiAdmin(admin.ModelAdmin):
    
    list_display=["user","date"]
    list_display_links=["date"]
    list_filter=["date","user"]
    
   

    class Meta:
        model=Gonderiler
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment','gonderi','user','status']
    list_filter = ['status']
    





admin.site.register(Gonderiler,GonderiAdmin)
admin.site.register(Comment,CommentAdmin)