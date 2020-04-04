import os
from django.shortcuts import render

# Create your views here.


def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_path = os.path.join(BASE_DIR, 'bootstrap')
    params = {'dir': base_path}
    return render(request, 'food/index.html', params)

def vendor_index(request):
    return render(request, 'food/vendor/index.html')

def addmess(request):
    return render(request, 'food/vendor/addmess.html')

def viewmess(request):
    return render(request, 'food/vendor/viewmess.html')

def viewfoodtype(request):
    return render(request, 'food/vendor/viewfoodtype.html')

def manageEmail(request):
    return render(request, 'food/vendor/manageEmail.html')

def managestudent(request):
    return render(request, 'food/vendor/managestudent.html')

def addfoodtype(request):
    return render(request, 'food/vendor/addfoodtype.html')

# student side

def viewmess(request):
    return render(request, 'food/viewmess.html')