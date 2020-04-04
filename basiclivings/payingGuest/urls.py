from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="IndexPage"),
    path('details/', views.details, name="DetailPage"),
    path('vendor/', views.vendor_index, name="Vendor Index"),
    path('vendor/logout', views.vendor_logout, name="Logout Vendor"),
    path('vendor/addrooms', views.addrooms, name="addrooms"),
    path('vendor/addrooms/upload_pic', views.upload, name="addrooms"),
    path('vendor/viewrooms', views.viewrooms, name="viewrooms"),
    path('vendor/viewrooms/update', views.updaterooms, name="viewrooms"),
    path('vendor/managestudent', views.managestudent, name="managestudent"),
    path('vendor/manageEmail', views.manageEmail, name="manageEmail"),
    path('vendor/managepayment', views.managepayment, name="managepayment"),
    path('vendor/area', views.area_handle, name="area"),
    path('vendor/addrooms/submit', views.submitRoom, name="submit"),
    path('vendor/Add', views.Add, name="Add"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
