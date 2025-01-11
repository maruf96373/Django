# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task13/', include('task13.urls')),  
    path('task14/', include('task14.urls')),  
    path('task15/', include('task15.urls')), 
    path('task16/', include('task16.urls')), 
    path('task17/', include('task17.urls')), 
    path('task18/', include('task18.urls')), 
       path('task19/', include('task19.urls')),
          path('task20/', include('task20.urls')),
               path('task22/', include('task22.urls')),         
]
