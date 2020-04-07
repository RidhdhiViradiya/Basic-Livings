from itertools import count

from django.db.models import Max
import mysql.connector
from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from django.contrib import messages
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
import json
from django.contrib.auth.decorators import login_required
from accounts.models import City, Area, User, Packages
from django.template import RequestContext

from .forms import ImageUploadForm
from .models import Room, RoomImage
from django.contrib.auth.models import auth
# from ..accounts.models import City
# error in importing City model
# Create your views here.


def Add(request):
    return render(request, 'payingGuest/vendor/Add.html')


def index(request):
    return render(request, 'payingGuest/index.html')


def details(request):
    return render(request, 'payingGuest/details.html')


@login_required(login_url="/accounts/")
def vendor_index(request):
    return render(request, 'payingGuest/vendor/index.html')


@login_required(login_url="/accounts/")
def addrooms(request):
    city = City.objects.all()
    packages = Packages.objects.all()
    Form = ImageUploadForm(auto_id=False)
    return render(request, 'payingGuest/vendor/addrooms.html', {'cities': city, 'Form': Form, 'packages': packages})


@login_required(login_url="/accounts/")
def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            for file in request.FILES.getlist('image'):
                f = RoomImage()
                myUser = auth.get_user(request)
                usr = User.object.get(user_id=myUser.user_id)
                room = Room.objects.filter(user_id=usr.user_id).aggregate(maxId=Max('room_id'))
                newRoom = Room.objects.get(room_id=room['maxId'])
                f.room_id = newRoom
                f.image_path = file
                f.save()
        else:
            messages.info(request, 'Please Select Valid Images!!')
    return redirect('/payingGuest/vendor/addrooms#step-3')


def getRooms(request):
    myUser = auth.get_user(request)
    usr = User.object.get(user_id=myUser.user_id)
    rooms = Room.objects.filter(user_id=usr.user_id)
    rooms_images = RoomImage.objects.filter(room_id__in=rooms)
    return rooms, rooms_images


@login_required(login_url="/accounts/")
def viewrooms(request):
    rooms, rooms_images = getRooms(request)
    data = {'rooms': rooms, 'room_images': rooms_images, 'rooms_count': rooms.count()}
    return render(request, 'payingGuest/vendor/viewrooms.html', data)


@login_required(login_url="/accounts")
def updaterooms(request):
    if request.method == 'POST':
        roomid = request.GET.get('id')
        room = Room.objects.get(room_id=roomid)
        vacantBeds = request.POST['vacantBeds']
        rentPerBed = request.POST['rentPerBed']
        deposit = request.POST['deposit']
        gender = request.POST['gender']

        room.vacant_beds = vacantBeds
        room.rent_per_bed = rentPerBed
        room.deposit = deposit
        room.gender = gender

        room.save(update_fields=['vacant_beds', 'rent_per_bed', 'deposit', 'gender'])

        print(vacantBeds, rentPerBed, deposit, gender)
        return redirect('/payingGuest/vendor/viewrooms')
    else:
        return redirect('/payingGuest/vendor/viewrooms')


@login_required(login_url="/accounts/")
def managestudent(request):
    return render(request, 'payingGuest/vendor/managestudent.html')


@login_required(login_url="/accounts/")
def managepayment(request):
    return render(request, 'payingGuest/vendor/managepayment.html')


@login_required(login_url="/accounts/")
def manageEmail(request):
    return render(request, 'payingGuest/vendor/manageEmail.html')


def area_handle(request):
    areas = int(request.POST['id'])
    print(areas)
    areas_list = Area.objects.filter(city_id=areas)
    print(areas_list)
    myList = []
    for area in areas_list:
        tup = (area.area_id, area.area_name)
        myList.append(tup)

    print(myList)
    json_data = json.dumps(myList)
    print(json_data)
    return HttpResponse(json_data)


@login_required(login_url="/accounts/")
def submitRoom(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        totalBeds = request.POST['totalBeds']
        vacantCount = request.POST['vacantCount']
        rentPerBed = request.POST['rentPerBed']
        deposit = request.POST['deposit']
        available = request.POST['available']
        address = request.POST['address']
        instructions = request.POST['instructions']
        area = request.POST['area']
        amenities = request.POST.getlist('amenities')
        myAmenities = ""
        leng = len(amenities)
        for i in amenities:
            if leng == 1:
                myAmenities += i
            else:
                myAmenities += i + ','
            leng -= 1

        print(gender, totalBeds, vacantCount, rentPerBed, deposit, available, address, instructions, area, myAmenities)
        areas = Area.objects.get(area_id=area)
        myUser = auth.get_user(request)
        usr = User.object.get(user_id=myUser.user_id)
        todays = date.today() + relativedelta(months=+2)
        room = Room(user_id=usr, exp_date=todays, address=address, no_of_beds=totalBeds, vacant_beds=vacantCount, rent_per_bed=rentPerBed, deposit=deposit, available_from=available, amenities=myAmenities, gender=gender, special_instruction=instructions, area_id=areas)
        room.save()
        messages.success(request, 'Room Added!!')
        return redirect('/payingGuest/vendor/addrooms#step-2')
    else:
        print("None")

    return render(request, 'payingGuest/vendor/addrooms.html')


@login_required(login_url="/accounts/")
def vendor_logout(request):
    auth.logout(request)
    return redirect('/')

# Student Side
def viewpg(request):
    return render(request, 'payingGuest/viewpg.html')

def viewroom(request):
    return render(request, 'payingGuest/viewroom.html')
