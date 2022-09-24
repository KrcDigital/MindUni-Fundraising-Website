from django.contrib import admin
from .models import Donate
# Register your models here.
class DonateAdmin(admin.ModelAdmin):
    
    list_display=["veren","alan","miktar"]
    list_display_links=["alan"]
    list_filter=["alan"]
    search_fields=["veren"]
    
   

    class Meta:
        model=Donate
admin.site.register(Donate,DonateAdmin)
