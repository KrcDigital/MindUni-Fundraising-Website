"""blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from main.views import main
from django.conf.urls.static import static
from django.conf import settings
from takip.views import add_fallow_or_delete
from django.urls import path, register_converter
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', main),
    path('be9232c.txt/',include("mail.urls")),

    path('order/',include("orders.urls")),
    path('gonderi/',include("gonderi.urls")),
    path('bakiye_ekle/',include("bakiye.urls")),

    path('auths/',include("auths.urls")),
    path('project/',include("post.urls")),
    path('shop/',include("shop.urls")),
    path('fonlama/',include("fonlamalar.urls")),
    path('haberler/',include("haberler.urls")),

    path('fallowing/',include('takip.urls',namespace='fallowing')),

    path('product/',include("products.urls")),

    path('tanitim/',include("tanitim.urls")),
    path('odeme/',include("odeme.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
