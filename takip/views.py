
from django.http import JsonResponse
from .models import Fallowing,User
# Create your views here.

def add_fallow_or_delete(request):
   if request.method=='POST':
     fallowed=request.POST.get("fallow",None)
     fallow=request.POST.get("fallowed",None)

     fallowed=User.objects.filter(username=fallowed)
     fallow=User.objects.filter(username=fallow)


     if ((fallowed.exists() and fallowed.count() ==1) and ( fallow.exists() and fallow.count()==1)):
        fallow=fallow.first()
        fallowed=fallowed.first()
        data=Fallowing.add_or_delete_fallowed(fallowed=fallowed,fallow=fallow)

        return JsonResponse(data=data)

   return JsonResponse(data={'msg':'error'})    



  