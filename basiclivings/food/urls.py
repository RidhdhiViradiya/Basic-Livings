
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="IndexPage"),
    path('vendor/', views.vendor_index, name="Vendor Index"),
    path('vendor/addmess', views.addmess, name="Add Mess"),
    path('vendor/viewmess', views.viewmess, name="View Mess"),
    path('vendor/viewfoodtype', views.viewfoodtype, name="View Food Type"),
    path('vendor/managestudent', views.managestudent, name="Manage Student"),
    path('vendor/manageEmail', views.manageEmail, name="Manage Email"),
    path('vendor/addfoodtype', views.addfoodtype, name="Add Food Type"),

    # Student side
    path('viewmess', views.viewmess, name="View Mess"),
]
