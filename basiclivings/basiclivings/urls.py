from django.conf.urls.static import static

from . import views, settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.index, name="MainHome"),
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('payingGuest/', include('payingGuest.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
