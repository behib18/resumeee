from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('resume/', include('background_info.urls')),
    path('contact/', include('contact.urls')),
    path('projects/', include('projects.urls')),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
