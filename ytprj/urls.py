from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('yt_auth/', include('userauths.urls')),   
    path("c/", include("channel.urls")),
    path("studio/", include("useradmin.urls")),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
