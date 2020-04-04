from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="LandingPage"),
    path('register', views.register, name="submission"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('area', views.area_handle, name="area"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
