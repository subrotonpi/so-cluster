from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cluster/', include('cluster.urls')),
    path('admin/', admin.site.urls),
    path('', include('cluster.urls')),
    
]