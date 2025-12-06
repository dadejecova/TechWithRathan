from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import include
from accounts import views as AccountsViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('academy/', include('academy.urls')),

    path('register/', AccountsViews.register, name='register'),
    path('login/', AccountsViews.login, name='login'),
    path('logout/', AccountsViews.logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
