from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('misha/', include('blog.urls')),
    path('rishat/', include('blog.urls')),
    
]
