from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('superpuperuser/', admin.site.urls),
    path('',include('shop.urls'))
]
