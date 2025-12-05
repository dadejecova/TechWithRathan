from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('academy/', include('academy.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
