from django.contrib import admin
from .models import Post,Category,Category2,Category3,Category4,Category5
from .models import UserProfile,FavoriteBlog
from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    list_display=["title","date","slug","category","category2","category3"]
    list_display_links=["date"]
    list_filter=["date","category","category2","category3"]
    search_fields=["title","content"]
    list_editable=["title"]
   

    class Meta:
        model=Post
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    
admin.site.register(Category)
admin.site.register(Category2)
admin.site.register(Category3)
admin.site.register(Category4)
admin.site.register(Category5)




admin.site.register(Post,PostAdmin)
admin.site.register(UserProfile)
admin.site.register(FavoriteBlog)
admin.site.register(Comment)